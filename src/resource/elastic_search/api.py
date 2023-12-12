from fastapi import APIRouter, status
from src.resource.elastic_search.schema import Country, UpdateSchema
from src.elastic_search.elastic_search_curd import (
    post_data, 
    get_all_data, 
    delete_data, 
    get_by_name, 
    create_index,
    modified_data)

elasticsearch_route = APIRouter()


@elasticsearch_route.get("/", status_code=status.HTTP_200_OK)
def welcome_api():
    """
    testing api to check server is up or not
    """

    return "welcome"


@elasticsearch_route.post("/create-index", status_code=status.HTTP_201_CREATED)
def create_index_in_elasticsearch():
    """
    create index in elasticsearch
    """

    message , status_code = create_index()
    return{
        "message":message,
        "status_code":status_code
    }


@elasticsearch_route.post("/post-data", status_code=status.HTTP_201_CREATED)
def add_data_post(request: Country):
    """
    post data in elastic search
    """

    message , status_code = post_data(request)
    return{
        "message":message,
        "status_code":status_code
    }


@elasticsearch_route.get("/get-all-data", status_code=status.HTTP_200_OK)
def get_data():
    """
    get all data from elastic search
    """

    data , status_code, count = get_all_data()
    return{
        "data":data,
        "count": count, 
        "status_code":status_code   
    }


@elasticsearch_route.get("/get-by-name", status_code=status.HTTP_200_OK)
def get_data_by_name(city_name:str):
    """
    get data from elastic search by name
    """

    data , status_code, count = get_by_name(city_name)
    return{
        "data":data,
        "count": count, 
        "status_code":status_code   
    }


@elasticsearch_route.put("/update-data", status_code=status.HTTP_200_OK)
def update_data(request:UpdateSchema):
    """
    update data from elastic search
    """

    message , status_code = modified_data(request)
    return{
        "message":message,
        "status_code":status_code
    }


@elasticsearch_route.delete("/delete-data", status_code=status.HTTP_200_OK)
def delete_specific_data(id:str):
    """
    delete data from elastic search
    """

    message , status_code = delete_data(id)
    return{
        "message":message,
        "status_code":status_code
    }
