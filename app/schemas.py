
from pydantic import BaseModel, HttpUrl, Field
from pydantic import ConfigDict
from typing import Optional
from datetime import datetime

class URLCreate(BaseModel):
    url: HttpUrl = Field(..., example="https://www.example.com")
    custom_slug: Optional[str] = Field(None, example="my-slug")

class URLResponse(BaseModel):
    slug: str = Field(..., example="abc123")
    original_url: HttpUrl = Field(..., example="https://www.example.com")

class URLInfo(URLResponse):
    model_config = ConfigDict(from_attributes=True, json_encoders={
        datetime: lambda v: v.strftime("%d %b %Y %H:%M:%S")
    })
    
    clicks: int = Field(..., example=42)
    created_at: datetime = Field(..., example="01 Jan 2024 12:00:00")
    expires_at: datetime = Field(..., example="01 Jan 2025 12:00:00")