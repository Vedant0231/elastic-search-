from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.resource.elastic_search.api import elasticsearch_route
from src.resource.data_generation.api import data_generation

app = FastAPI()
origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(elasticsearch_route)
app.include_router(data_generation)
