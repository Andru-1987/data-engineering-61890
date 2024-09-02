from datetime import datetime, timedelta
from airflow import DAG 
import airflow.utils.dates
from airflow.operators.python import PythonOperator
from airflow.contrib.sensors.file_sensor import FileSensor

from mailer import send_email,print_message,get_file_name

default_args={
    'owner': 'ander_o',
    'depends_on_past': False,
    'email': ['anderson.coder.space@gmail.com'],
    'email_on_retry':True,
    'email_on_failure': False,
    'retries':10,
    'retry_delay': timedelta(minutes=1)
}

with DAG(
    dag_id='data_sensors_DBU',
    start_date=airflow.utils.dates.days_ago(3),
    schedule_interval='@daily',
    default_args=default_args,
    catchup = False
) as dag:



    file_sensor = FileSensor(
        task_id="sensar_archivo",
        poke_interval=10,        
        timeout=60 * 30,            # 30 minutes timeout
        filepath='/opt/airflow/data/data-*.csv',
        fs_conn_id='csv_files',
        mode='poke',
        soft_fail=False   
    ),


    get_file_name_task = PythonOperator(
        task_id='get_file_name',
        python_callable=get_file_name
    )

    imprimir = PythonOperator(
        task_id="print_message",
        python_callable= print_message
    )

    send_email = PythonOperator(
        task_id="mail_sender",
        python_callable=send_email,
    )

file_sensor >> get_file_name_task >> imprimir >> send_email