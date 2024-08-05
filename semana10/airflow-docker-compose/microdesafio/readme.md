# Microdesafio 
- [Display microdesafio](https://docs.google.com/presentation/d/1MeuLN6zSmRT1SL5nD9Uv-bsqVx9WcGynHhhgO5_8WBI/preview#slide=id.g1ea1e8f090f_0_0)

- Create of folders and download yml
```bash

curl -LfO 'https://airflow.apache.org/docs/apache-airflow/2.9.2/docker-compose.yaml'

mkdir -p ./microdesafio/{logs,dags,config,plugins}

echo -e "AIRFLOW_UID=$(id -u)" > ./microdesafio/.env

```

- Start project
```bash
docker compose up airflow-init
```
```bash
docker compose up
```
