from fastapi import APIRouter

router = APIRouter()

@router.get("/items")
async def get_items():
    """
    사용자 정보를 읽는 API 엔드포인트입니다.
    """
    return ["Portal gun", "Plumbus"]


@router.get("/users")
async def read_users():
    """
    사용자를 생성하는 API 엔드포인트입니다.
    """
    return ["Rick", "Morty"]
