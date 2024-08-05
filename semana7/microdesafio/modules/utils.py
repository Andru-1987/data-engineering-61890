import pandas as pd
import os
from pytrends.request import TrendReq


def store_data_from_pytrends(data: pd.DataFrame, path):
    if data is None:
        raise ValueError("No data is saved")
        
    data.to_parquet(path, engine='fastparquet') 

def read_data_if_no_data(path:str) -> pd.DataFrame:
    return  pd.read_parquet(path)

def get_data_from_pytrends(keywords:list[str], path, geo, pytrends):

    try:
        pytrends.build_payload(keywords, cat=0, timeframe='today 5-y', geo=geo, gprop='')
        data = pytrends.interest_over_time()[keywords]
        store_data_from_pytrends(data, path)
        return data
    except Exception  as e:
        print({"error":e})
        if not os.path.exists(path):
            raise ValueError("No data storaged")

        return read_data_if_no_data(path)


def store_data_into_list(lista_paises, keywords, pytrends):

    lista_dfs: list[pd.DataFrame] = []

    for geo in lista_paises:
        path: str = f"./data/data_{geo}.parquet"
        data = get_data_from_pytrends(keywords, path, geo, pytrends)

        data["Country"] = geo
        data["Fecha"] = data.index
        data = data.reset_index(drop=True)

        print(data.head())
        lista_dfs.append(data)
    return lista_dfs


def graph_data(data):
    if data is None:
        raise ValueError("Error with no data retrieved")
    ax = data.plot(
        kind="line",
        figsize=(12, 6),
        xlabel="Fecha",
        ylabel="Interés de audiencia",
        title="Interés en el tiempo",
    )
    ax.figure.savefig("data_returned.png")
