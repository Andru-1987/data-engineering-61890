from airflow import DAG
from airflow.operators.email_operator import EmailOperator
from airflow.operators.python_operator import PythonOperator
from airflow.utils.dates import days_ago
from airflow.utils.dates import days_ago
from airflow.models import Variable


from modules import fail_task, generate_end_of_world_estimates_context,get_email_subject



default_args = {
    'owner': 'ander_o',
    'start_date': days_ago(1),
    'email': ['anderson.coder.space@gmail.com','pabloing1993@gmail.com'],
    'email_on_retry':True,
    'email_on_failure': True,
    'retries':1
}

with DAG(
    'send_end_of_world_estimates',
    default_args=default_args,
    schedule_interval='@daily',

) as dag:

    generate_email_body = PythonOperator(
        task_id='generate_email_body',
        provide_context=True,
        python_callable=generate_end_of_world_estimates_context
    )

    get_email_subject = PythonOperator(
        task_id='get_email_subject',
        provide_context=True,
        python_callable=get_email_subject
    )

    send_email = EmailOperator(
        task_id='send_email',
        to=Variable.get("to_address"),
        subject="{{ task_instance.xcom_pull(task_ids='get_email_subject', key='email_subject') }}",
        html_content="{{ task_instance.xcom_pull(task_ids='generate_email_body', key='estimates') }}"
    )

    fail_task = PythonOperator(
        task_id='fail_task',
        provide_context=True,
        python_callable=fail_task
    )

    generate_email_body >> get_email_subject >> send_email >> fail_task
