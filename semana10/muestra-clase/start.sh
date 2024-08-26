#!/bin/bash
airflow standalone

airflow db migrate

airflow users create \
    --username admin \
    --firstname anderson \
    --lastname oca \
    --role Admin \
    --email andru.ocatorres@gmail.com 

airflow webserver --port 8080

airflow scheduler