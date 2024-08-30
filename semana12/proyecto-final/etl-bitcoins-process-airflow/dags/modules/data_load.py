from datetime import datetime

import pandas as pd
import psycopg2
from psycopg2.extras import execute_values
from .utils import get_credentials
from .utils import get_schema

def cargar_data(exec_date, path):

    print(f"Cargando la data para la fecha: {exec_date}")
    date = datetime.strptime(exec_date, "%Y-%m-%d %H")
    csv_path = (
        f"{path}/raw_data/data_{date.year}-{date.month}-{date.day}-{date.hour}.csv"
    )

    records = pd.read_csv(csv_path, sep=",")

    print(records.shape)
    print(records.head())
    # conexion a database

    credentials = get_credentials()

    conn = psycopg2.connect(**credentials)
    # Definir columnas
    columns = [
        "mining_algo",
        "network_hash_rate",
        "available_on_nicehash_percent",
        "one_hour_attack_cost",
        "twenty_four_hours_attack_cost",
        "attack_appeal",
        "hash_rate",
        "hash_rate_30d_average",
        "mining_revenue_per_hash_usd",
        "mining_revenue_per_hash_native_units",
        "mining_revenue_per_hash_per_second_usd",
        "mining_revenue_per_hash_per_second_native_units",
        "mining_revenue_from_fees_percent_last_24_hours",
        "mining_revenue_native",
        "mining_revenue_usd",
        "mining_revenue_total",
        "average_difficulty",
        "date",
    ]
    cur = conn.cursor()
    # Define the table name
    table_name = "mining_data"
    # Define the columns you want to insert data into
    columns = columns
    # Generate
    values = [tuple(x) for x in records.to_numpy()]
    insert_sql = f"INSERT INTO {get_schema()}.{table_name} ({', '.join(columns)}) VALUES %s"
    # Execute the INSERT statement using execute_values
    cur.execute("BEGIN")
    execute_values(cur, insert_sql, values)
    cur.execute("COMMIT")
