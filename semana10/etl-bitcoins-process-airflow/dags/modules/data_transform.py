import json
import pandas as pd
from datetime import datetime


def transformar_data(exec_date, path):
    print(f"Transformando la data para la fecha: {exec_date}")

    json_path = (
        f"{path}/raw_data/data_{date.year}-{date.month}-{date.day}-{date.hour}.json"
    )
    csv_path = (
        f"{path}/raw_data/data_{date.year}-{date.month}-{date.day}-{date.hour}.csv"
    )

    date = datetime.strptime(exec_date, "%Y-%m-%d %H")
    with open(json_path, "r") as json_file:
        loaded_data = json.load(json_file)
    # Extraer la data en tabla
    datax = loaded_data["data"]
    dt = pd.DataFrame.from_dict(datax, orient="index")
    # Fiiltrar el topico de interes: mining_stats
    extract = dt.loc["mining_stats"][0]
    e = (
        pd.DataFrame.from_dict(extract, orient="index", columns=["value"])
        .transpose()
        .reset_index(drop=True)
    )
    e["Date"] = loaded_data["status"]["timestamp"]
    e.to_csv(csv_path, index=False, mode="a", header=False)
