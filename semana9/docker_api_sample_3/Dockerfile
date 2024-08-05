FROM python:3.8

WORKDIR /code

COPY requirements.txt .

RUN mkdir -p foo_folder
RUN pip install -r requirements.txt

COPY src/ .

CMD [ "python", "./main.py" ]