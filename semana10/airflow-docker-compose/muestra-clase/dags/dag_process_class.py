import datetime

from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.utils.helpers import chain

from modules import print_surname, print_country, print_name


task_functions = [ print_country, print_name, print_surname]
task_ids = ["country","name","apellido"]
task_arg = ["peru","anderson","ocana"]


with DAG(
    dag_id="mi_primer_dag_identidad",
    start_date=datetime.datetime(2024, 6, 24),
    schedule="@daily",
    doc_md='dag que creara tres etapas'
) as dag:
    
    task_list = [
        PythonOperator(task_id=id,python_callable=cb,op_args=[arg])
        for id,cb,arg in zip(task_ids,task_functions,task_arg)]
    chain(*task_list)

