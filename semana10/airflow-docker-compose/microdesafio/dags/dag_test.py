from datetime import datetime

from airflow import DAG
from airflow.decorators import task
from airflow.operators.bash import BashOperator


with DAG(
    dag_id="microdesafio_semana_10",
    start_date=datetime(2024, 1, 1),
    schedule="0 0 * * *",
    doc_md="microdesafio para el fin del mundo"
    ) as dag:
    
    init_project = BashOperator(
        task_id="init_project_data_creation",
        bash_command="echo start project")

    @task()
    def airflow():
        print("airflow")

    @task()
    def finish_dag():
        print("dag finish")


    init_project >> airflow() >> finish_dag()