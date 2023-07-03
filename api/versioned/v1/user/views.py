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

    @router.put("/{item_id}", response_model=dict)
    async def update_item(self, item_id: int, item: dict):
        person_data = {
            "id": 1,
            "name": "str"
        }

        # BaseModel을 사용하여 생성된 객체에 대해 유효성 검사를 수행하는 메서드
        a = Cafe.parse_obj(person_data)

        # 문자열로 표현된 JSON 데이터
        json_str = '{"id": 1, "name": "John Doe"}'

        # parse_raw 메서드를 사용하여 JSON 데이터를 모델로 변환
        model_instance = Cafe.parse_raw(json_str)

        # Pydantic 모델의 인스턴스 생성
        model_instance = Cafe(name='John', id=25)

        # 스키마를 JSON 형식으로 가져오기
        schema_json = model_instance.schema_json()
        # updated_item = await self.model.objects.filter(id=item_id).update(**item.dict())
        return a

    @router.delete("/{item_id}", response_model=dict)
    async def delete_item(self, item_id: int):
        return {"message": "Item deleted"}


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



