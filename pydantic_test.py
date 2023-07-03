from pydantic import BaseModel

class MyModel(BaseModel):
    id: int
    name: str

"""
* parse_raw
"""

# 문자열로 표현된 JSON 데이터
json_str = '{"id": 1, "name": "John Doe"}'

# parse_raw 메서드를 사용하여 JSON 데이터를 모델로 변환
model_instance = MyModel.parse_raw(json_str)

# 변환된 모델 인스턴스를 사용
print(model_instance.id)  # 출력: 1
print(model_instance.name)  # 출력: John Doe

"""
* from_orm
"""
# 데이터베이스에서 조회한 결과를 가져옴
db_result = {'id': 1, 'name': 'John Doe'}

# from_orm 메서드를 사용하여 결과를 모델로 변환
model_instance = MyModel.from_orm(db_result)

# 변환된 모델 인스턴스를 사용
print(model_instance.id)  # 출력: 1
print(model_instance.name)  # 출력: John Doe

"""
* parse_obj
"""
person_data = {
    "id": 1,
    "name": "str"
}
# JSON을 User 모델 객체로 변환 및 검증
user_obj = MyModel.parse_obj(person_data)

# 생성된 User 모델 객체 확인
print(user_obj)
print(user_obj.id)
print(user_obj.name)

from pydantic import BaseModel, ValidationError, validator


"""
* validate
"""
class User(BaseModel):
    name: str
    age: int

    @validator('age')
    def check_age(cls, age):
        if age < 0:
            raise ValueError("Age must be a positive integer.")
        return age

    def validate(self):
        if len(self.name) < 3:
            raise ValueError("Name must be at least 3 characters long.")


try:
    user = User(name="John", age=25)
    user.validate()  # 모델 유효성 검사 수행
except ValidationError as e:
    print(e.errors())


from pydantic import BaseModel, parse_obj_as, validate_model
db_result = [
    {'id': 1, 'name': 'John Doe', 'age': 30},
    {'id': 2, 'name': 'Jane Smith', 'age': 25},
    {'id': 3, 'name': 'Bob Johnson', 'age': 35}
]

# Model definition
class User(BaseModel):
    id: int
    name: str
    age: int

    class Config:
        orm_mode = True

# Convert a list of dictionaries to a list of model instances
users = parse_obj_as(list[User], db_result)

# Use converted model instances
for user in users:
    print(user.id, user.name, user.age)


"""
validate_model
"""
from pydantic import BaseModel, validate_model

# 모델 정의
class User(BaseModel):
    id: int
    name: str

# 모델 인스턴스 생성
user = User(id=1, name="John Doe")

# 모델 인스턴스 유효성 검사
errors = validate_model(User, user)

if errors:
    for error in errors:
        print(f"유효성 검사 오류: {error['loc']}: {error['msg']}")
else:
    print("모델 인스턴스 유효성 검사 통과")