
from pydantic import BaseModel, HttpUrl

class URL(BaseModel):
    pass

class URLCreate(URL):
    url: HttpUrl

class URLResponse(URL):
    slug: str
    original_url: HttpUrl

    class Config:
        from_attributes = True
