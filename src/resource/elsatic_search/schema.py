from typing import List, Optional
from pydantic import BaseModel, EmailStr

class Country(BaseModel):
    name: str
    bio: str

