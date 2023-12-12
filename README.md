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