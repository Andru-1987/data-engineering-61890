import sqlite3
import time
from kafka import KafkaProducer
import json
import os

table_name_producer = os.getenv("DATABASE_TABLE_PRODUCER")
topic=os.getenv("TOPIC")

def running_process():
    print(f"PRODUCER IS ACTIVE RUNNING AT TOPIC --> {topic}")
    
def get_db_connection():
    conn = sqlite3.connect('/database/db.sqlite3')
    conn.row_factory = sqlite3.Row
    return conn

def create_table_if_not_exists():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(f'''
        CREATE TABLE IF NOT EXISTS {table_name_producer} (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            country TEXT,
            country_code TEXT,
            mensaje TEXT,
            fecha   DATE,
            timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    conn.commit()
    conn.close()

def get_last_row_id(cursor):
    cursor.execute(f"SELECT seq FROM sqlite_sequence WHERE name='{table_name_producer}'")
    row = cursor.fetchone()
    return row[0] if row else None

def produce_messages():

    producer = KafkaProducer(
        bootstrap_servers='kafka-broker:9092',
        value_serializer=lambda v: json.dumps(v).encode('utf-8'))
    
    conn = get_db_connection()
    cursor = conn.cursor()
    last_timestamp = None

    create_table_if_not_exists()

    running_process()

    while True:
        if last_timestamp is None:
            cursor.execute(f'SELECT timestamp FROM {table_name_producer} ORDER BY timestamp DESC LIMIT 1')
            row = cursor.fetchone()
            last_timestamp = row[0] if row else None

        cursor.execute(f'SELECT * FROM {table_name_producer} WHERE timestamp > ?', (last_timestamp,))
        rows = cursor.fetchall()
        for row in rows:
            producer.send(topic, dict(row))
            producer.flush()
            last_timestamp = row['timestamp']  # Update the last_timestamp to the latest row's timestamp

        time.sleep(1)


if __name__ == "__main__":
    produce_messages()