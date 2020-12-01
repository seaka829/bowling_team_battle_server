FROM python:3.7

RUN mkdir /api
RUN mkdir /api/src
RUN mkdir /api/module
WORKDIR /api

ADD module/ ./module

ENV FLASK_APP ./src/app.py
ENV FLASK_ENV development

RUN pip install --upgrade pip --no-cache-dir
RUN pip install -r ./module/requirements.txt --no-cache-dir

EXPOSE 5000
