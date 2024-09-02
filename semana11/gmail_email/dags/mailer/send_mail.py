import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


def send_email(**context):
    subject = context["var"]["value"].get("subject_mail")
    from_address = context["var"]["value"].get("email")
    password = context["var"]["value"].get("email_password")
    to_address = context["var"]["value"].get("to_address")

    file_name = context['ti'].xcom_pull(task_ids='get_file_name', key='file_name')

    # Create a MIMEText object
    msg = MIMEMultipart()
    msg['From'] = from_address
    msg['To'] = to_address
    msg['Subject'] = subject

    # Create HTML content
    html_content = f"""
    <html>
    <body>
        <p>Hola!</p>
        <p>El siguiente CSV fue detectado:</p>
        <p><strong>{file_name}</strong></p>
    </body>
    </html>
    """

    # Attach HTML content
    msg.attach(MIMEText(html_content, 'html'))

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

