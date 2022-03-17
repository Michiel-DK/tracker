# Pull base image
FROM python:3.8.12-buster

# Set environment varibles
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1


# Install dependencies
COPY fast /fast
COPY tracker /tracker
COPY requirements.txt /requirements.txt
COPY setup.py /setup.py
COPY scripts /scripts

#upgrade libpq and install build tools, then build psycopg2-binary from source
RUN apt update -y && apt install -y build-essential libpq-dev
RUN pip install psycopg2-binary --no-binary psycopg2-binary

RUN pip install --upgrade pip
RUN pip install -r requirements.txt
RUN pip install .

EXPOSE 8000

CMD uvicorn fast.api:app --host 0.0.0.0