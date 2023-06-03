from fastapi import APIRouter

router = APIRouter()

@router.get("/", summary="User 전체 검색")
async def get_items():
    """
    사용자 정보를 읽는 API 엔드포인트입니다.
    """
    return ["Portal gun", "Plumbus"]


@router.get("/{users}", summary="User 디테일")
async def read_users():
    """
    사용자를 생성하는 API 엔드포인트입니다.
    """
    return ["Rick", "Morty"]
