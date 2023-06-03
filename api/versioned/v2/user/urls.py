from fastapi import APIRouter

router = APIRouter()

@router.get("/")
async def read_users():
    return 'v2'

@router.post("/asdf")
async def create_user():
    pass
