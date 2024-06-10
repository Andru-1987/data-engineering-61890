import requests
from io import StringIO
import pandas as pd
import logging

logging.basicConfig(
    filename='app.log',
    filemode='a',
    format='%(asctime)s ::GetDataModule-> %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO)

class DataRetriever:
    def __init__(self, user:str = "Andru-1987", repos:str = "repos" ) -> None:
        self.endpoint:str = f"https://api.github.com/users/{user}/{repos}"
    
    def get_data(self):
        response_json = requests.get(self.endpoint).json()
        data_by_list_api:pd.DataFrame = pd.DataFrame(response_json)
        # columnas necesarias para la ingestan en las tablas
        cols:list[str] = ["id","name","full_name","private", "html_url","size"]
        logging.info(f"{cols} -> to be inserted")
        data = data_by_list_api[cols]
        
        try:
            data = pd.DataFrame(data)
            data = data.fillna(0)
            buffer = StringIO()
            data.info(buf=buffer)
            s = buffer.getvalue()
            logging.info(s)
            logging.info(f"Data created")
            return data
        
        except Exception as e:
            logging.error(f"Not able to import the data from the api\n{e}")
            raise
