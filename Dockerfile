FROM python:3.7-alpine

ARG build_ts

RUN apk add --no-cache gcc libressl-dev musl-dev libffi-dev ; rm -rf /var/lib/apt/lists/*

COPY requirements.txt /
RUN pip install -r /requirements.txt

COPY . /app
RUN echo ${build_ts} > /app/timestamp
WORKDIR /app

RUN apk del gcc libressl-dev musl-dev libffi-dev

CMD python ./app.py