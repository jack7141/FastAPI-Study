from fastapi import APIRouter, Depends
from pydantic import BaseModel
from typing import List

router = APIRouter()


class Cafe(BaseModel):
    id: int
    name: str

class UserViewSet(APIRouter):
    model = Cafe

    @router.get("/", response_model=List[model])
    async def get_items(self):

        items = await self.model.objects.all()
        return ["Portal gun", "Plumbus"]

    @router.post("/", response_model=model)
    async def create_item(self, item: model):
        new_item = await self.model.objects.create(**item.dict())
        return ["Rick", "Morty"]

    @router.get("/{item_id}", response_model=model)
    async def get_item(self, item_id: int):
        item = await self.model.objects.get(id=item_id)
        return ["Rick", "Morty"]

    @router.put("/{item_id}", response_model=model)
    async def update_item(self, item_id: int, item: model):
        updated_item = await self.model.objects.filter(id=item_id).update(**item.dict())
        return ["Rick", "Morty"]

    @router.delete("/{item_id}")
    async def delete_item(self, item_id: int):
        await self.model.objects.filter(id=item_id).delete()
        return ["Rick", "Morty"]


class ItemsView:
    @staticmethod
    async def get_items():
        """
        사용자 정보를 읽는 API 엔드포인트입니다.
        """
        return ["Portal gun", "Plumbus"]

    @staticmethod
    async def read_users(users: str):
        """
        사용자를 생성하는 API 엔드포인트입니다.
        """
        return ["Rick", "Morty"]



