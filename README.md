# README #

This README would normally document whatever steps are necessary to get your application up and running.
## Postman collection is also attack with this repo, you can simply import postman collection json file ##


### What is this repository for? ###

In this project we setup elastic search with the help of docker compose file and create curd operation

### Things used in this project ###

  * Docker compose
  * Elastic search
  * Python
  * FastAPI
  * Postman

## What is Docker compose? ##

Docker Compose is a tool for defining and running multi-container Docker applications. It allows you to define a multi-container Docker application using a YAML file to configure the application's services, networks, and volumes. With Docker Compose, you can start and run your entire application stack with a single command.     


## What is Elastic search ? ##

Elasticsearch is a distributed, open-source search and analytics engine built on top of Apache Lucene. It is designed for horizontal scalability, meaning that it can easily scale out to handle large amounts of data and queries across multiple nodes or servers. Elasticsearch is part of the Elastic Stack, which also includes Logstash for log data collection and Kibana for data visualization.


## What is FastAPI? ##

FastAPI is a modern, fast (high-performance), web framework for building APIs with Python 3.7+ based on standard Python type hints. It was created by Sebastián Ramírez and is designed to be easy to use, fast to develop with, and to produce fast, efficient code.


## What is Postman? ##

Postman is a popular collaboration platform for API development. It provides a user-friendly interface that allows developers to create, test, and manage APIs more efficiently.


### How do I get set up? ###

  * Take pull
  * Create venv file (Command to create venv file: python3 -m venv your_env, to start write command: source/your_env/bin/activate)
  * docker-compose up
  * pip install -r requirements.txt
  * python3 main.py
  * first hit welcome api to check server is up or not
  * then hit create index api to create index (you need to give index name in .env file, example is already there in .env_example file)
  * then you can create data in elastic search and get data or delete data or search data

### What functionality did this project provide ###

  * Create elastic search and kibana container from there docker image
  * Create index with proper mapping(mapping is already created, you can update mapping from mapping.py file)
  * Crud operation on elastic search