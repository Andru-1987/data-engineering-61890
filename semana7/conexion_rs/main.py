
# creacion de tabla en rs
# DROP TABLE IF EXISTS andru_ocatorres_coderhouse.ingesta_python; 
# CREATE TABLE andru_ocatorres_coderhouse.ingesta_python(
#     id INT ,
#     nombre VARCHAR(100),
#     email VARCHAR(100)
# );

import pandas as pd
import sqlalchemy as sa
from dotenv import load_dotenv
import os



def main():
    load_dotenv()

    users: list[str] = [{
    "id": 1,
    "nombre": "Garfield",
    "email": "ggrellis0@loc.gov"
    }, {
    "id": 2,
    "nombre": "Felicia",
    "email": "fpellatt1@wordpress.com"
    }, {
    "id": 3,
    "nombre": "Dante",
    "email": "dmcnellis2@lulu.com"
    }, {
    "id": 4,
    "nombre": "Genni",
    "email": "gsavil3@constantcontact.com"
    }, {
    "id": 5,
    "nombre": "Dennison",
    "email": "daspey4@omniture.com"
    }]

    print(users)

    data = pd.DataFrame(users)

    print(data)

    username = os.getenv('REDSHIFT_USERNAME')
    password = os.getenv('REDSHIFT_PASSWORD')
    host = os.getenv('REDSHIFT_HOST')
    port = os.getenv('REDSHIFT_PORT', 5439)
    dbname = os.getenv('REDSHIFT_DBNAME')
    schema:str = "andru_ocatorres_coderhouse"

    connection_url = f"postgresql+psycopg2://{username}:{password}@{host}:{port}/{dbname}"
    print(connection_url)
    db_engine = sa.create_engine(connection_url)

    try: 

        data.reset_index(drop=True)
        data.to_sql(
            "ingesta_python",
            db_engine,
            index=False,
            if_exists='append',
            schema=schema
        )

    except sa.exc.SQLAlchemyError as e:
        print(f"Error occurred while dropping the table: {e}")
    except Exception as e:
        print(e)

if __name__ == "__main__":
    main()






