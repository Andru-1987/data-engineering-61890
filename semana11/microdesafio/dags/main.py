from datetime import datetime
from modules import send_email

from airflow.models import DAG

from airflow.operators.python_operator import PythonOperator
from airflow.operators.bash import BashOperator


default_args={
    'owner': 'anderson_o',
    'start_date': datetime(2024,7,3),
    'email_on_retry': True
}

with DAG(
    dag_id='dag_smtp_email_automatico',
    default_args=default_args,
    schedule_interval='@daily',
    ) as dag:

    email_massive = PythonOperator(
        task_id="mail_sender",
        python_callable=send_email,
        provide_context=True
    )

    printer_airflow_variables= BashOperator(
        task_id="printer_variables",
        bash_command='echo "{{ var.value.subject_mail }} --> {{ var.value.email }} -> {{ var.value.email_password }}"',
    )


    printer_airflow_variables >> email_massive 
