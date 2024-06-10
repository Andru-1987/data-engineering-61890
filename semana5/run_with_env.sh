VENV=venv
python3 -m venv $VENV && source $VENV/bin/activate
pip install yfinance pandas sqlalchemy sqlalchemy-redshift  psycopg2-binary python-dotenv

