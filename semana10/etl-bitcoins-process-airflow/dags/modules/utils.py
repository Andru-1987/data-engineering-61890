from dotenv import load_dotenv
from datetime import datetime, timedelta
import os


load_dotenv()  # take environment variables from .env.


def get_schema()->str:
    return os.getenv("REDSHIFT_SCHEMA")

def get_credentials() -> dict:

    url = os.getenv("REDSHIFT_URL")
    user = os.getenv("REDSHIFT_USER")
    pwd = os.getenv("REDSHIFT_PWD")
    port = os.getenv("REDSHIFT_PORT")
    data_base = os.getenv("REDSHIFT_DB")

    return {
        "host": url,
        "username": user,
        "database": data_base,
        "port": port,
        "pwd": pwd,
    }


def get_defaultairflow_args():
    return {
        "owner": "anderson_oca",
        "depends_on_past": False,
        "start_date": datetime(2023, 1, 1),
        "email_on_failure": False,
        "email_on_retry": False,
        "retries": 1,
        "catch"
        "retry_delay": timedelta(minutes=5),
    }
