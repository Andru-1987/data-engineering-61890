import pandas as pd
import logging

from sqlalchemy import create_engine, Table, Column, Integer, String, MetaData, exc , inspect, text


logging.basicConfig(
    filename='app.log',
    filemode='a',
    format='%(asctime)s ::DataConnectionModule-> %(name)s - %(levelname)s - %(message)s',
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

    def create_insert_redshift_table(self, df, table_name:str):
        if self.db_engine is None:
            logging.warn("Execute it before")
            self.get_conn()

        table_name = f"table_country_{table_name.lower()}"
        metadata = MetaData(schema=self.schema)

        columns = []
        
        DTYPE_MAPPING = {
            "int64": Integer,
            "float64": String,
            "object": String,
            "datetime64[ns]": String
        }

        # CREACION DE LA TABLA DE MANERA DINAMICA

        for col_name, col_type in zip(df.columns, df.dtypes):
            
            sql_type = DTYPE_MAPPING.get(str(col_type))

            if sql_type:
                columns.append(Column(col_name,sql_type))
            else:
                raise TypeError(f"Unsupported dtype: {col_type}")
        
        # Create the table in Redshift
        
        inspector = inspect(self.db_engine)
        table_exists = inspector.has_table(table_name, schema=self.schema)

        if table_exists:
            try:
                # Use raw SQL to drop the table to ensure it's dropped from the correct schema
                with self.db_engine.connect() as connection:
                    connection.execute(f'DROP TABLE IF EXISTS "{self.schema}"."{table_name}"')
                print(f"Table {table_name} dropped successfully.")
            except exc.SQLAlchemyError as e:
                print(f"Error occurred while dropping the table: {e}")
        
        Table(table_name, metadata, *columns)

        df.to_sql(table_name, self.db_engine, index=False, if_exists='append', schema=self.schema)
        print(table_name, 'insert data .............. OK')

    
    def check_table_exists(self, table_name:str) -> bool:
        with self.db_engine.connect() as connection:
            cursor = connection.cursor
            query_checker = f"""
                SELECT 1 FROM information_schema.tables 
                WHERE  table_schema = 'andru_ocatorres_coderhouse'
                AND    table_name   = '{table_name}';              
            """
            cursor.execute(query_checker)
            
            if not cursor.fetchone():
                logging.error(f"No {table_name} has been created")
                raise ValueError(f"No {table_name} has been created")

            logging.info(f"{table_name} exists")

    def upload_data(self, data: pd.DataFrame, table: str):
        if self.db_engine is None:
            logging.warn("Execute it before")
            self.get_conn()

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
            logging.error(f"Failed to upload data to {self.schema}.{table}:\n{e}")
            raise

    def close_conn(self):
        if self.db_engine:
            self.db_engine.dispose()
            logging.info("Connection to Redshift closed.")
        else:
            logging.warning("No active connection to close.")


