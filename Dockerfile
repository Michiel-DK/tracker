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

RUN pip install --upgrade pip
RUN pip install -r requirements.txt
RUN pip install .

EXPOSE 8000

CMD uvicorn fast.api:app --host 0.0.0.0