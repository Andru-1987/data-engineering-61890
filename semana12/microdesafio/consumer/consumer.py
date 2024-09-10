import sqlite3
import json
import os
import logging
from kafka import KafkaConsumer

# Configuración del logger
logging.basicConfig(
    level=logging.INFO,
    format='CONSUMER: %(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.StreamHandler(),  # Muestra los logs en la consola
        logging.FileHandler('/logger.log')  # Guarda los logs en un archivo
    ]
)

logger = logging.getLogger('KafkaConsumer')

table_name_consumer = os.getenv("DATABASE_TABLE_CONSUMER")
topic = os.getenv("TOPIC")

def running_process():
    logger.info(f"CONSUMER IS ACTIVE RUNNING AT TOPIC --> {topic}")

def get_db_connection():
    conn = sqlite3.connect('/database/db.sqlite3')
    return conn

def create_table_if_not_exists():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(f'''
        CREATE TABLE IF NOT EXISTS {table_name_consumer} (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            country_code TEXT,
            mensaje TEXT,
            fecha DATE
        )
    ''')
    conn.commit()
    conn.close()
    logger.info(f"Table {table_name_consumer} created or already exists.")

def insert_into_db(data):
    conn = get_db_connection()
    cursor = conn.cursor()
    try:
        cursor.execute(f'''
            INSERT INTO {table_name_consumer} (country_code, mensaje, fecha)
            VALUES (?, ?, ?)
        ''', (data['country_code'], data['mensaje'], data['fecha']))
        conn.commit()
        logger.info(f"Inserted data into DB: {data}")
    except Exception as e:
        logger.error(f"Error inserting data into DB: {e}")
    finally:
        conn.close()

def consume_messages():
    """ Consume messages from Kafka and insert them into the database. """
    running_process()
    
    try:
        consumer = KafkaConsumer(
            topic,
            bootstrap_servers='kafka-broker:9092',
            auto_offset_reset='earliest',
            value_deserializer=lambda m: json.loads(m.decode('utf-8'))
        )
        logger.info("Kafka Consumer connected successfully.")
    except Exception as e:
        logger.error(f"Failed to connect to Kafka broker: {e}")
        return

    # Process messages from Kafka
    for message in consumer:
        data = message.value
        logger.info(f"Received message: {data}")
        insert_into_db(data)

if __name__ == "__main__":
    # Ensure the database table is created
    create_table_if_not_exists()
    
    # Start consuming messages
    consume_messages()
