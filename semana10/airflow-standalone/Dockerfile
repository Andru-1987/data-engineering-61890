FROM apache/airflow:slim-latest-python3.11

COPY requirements.txt /requirements.txt

RUN pip install --no-cache-dir -r /requirements.txt

USER root

RUN apt-get update && apt-get install -y \
    wget

COPY start.sh /start.sh

RUN chmod +x /start.sh

USER airflow

ENTRYPOINT ["/bin/bash","/start.sh"]

EXPOSE 8080