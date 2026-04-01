from urllib.parse import urlparse

from fastapi import APIRouter

router = APIRouter(tags=["index"])


@router.post("shorten")
async def create_short_link(link: str) -> str:
    parsed_link = urlparse(link)

    return str(parsed_link.hostname)
