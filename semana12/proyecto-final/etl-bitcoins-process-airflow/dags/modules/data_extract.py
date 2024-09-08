import json
import requests
from datetime import datetime


# funcion de extraccion de datos
def extraer_data(exec_date, path):
    date = datetime.strptime(exec_date, "%Y-%m-%d %H")
    json_path = (
        f"{path}/raw_data/data_{date.year}-{date.month}-{date.day}-{date.hour}.json"
    )
    url = "https://data.messari.io/api/v1/assets/bitcoin/metrics"
    headers = {"Accept-Encoding": "gzip, deflate"}

    try:
        print(f"Adquiriendo data para la fecha: {exec_date}")
        response = requests.get(url, headers=headers)
        if response:
            print("Success!")
            data = response.json()
            with open(
                json_path,
                "w",
            ) as json_file:
                json.dump(data, json_file)
            print("JSON File stored")
        else:
            print("An error has occurred.")
    except ValueError as e:
        print("Formato datetime deberia ser %Y-%m-%d %H", e)
        raise e
