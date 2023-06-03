from fastapi import APIRouter
import os
from pathlib import Path
from . import urls

def get_current_folder_name() -> str:
    return Path(os.path.dirname(os.path.abspath(__file__))).parts[-1]

folder_name = get_current_folder_name()

router = APIRouter(tags=[folder_name],
                   responses={404: {"description": "Not found"}})

router.include_router(urls.router)

__all__ = ["router"]
