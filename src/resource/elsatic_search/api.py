import logging
from fastapi import APIRouter, status
from src.resource.elsatic_search.schema import Country
from src.elastic_search.elastic_search_curd import post_data, get_all_data, delete_data, get_by_name

elasticsearch_route = APIRouter()

@elasticsearch_route.get("/", status_code=status.HTTP_200_OK)
def welcome_api():
    return "welcome"

@elasticsearch_route.post("/post-data", status_code=status.HTTP_201_CREATED)
def add_data_post(request: Country):
    message , status_code = post_data(request)

    return{
        "message":message,
        "status_code":status_code
    }


@elasticsearch_route.get("/get-all-data", status_code=status.HTTP_200_OK)
def get_data():
    data , status_code, count = get_all_data()

    return{
        "data":data,
        "count": count, 
        "status_code":status_code   
    }


@elasticsearch_route.get("/get-by-name", status_code=status.HTTP_200_OK)
def get_data_by_name(city_name:str):
    data , status_code, count = get_by_name(city_name)

    return{
        "data":data,
        "count": count, 
        "status_code":status_code   
    }


@elasticsearch_route.delete("/delete-data", status_code=status.HTTP_200_OK)
def delete_specific_data(id:str):
    message , status_code = delete_data(id)

    return{
        "message":message,
        "status_code":status_code
    }
