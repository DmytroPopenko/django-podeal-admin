FROM python:3.12-alpine


ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1


COPY requirements.txt /app/requirements.txt
COPY ./podeal_page /app
WORKDIR /app

RUN pip install --upgrade pip && pip install -r requirements.txt