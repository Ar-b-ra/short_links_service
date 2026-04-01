from fastapi import APIRouter
from starlette.responses import RedirectResponse

router = APIRouter(tags=["index"])


@router.get("/stats/{short_code}")
async def get_stats(short_code: str):
    return


@router.get("/{short_code}", response_class=RedirectResponse)
async def short_link_redirect(short_code: str) -> RedirectResponse:
    return RedirectResponse(short_code, status_code=301)
