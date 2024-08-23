# Use the official Python image as a base
FROM python:latest

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container
COPY . /app
COPY . /data

# Install any necessary dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
RUN apt-get update \
    && apt-get -y install libpq-dev gcc \
    && pip install psycopg2


