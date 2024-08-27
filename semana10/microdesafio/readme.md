# Microdesafio 
- Create of folders and download yml
```bash

curl -LfO 'https://airflow.apache.org/docs/apache-airflow/2.9.2/docker-compose.yaml'

mkdir -p ./microdesafio/{logs,dags,config,plugins}

echo -e "AIRFLOW_UID=$(id -u)" > ./.env


```

- Start project
```bash
docker compose up airflow-init
```
```bash
docker compose up
```

---

> [!TIP]
> Cada vez que tenemos que colocar un dato de conexion para una base de datos externa o interna en nuestra red, hay que identificarla y llamarla desde el sector de admin -> connections con el host indicado 
