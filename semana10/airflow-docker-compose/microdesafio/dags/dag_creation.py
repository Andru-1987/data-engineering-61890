from datetime import datetime, timedelta
from email.policy import default

from airflow import DAG
from airflow.providers.common.sql.operators.sql import SQLExecuteQueryOperator

default_args={
    'owner': 'anderson_oca',
    'retries':3,
    'retry_delay': timedelta(minutes=5)
}

DAG_ID = "postgres_operator_dag"

with DAG(
    default_args=default_args,
    dag_id=DAG_ID,
    description= 'Dag conexion a postgres',
    start_date=datetime(2024,6,26),
    schedule_interval='@once'
    ) as dag:



    create_table = SQLExecuteQueryOperator(
        task_id="create_table",
        sql="""
            CREATE TABLE IF NOT EXISTS fin_mundo (
            dt DATE,
            pais VARCHAR(30)
            );
          """,
           conn_id="postgres_operator_dag"
        )


    populate_data = SQLExecuteQueryOperator(
        task_id='insertar_en_tabla',
        sql="""
            INSERT INTO fin_mundo 
            (dt,pais)
            values 
                ('2025-12-12', 'Colombia'),
                ('2035-08-15', 'Brasil'),
                ('2030-09-21', 'Argentina'),
                ('2045-07-13', 'Chile'),
                ('2028-11-17', 'Ecuador'),
                ('2032-03-19', 'Peru'),
                ('2026-08-18', 'Uruguay'),
                ('2037-05-22', 'Paraguay'),
                ('2080-12-12', 'Venezuela'),
                ('2071-12-12', 'Mexico');
        """,
        conn_id="postgres_operator_dag"
    )
    
    create_table >> populate_data
