FROM python:3.9.6-slim-buster
ENV PYTHONUNBUFFERED 1

RUN mkdir /src
WORKDIR /src

COPY ./back-end /src

RUN apt-get update \
    && apt-get -y install libpq-dev gcc 

RUN pip install --upgrade pip && \
    pip install psycopg2-binary && \
    pip install -r requirements.txt
