from pydantic import BaseModel
from typing import Optional

class Country(BaseModel):     #schema for get data from users
    city_name: str
    country_name: Optional[str] = None
    buyer_categories: dict

class UpdateSchema(BaseModel):   #schema for get data from users
    id: str
    name: Optional[str] = None
    bio: Optional[str] = None