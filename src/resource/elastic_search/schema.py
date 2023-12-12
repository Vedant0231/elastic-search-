from pydantic import BaseModel
from typing import Optional

class Country(BaseModel):     #schema for get data from users
    name: str
    bio: str

class UpdateSchema(BaseModel):   #schema for get data from users
    id: str
    name: Optional[str] = None
    bio: Optional[str] = None