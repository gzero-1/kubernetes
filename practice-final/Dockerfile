# syntax=docker/dockerfile:1

FROM python:3.11.0

WORKDIR /app

COPY requirements.txt requirements.txt
RUN python -m pip install -r requirements.txt

COPY . .

CMD [ "python", "app.py"]