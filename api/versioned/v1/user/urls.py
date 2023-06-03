from fastapi import APIRouter

router = APIRouter()

@router.get("/")
async def read_users():
    return 'v1'

@router.post("/create")
async def create_user():
    pass
