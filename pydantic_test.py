from datetime import datetime
from decimal import Decimal
from typing import List, Union, Optional
from pydantic import BaseModel, Field, validator
import requests
#
# class MyModel(BaseModel):
#     id: int
#     name: str
#
# """
# * parse_raw
# """
#
# # 문자열로 표현된 JSON 데이터
# json_str = '{"id": 1, "name": "John Doe"}'
#
# # parse_raw 메서드를 사용하여 JSON 데이터를 모델로 변환
# model_instance = MyModel.parse_raw(json_str)
#
# # 변환된 모델 인스턴스를 사용
# print(model_instance.id)  # 출력: 1
# print(model_instance.name)  # 출력: John Doe
#
# """
# * from_orm
# """
# # 데이터베이스에서 조회한 결과를 가져옴
# db_result = {'id': 1, 'name': 'John Doe'}
#
# # from_orm 메서드를 사용하여 결과를 모델로 변환
# model_instance = MyModel.from_orm(db_result)
#
# # 변환된 모델 인스턴스를 사용
# print(model_instance.id)  # 출력: 1
# print(model_instance.name)  # 출력: John Doe
#
# """
# * parse_obj
# """
# person_data = {
#     "id": 1,
#     "name": "str"
# }
# # JSON을 User 모델 객체로 변환 및 검증
# user_obj = MyModel.parse_obj(person_data)
#
# # 생성된 User 모델 객체 확인
# print(user_obj)
# print(user_obj.id)
# print(user_obj.name)
#
# from pydantic import BaseModel, ValidationError, validator
#
#
# """
# * validate
# """
# class User(BaseModel):
#     name: str
#     age: int
#
#     @validator('age')
#     def check_age(cls, age):
#         if age < 0:
#             raise ValueError("Age must be a positive integer.")
#         return age
#
#     def validate(self):
#         if len(self.name) < 3:
#             raise ValueError("Name must be at least 3 characters long.")
#
#
# try:
#     user = User(name="John", age=25)
#     user.validate()  # 모델 유효성 검사 수행
# except ValidationError as e:
#     print(e.errors())
#
#
# from pydantic import BaseModel, parse_obj_as, validate_model
# db_result = [
#     {'id': 1, 'name': 'John Doe', 'age': 30},
#     {'id': 2, 'name': 'Jane Smith', 'age': 25},
#     {'id': 3, 'name': 'Bob Johnson', 'age': 35}
# ]
#
# # Model definition
# class User(BaseModel):
#     id: int
#     name: str
#     age: int
#
#     class Config:
#         orm_mode = True
#
# # Convert a list of dictionaries to a list of model instances
# users = parse_obj_as(list[User], db_result)
#
# # Use converted model instances
# for user in users:
#     print(user.id, user.name, user.age)
#
#
# """
# validate_model
# """
# from pydantic import BaseModel, validate_model
#
# # 모델 정의
# class User(BaseModel):
#     id: int
#     name: str
#
# # 모델 인스턴스 생성
# user = User(id=1, name="John Doe")
#
# # 모델 인스턴스 유효성 검사
# errors = validate_model(User, user)
#
# if errors:
#     for error in errors:
#         print(f"유효성 검사 오류: {error['loc']}: {error['msg']}")
# else:
#     print("모델 인스턴스 유효성 검사 통과")
#
#
#
# from pydantic import BaseModel, root_validator
#
# class MyModel(BaseModel):
#     field1: int
#     field2: str
#
#     @root_validator
#     def validate_fields(cls, values):
#         # values는 입력된 필드들의 값들을 가지는 딕셔너리입니다.
#         field1_value = values.get('field1')
#         field2_value = values.get('field2')
#
#         # 복잡한 유효성 검사 규칙을 적용합니다.
#         if field1_value is not None and field2_value is not None:
#             if field1_value > 0 and field2_value.startswith('A'):
#                 # 유효하지 않은 조건이면 ValidationError를 발생시킵니다.
#                 raise ValueError("Invalid values for field1 and field2")
#
#         # 유효성 검사를 통과한 값을 반환합니다.
#         return values
# from pydantic import BaseModel, validator, root_validator
#
#
# class Person(BaseModel):
#     name: str
#     age: int
#
#     @validator('name')
#     def validate_name(cls, value):
#         if len(value) < 2:
#             raise ValueError("이름은 최소 2글자 이상이어야 합니다.")
#         value = "john"
#         return value
#
#     @validator('age')
#     def validate_age(cls, value):
#         if value < 0 or value > 150:
#             raise ValueError("나이는 0부터 150 사이여야 합니다.")
#         else:
#             value = 19
#         return value
#
#     @root_validator
#     def root_validate_fields(cls, values):
#         name = values.get('name')
#         age = values.get('age')
#
#         if name == 'John' and age < 18:
#             raise ValueError("John은 미성년자일 수 없습니다.")
#
#         return values
#
#
# # 예시 데이터
# data = {'name': 'asdfasdf', 'age': 150}
#
# # 모델 인스턴스 생성
# person = Person(**data)
#
# # 유효성 검사 통과 확인
# print(person.name)  # 출력: John
# print(person.age)  # 출력: 20
#
#
# from pydantic import validate_arguments, BaseModel
#
# # 모델 정의
# class User(BaseModel):
#     id: int
#     name: str
#
# # validate_arguments를 이용한 함수 정의
# @validate_arguments
# def create_user(id: int, name: str):
#     return User(id=id, name=name)
#
# # User 객체 생성
# user = create_user(id=123, name='홍길동')
#
# user = create_user(id='one-two-three', name='홍길동')
# print(user.id)    # 123 출력
# print(user.name)  # '홍길동' 출력
#
#
#
# from dataclasses import dataclass as dc
# from pydantic.dataclasses import create_pydantic_model_from_dataclass
#
# @dc
# class BaseUser:
#     id: int
#     name: str
# # 그냥 dataclass는 타입힌트만을 지원하기 때문에 유효성 검사를 위해서 사용한다.
# PydanticUser = create_pydantic_model_from_dataclass(BaseUser)
# user = PydanticUser(id=123, name='홍길동')
# print(user.id)    # 123 출력
# print(user.name)  # '홍길동' 출력



#
#
# test_data = {
#     "result": {
#         "place": {
#             "totalCount": 2,
#             "list": [
#                 {
#                     "id": "cafe123",
#                     "menuInfo": "Espresso, Latte",
#                     "tel": "010-1234-5678",
#                     "thumUrls": ["http://example.com/img1.jpg", "http://example.com/img2.jpg"],
#                     "display": "My Favorite Cafe",
#                     "reviewCount": "100",
#                     "placeReviewCount": "50",
#                     "address": "123 Main St, Seoul",
#                     "roadAddress": "123 Main St, Seoul",
#                     "businessStatus": {
#                         "businessHours": "09:00 - 18:00"
#                     },
#                     "y": "37.5665",
#                     "x": "126.9780",
#                     "homePage": "http://example.com",
#                 }
#             ]
#         }
#     }
# }
#
#
# class Response(BaseModel):
#     class Config:
#         allow_population_by_field_name = True
#
#
# class APIResponse(Response):
#     def dict(self, by_alias=True, **kwargs):
#         return super().dict(by_alias=True, **kwargs)
# class BusinessStatus(BaseModel):
#     business_hours: str = Field(alias="businessHours")
#
# class PlaceData(BaseModel):
#     asdfasdfasdfddd: str = Field(alias="id", repr=False)
#     menu_info: str = Field(alias="menuInfo", repr=False)
#     tel: str
#     thumUrls: List[str]
#     title: str = Field(alias="display", repr=False)
#     review_count: str = Field(alias="reviewCount", repr=False)
#     place_review_count: str = Field(alias="placeReviewCount", repr=False)
#     address: str
#     road_address: str = Field(alias="roadAddress", repr=False)
#     business_status: BusinessStatus = Field(alias="businessStatus", repr=False)
#     latitude: str = Field(alias="y", repr=False)
#     longitude: str = Field(alias="x", repr=False)
#     home_page: str = Field(alias="homePage", repr=False)
#
# class Place(BaseModel):
#     total_count: int = Field(alias="totalCount")
#     list: List[PlaceData]
#
# class Result(BaseModel):
#     place: Place
#
# class NaverListResp(BaseModel):
#     result: Result
#
# response = NaverListResp(**test_data)
# print(response)
# print(response.dict())
#
#
# from pydantic import BaseModel, validator
#
# class MyModel(BaseModel):
#     holdings: str
#     balance: str
#
#     @validator("holdings", "balance")
#     def strip_str(cls, v: str):
#         return v.strip()
#
# data = MyModel(holdings=' 1000  ', balance=' 5000  ')
# print(data)
#
#
#
#
# """
#  repr가 선언되어있는건 무슨역할을 하게되는거야?
# """
# class User(BaseModel):
#     id: int = Field(..., description="The unique id of the user", repr=True)
#     password: str = Field(..., description="The user's password", repr=False)
#
# user = User(id=123, password='secret')
# print(repr(user))  # Output: User(id=123)
#
#
# """
# exclude가 선언된건 무슨 역할을 하게되는거야?
# """
# class User(BaseModel):
#     id: int = Field(..., description="The unique id of the user")
#     password: str = Field(..., description="The user's password", exclude=True)
#
# user = User(id=123, password='secret')
# print(user.dict())  # Output: {'id': 123}
#
#
# """
# 이 예제에서 KDTProjectRetrieve 인스턴스를 생성할 때 user_id를 설정하지 않으면 user_id는 기본적으로 None으로 설정되며exclude_unset=True로
# dict()함수를 호출하면user_id가 기본적으로 None으로 설정됩니다.
# 및 exclude_none=True, user_id 필드는 설정되지 않았거나 None으로 설정된 경우 출력 사전에서 제외됩니다.
# 이렇게 하면 설정되고 '없음' 이외의 값을 갖는 필드만 동적으로 포함할 수 있습니다.
# """
# class KDTProjectRetrieve(BaseModel):
#     course_id: str
#     project_id: str
#
#     user_id: Optional[str] = Field(None)
#
# # create instance
# kdt = KDTProjectRetrieve(course_id="some_course_id", project_id="some_project_id")
#
# # exclude unset or null fields when exporting to dict or json
# kdt_dict = kdt.dict(exclude_unset=True, exclude_none=True)

from pydantic import BaseModel, validator
class MyModel(BaseModel):
    id: int = Field(alias="xymd")

    class Config:
        allow_population_by_field_name = True

m = MyModel(**{'xymd': 1})

class MyModel(BaseModel):
    start_time: datetime

    class Config:
        json_encoders = {datetime: lambda dt: dt.timestamp()}

m = MyModel(start_time=datetime.now())

class MyModel(BaseModel):
    id: int

    class Config:
        @staticmethod
        def alias_generator(string: str) -> str:
            return string.upper()

m = MyModel(ID=1)

class MyModel(BaseModel):
    name: str

    class Config:
        anystr_strip_whitespace = True

m = MyModel(name="  John Doe  ")

class MyModel(BaseModel):
    id: int

    class Config:
        extra = "allow"

m = MyModel(id=1, extra_field="extra")
# class UserModel(BaseModel):
#     username: str
#     email: Optional[str]
#
#     @validator("email")
#     def add_email_domain(cls, v, values, **kwargs):
#         username = values.get('username')
#         if username:
#             print(f"{username}@domain.com")
#             return f"{username}@domain.com"
#         return v
#
# # Now let's create a user
# user = UserModel(username='johndoe', email='')
#
#
# class KDTProjectRetrieve(BaseModel):
#     course_id: str
#     project_id: str
#     user_id: Optional[str] = Field(None)
#
#     @validator("course_id", pre=True)
#     def ensure_email(cls, v, values, **kwargs):
#         username = values.get('username')
#         if not v and username:
#             return f"{username}@domain.com"
#         return v
#
#     @validator("project_id", pre=False)
#     def validate_email(cls, v):
#         # 이제 이메일이 입력에서 제공되었거나 `ensure_email` 검증기에서 생성된 상태입니다
#         if "@" not in v or v.startswith("@") or v.endswith("@"):
#             raise ValueError("잘못된 이메일")
#         return v
#
#
# from datetime import datetime
# from pydantic import BaseModel
#
# class CustomDatetime(datetime):
#     def __str__(self):
#         return self.strftime('%Y-%m-%d %H:%M:%S')
#
# class User(BaseModel):
#     id: int
#     name: str
#     created_at: CustomDatetime
#
#     class Config:
#         json_encoders = {
#             CustomDatetime: str
#         }
#
# user = User(id=1, name="John", created_at=CustomDatetime.now())
# print(user.json())  # {"id": 1, "name": "John", "created_at": "2023-07-20 12:14:56"}
from pydantic import BaseModel

class MyModel(BaseModel):
    id: int

    class Config:
        validate_assignment = True

m = MyModel(id=1)
# m.id = "not an integer"


def to_camel(string: str) -> str:
    return ''.join(word.capitalize() if i > 0 else word for i, word in enumerate(string.split('_')))

class MyModel(BaseModel):
    user_name: str = Field(alias='name')
    user_id: int = Field(alias='id')

    class Config:
        alias_generator = to_camel
        allow_population_by_field_name = True


data = {
    "userName": "John Doe",
    "userId": 123,
}

model = MyModel(**data)

print(model.dict(by_alias=True)) # {'name': 'John Doe', 'id': 123}
print(model.dict(by_alias=False)) # {'user_name': 'John Doe', 'user_id': 123}



