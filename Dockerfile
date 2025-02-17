FROM python:3.12

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY ./src /app

CMD ["python", "/app/fast_server.py"]

