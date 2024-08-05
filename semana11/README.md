_PRESENTACION_
[Microdesafio](https://docs.google.com/presentation/d/e/2PACX-1vSIGotL4kNsKWr34WuO11kaTMbowocHU-Wl6DItUct0IUb0_vCAYFqHAX5EVX5wMQ/pub?start=false&loop=false&delayms=3000)

_EMAIL CONFIG_
```toml
[email]
email_backend = airflow.utils.email.send_email_smtp
smtp_host = smtp.gmail.com
smtp_starttls = True
smtp_ssl = False
smtp_user = your-email@gmail.com
smtp_password = your-email-password
smtp_port = 587
smtp_mail_from = your-email@gmail.com

```
Bibliografia:
[AirFlow SMTP](https://airflow.apache.org/docs/apache-airflow/stable/howto/email-config.html)
[TASKGROUPS](https://jashbhatt776.medium.com/organize-airflow-dags-with-task-groups-627f5b6f1098) 
[AIRFLOW VARIABLES](https://www.astronomer.io/docs/learn/airflow-variables?tab=airflow#create-an-airflow-variable)


