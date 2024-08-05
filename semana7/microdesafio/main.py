import os
from modules import store_data_into_list
from modules import DataConn
from pytrends.request import TrendReq
from dotenv import load_dotenv

load_dotenv()

def main():

    lista_paises=['CO','AR','BR','CL','BO','UY','VE','PY','EC','PE', 'US'] 
    # Colombia, Argentina, Brazil, Chile, Bolivia, Uruguay, Venezuela, Paraguay, Ecuador, Peru, USA
    keywords = ["Sea Level", "Wheater",'Temperatures','Carbon Dioxide','Global Warming']

    
    pytrends = TrendReq()
    lista_dfs = store_data_into_list(lista_paises,keywords,pytrends)


    user_credentials = {
        "REDSHIFT_USERNAME" : os.getenv('REDSHIFT_USERNAME'),
        "REDSHIFT_PASSWORD" : os.getenv('REDSHIFT_PASSWORD'),
        "REDSHIFT_HOST" : os.getenv('REDSHIFT_HOST'),
        "REDSHIFT_PORT" : os.getenv('REDSHIFT_PORT', '5439'),
        "REDSHIFT_DBNAME" : os.getenv('REDSHIFT_DBNAME')
    }

    schema:str = "andru_ocatorres_coderhouse"

    data_conn = DataConn(user_credentials, schema)


    for df,pais in zip(lista_dfs,lista_paises):
        print(pais)
        data_conn.create_insert_redshift_table(df, pais)

if __name__ == "__main__":
    main()