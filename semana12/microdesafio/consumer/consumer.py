from kafka import KafkaConsumer
import json
import sqlite3
import os



table_name_consumer = os.getenv("DATABASE_TABLE_CONSUMER")
topic = os.getenv("TOPIC")


def running_process():
    print(f"PRODUCER IS ACTIVE RUNNING AT TOPIC --> {topic}")

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

def insert_into_db(data):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(f'''
        INSERT INTO {table_name_consumer} (country_code, mensaje, fecha)
        VALUES (?, ?, ?)
    ''', (data['country_code'], data['mensaje'], data['fecha']))
    conn.commit()
    conn.close()



def consume_messages():
    """ Consume messages from Kafka and insert them into the database. """
    # Initialize Kafka Consumer
    running_process()
    
    consumer = KafkaConsumer(
        topic,
        bootstrap_servers='kafka-broker:9092',
        auto_offset_reset='earliest',
        value_deserializer=lambda m: json.loads(m.decode('utf-8'))
    )
    
    
    # Process messages from Kafka
    for message in consumer:
        data = message.value
        print(data)
        insert_into_db(data)
        print(f"Inserted data into DB: {data}")

if __name__ == "__main__":
    # Ensure the database table is created
    create_table_if_not_exists()
    
    # Start consuming messages
    consume_messages()