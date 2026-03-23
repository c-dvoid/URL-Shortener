
from fastapi import APIRouter, HTTPException
from fastapi.responses import RedirectResponse

from .schemas import URLCreate, URLResponse, URLInfo
from .service import (
    generate_url,
    get_url_by_slug,
    info_by_slug
)

router = APIRouter()

@router.post("/short_url", response_model=URLResponse)
async def create_short_url(url_data: URLCreate):
    try:
        slug = await generate_url(
            str(url_data.url),
            url_data.custom_slug
        )
    except ValueError:
        raise HTTPException(status_code=409, detail="Custom slug already exists")
    return {"slug": slug, "original_url": str(url_data.url)}


@router.get("/info/{slug}", response_model=URLInfo)
async def get_url_info(slug: str):
    link = await info_by_slug(slug)
    if link is None:
        raise HTTPException(status_code=404, detail="Slug not found")
    return link


@router.get("/{slug}")
async def redirect(slug: str):
    link = await get_url_by_slug(slug)
    if link is None:
        raise HTTPException(status_code=404, detail="Slug not found")
    return RedirectResponse(url=link.original_url)

