from fastapi import APIRouter

router = APIRouter(prefix="/cookie", tags=["cookie"])


@router.get("/")
async def give_cookie_from_server():
    pass
