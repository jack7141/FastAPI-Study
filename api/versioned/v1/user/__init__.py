from fastapi import APIRouter
import os
from pathlib import Path
from .views import UserViewSet, ItemsView

# 얘가 사실상 URL

def get_current_folder_name() -> str:
    return Path(os.path.dirname(os.path.abspath(__file__))).parts[-1]

folder_name = get_current_folder_name()

router = APIRouter(tags=[folder_name],
                   responses={404: {"description": "Not found"}})

router.add_api_route("/", endpoint=ItemsView.get_items, methods=["GET"], summary="User 전체 검색")
router.add_api_route("/{users}", endpoint=ItemsView.read_users, methods=["POST"], summary="User 디테일")
# router.add_api_route("/{item_id}", endpoint=UserViewSet.update_item, methods=["PUT"], summary="User 전체 검색")
# router.add_api_route("/{users}", endpoint=UserViewSet.get_item, methods=["GET"], summary="User 디테일")

__all__ = ["router"]
