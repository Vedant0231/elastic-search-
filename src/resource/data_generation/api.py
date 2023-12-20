from fastapi import APIRouter, status
from src.data_generation.data_generation import generate_data

data_generation = APIRouter()


@data_generation.post("/create-data", status_code=status.HTTP_201_CREATED)
def create_data(name:str):
    """
    create index in elasticsearch
    """

    response, status_code = generate_data(name)
    return{
        "response":response,
        "status_code":status_code
    }