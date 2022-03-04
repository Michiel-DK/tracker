# Pull base image
FROM python:3.8.12-buster

# Set environment varibles
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1


# Install dependencies
COPY fast /fast
COPY tracker /tracker
COPY requirements.txt /requirements.txt

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Install ssh client and git
RUN apt update && apt install openssh-client git

# Download public key for github.com
RUN mkdir -p -m 0700 ~/.ssh && ssh-keyscan github.com >> ~/.ssh/known_hosts

# Clone private repository
RUN --mount=type=ssh git clone git+git@github.com:Michiel-DK/tracker.git@88b53454c9b70d364b4d7103f307b4ca88418893#egg=tracker

EXPOSE 8000

CMD ["python", "fast/api.py"]