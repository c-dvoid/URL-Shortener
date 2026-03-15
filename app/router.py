
from fastapi import APIRouter, HTTPException
from fastapi.responses import RedirectResponse

from .schemas import URLCreate, URLResponse
from .service import generate_short_url, get_url_by_slug

router = APIRouter()

@router.post("/short_url", response_model=URLResponse)
async def create_short_url(url_data: URLCreate):
    new_slug = await generate_short_url(str(url_data.url))
    return {"slug": new_slug, "original_url": url_data.url}

@router.get("/{slug}")
async def redirect(slug: str):
    link = await get_url_by_slug(slug)
    if link is None:
        raise HTTPException(status_code=404, detail="Slug not found")
    return RedirectResponse(url=link.original_url)