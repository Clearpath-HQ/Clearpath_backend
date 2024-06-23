# pull official base image
FROM python:3.11.4-slim-buster

# set work directory
WORKDIR /usr/src/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install system dependencies
RUN apt-get update && apt-get install -y netcat

RUN apt-get update \
    && apt-get install -y \
        build-essential \
        libpq-dev \
        python3-dev \ 
        netcat \    
    && pip install psycopg2

# install dependencies
RUN pip install --upgrade pip

COPY ./app/requirements.txt /requirements.txt
RUN pip install -r /requirements.txt

COPY ./app/compose/local/django/entrypoint /entrypoint
RUN sed -i 's/\r$//g' /entrypoint
RUN chmod +x /entrypoint

COPY ./app/compose/local/django/start /start
RUN sed -i 's/\r$//g' /start
RUN chmod +x /start

# copy project
COPY . .

# run entrypoint.sh
ENTRYPOINT ["/usr/src/app/entrypoint.prod.sh"]