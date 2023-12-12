from pydantic import BaseModel

class Country(BaseModel):     #schema for get data from users
    name: str
    bio: str

