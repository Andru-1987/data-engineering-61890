import datetime as dt
from airflow import DAG
from airflow.operators.python import PythonOperator

with DAG(
        dag_id="hello-world",
        schedule="@daily",
        start_date=dt.datetime(year=2022, month=10, day=27),
        end_date=None,
        tags=["learning", "examples"],
        doc_md="Esto es una dag idempotente"

) as bifrost_workflow_dag:
    
    def print_hello(**context):
        return "Hello World..!"


    hello_operator = PythonOperator(dag=bifrost_workflow_dag, task_id="hello-operator",
                                    python_callable=print_hello)

hello_operator