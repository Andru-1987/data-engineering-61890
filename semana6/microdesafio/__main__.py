import pandas as pd
import os
from pytrends.request import TrendReq

def store_data_from_pytrends(data: pd.DataFrame):
    if data is None:
        raise ValueError("No data is saved")
        
    data.to_parquet('df.parquet', engine='fastparquet') 

def read_data_if_no_data(path:str) -> pd.DataFrame:
    return  pd.read_parquet("df.parquet")

def get_data_from_pytrends(keywords:list[str]):
    pytrends = TrendReq()
    try:
        pytrends.build_payload(keywords, cat=0, timeframe='today 5-y', geo='', gprop='')
        data = pytrends.interest_over_time()[keywords]
        store_data_from_pytrends(data)
        return data
    except Exception  as e:
        print({"error":e})
        if not os.path.exists("df.parquet"):
            raise ValueError("No data storaged")
        
        read_data_if_no_data("df.parquet")
        

def graph_data(data):
    if data is None:
        raise ValueError("Error with no data retrieved")
    ax = data.plot(
        kind='line',
        figsize=(12,6),
        xlabel='Fecha',
        ylabel='Interés de audiencia',
        title='Interés en el tiempo')
    ax.figure.savefig("data_returned.png")


keywords = ["Fin del mundo", "Calentamiento global", "Terremoto",'Tsunami']

data = get_data_from_pytrends(keywords)
print(data.describe)
print(data.head())

graph_data(data)

print("process success")
