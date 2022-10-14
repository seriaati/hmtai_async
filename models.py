from typing import List
from pydantic import BaseModel, validator

class SFWEndpoint(BaseModel):
    name: str
    
class NSFWEndpoint(BaseModel):
    name: str

class Endpoint(BaseModel):
    sfw: List[SFWEndpoint]
    nsfw: List[NSFWEndpoint]
    
    @validator("sfw", pre=True)
    def validate_sfw(cls, v):
        return [SFWEndpoint(name=name) for name in v['sfw']]
    
    @validator("nsfw", pre=True)
    def validate_nsfw(cls, v):
        return [NSFWEndpoint(name=name) for name in v['nsfw']]
