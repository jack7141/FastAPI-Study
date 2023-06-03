from fastapi import APIRouter
from . import urls

router = APIRouter()

router.include_router(urls.router)

__all__ = ["router"]
