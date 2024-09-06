
# Project Title

Football games statistics. 

## Description

This project is a data pipeline that uses API to extract information, stores the data locally, loads it into a PostgreSQL database, and exports a summary into a CSV file..

## Architecture diagram

![architecture_diagram](https://github.com/gwakaf/football_games/blob/main/architecture_diagram.png?raw=true)


## Build with

* Docker Compose
* Python
* PostgreSQL
* https://www.football-data.org/ API

## Getting Started
### Project Setup
* Use docker-copose.yaml file to start two containers:
  *   Postres DB
  *   Python app 
* Python code executes
  *   API handler requests data from football API and store it to the local json files
  *   Database class creates connection to Postgres DB using psycopg2 library
  *   It creates three tables
  *   Reads data from json files and inserts it to the tables
  *   csv_exporter module reads data from json files and write summary to local .csv file 




