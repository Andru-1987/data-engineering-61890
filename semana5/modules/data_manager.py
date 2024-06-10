import yfinance as yf
import pandas as pd
import logging

from io import StringIO
from sqlalchemy import create_engine

logging.basicConfig(
    filename='app.log',
    filemode='a',
    format='%(name)s - %(levelname)s - %(message)s',
    level=logging.INFO)
    
class DataConn:
    def __init__(self, config: dict,schema: str):
        self.config = config
        self.schema = schema
        self.db_engine = None


    def get_conn(self):
        username = self.config.get('REDSHIFT_USERNAME')
        password = self.config.get('REDSHIFT_PASSWORD')
        host = self.config.get('REDSHIFT_HOST')
        port = self.config.get('REDSHIFT_PORT', '5439')
        dbname = self.config.get('REDSHIFT_DBNAME')

        # Construct the connection URL
        connection_url = f"postgresql+psycopg2://{username}:{password}@{host}:{port}/{dbname}"
        self.db_engine = create_engine(connection_url)

        try:
            with self.db_engine.connect() as connection:
                result = connection.execute('SELECT 1;')
            if result:
                logging.info("Connection created")
                return
        except Exception as e:
            logging.error(f"Failed to create connection: {e}")
            raise

    def upload_data(self, data: pd.DataFrame, table: str):
        try:
            data.to_sql(
                table,
                con=self.db_engine,
                schema=self.schema,
                if_exists='append',
                index=False
            )

            logging.info(f"Data from the DataFrame has been uploaded to the {self.schema}.{table} table in Redshift.")
        except Exception as e:
            logging.error(f"Failed to upload data to {self.schema}.{table}: {e}")
            raise

    def close_conn(self):
        if self.db_engine:
            self.db_engine.dispose()
            logging.info("Connection to Redshift closed.")
        else:
            logging.warning("No active connection to close.")




class DataManager:

    def __init__(self,company: str):
        try:
            self.manager = yf.Ticker(company)
        except  Exception as e:
            logging.error(e)

    def get_data(self):
        try:
            logging.info("Creacion de data")
            return self.manager.income_stmt
        except Exception as e:
            logging.error(e)
        finally:
            logging.warn("Check the data format")

    def data_transform(self):
        try:
            data = self.get_data()
            logging.info("rename columns")
            data = data.iloc[:,:4]
            data.columns =["stock_actions","revenue","value","avg_data"]
            logging.info("change index")
            data = data.rename_axis('specific_area').reset_index()
            logging.info("add date to stage the data")
            data["date_to_stage"] = self.get_data().columns[0].date()
            logging.info("save the data")
            data = data.fillna(0)
            buffer = StringIO()
            data.info(buf=buffer)
            s = buffer.getvalue()
            logging.info(s)
            
            return data
        
        except Exception as e:
            logging.error(e)