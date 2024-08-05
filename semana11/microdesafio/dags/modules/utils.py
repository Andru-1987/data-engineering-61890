import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

from airflow.models import Variable

def generate_end_of_world_estimates():
    countries = ['Argentina', 'Brasil', 'Colombia', 'Chile', 'Paraguay', 'Uruguay', 'Venezuela', 'Peru', 'Ecuador', 'Bolivia', 'México']
    acronyms = ['AR', 'BR', 'CO', 'CL', 'PY', 'UR', 'VE', 'PE', 'EC', 'BO', 'MX']
    end_of_world_years = [2040, 2080, 2095, 2100, 2089, 2093, 2054, 2078, 2079, 2083, 2071]

    texts = [
        f'Pais {country} ({acronym}), Fecha fin mundo estimada: {year}'
        for country, acronym, year in zip(countries, acronyms, end_of_world_years)
    ]

    return '\n'.join(texts)
    


def send_email(**context):
    subject = context["var"]["value"].get("subject_mail")
    from_address = context["var"]["value"].get("email")
    password = context["var"]["value"].get("email_password")
    to_address = context["var"]["value"].get("to_address")

    # Create a MIMEText object
    msg = MIMEMultipart()
    msg['From'] = from_address
    msg['To'] = to_address
    msg['Subject'] = subject

    # Attach the body with the msg instance
    msg.attach(MIMEText(generate_end_of_world_estimates(), 'plain'))

    print(
    f"""
    subject:    {subject}
    from_address:   {from_address}
    password:   {password}
    to_address: {to_address}
    """
    )

    try:
        # Create an SMTP session
        server = smtplib.SMTP('smtp.gmail.com', 587)  # Use your SMTP server and port
        server.starttls()  # Enable security

        # Login to the server
        server.login(from_address, password)

        # Send the email
        text = msg.as_string()
        server.sendmail(from_address, to_address, text)
        server.quit()
        print("Email sent successfully")
    except Exception as e:
        print(f"Failed to send email: {str(e)}")


# To fail


def generate_end_of_world_estimates_context(**context):
    countries = ['Argentina', 'Brasil', 'Colombia', 'Chile', 'Paraguay', 'Uruguay', 'Venezuela', 'Peru', 'Ecuador', 'Bolivia', 'México']
    acronyms = ['AR', 'BR', 'CO', 'CL', 'PY', 'UR', 'VE', 'PE', 'EC', 'BO', 'MX']
    end_of_world_years = [2040, 2080, 2095, 2100, 2089, 2093, 2054, 2078, 2079, 2083, 2071]

    texts = [
        f'Pais {country} ({acronym}), Fecha fin mundo estimada: {year}'
        for country, acronym, year in zip(countries, acronyms, end_of_world_years)
    ]

    estimates = '\n'.join(texts)
    context['ti'].xcom_push(key='estimates', value=estimates)


def fail_task(**context):
    print(context)
    estimates = context['ti'].xcom_pull(task_ids='generate_email_body', key='estimates')
    raise Exception(f"This task is intentionally failing. Estimates: {estimates}")

def get_email_subject(**context):
    retry_count = context['ti'].try_number
    base_subject = Variable.get("subject_mail")
    if retry_count > 0:
        subject = f"{base_subject} (Retry Attempt {retry_count - 1}) :) "
    else:
        subject = base_subject + " ^_^ "
    context['ti'].xcom_push(key='email_subject', value=subject)