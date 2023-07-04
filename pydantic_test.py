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



from pydantic import BaseModel, root_validator

class MyModel(BaseModel):
    field1: int
    field2: str

    @root_validator
    def validate_fields(cls, values):
        # values는 입력된 필드들의 값들을 가지는 딕셔너리입니다.
        field1_value = values.get('field1')
        field2_value = values.get('field2')

        # 복잡한 유효성 검사 규칙을 적용합니다.
        if field1_value is not None and field2_value is not None:
            if field1_value > 0 and field2_value.startswith('A'):
                # 유효하지 않은 조건이면 ValidationError를 발생시킵니다.
                raise ValueError("Invalid values for field1 and field2")

        # 유효성 검사를 통과한 값을 반환합니다.
        return values
from pydantic import BaseModel, validator, root_validator


class Person(BaseModel):
    name: str
    age: int

    @validator('name')
    def validate_name(cls, value):
        if len(value) < 2:
            raise ValueError("이름은 최소 2글자 이상이어야 합니다.")
        value = "john"
        return value

    @validator('age')
    def validate_age(cls, value):
        if value < 0 or value > 150:
            raise ValueError("나이는 0부터 150 사이여야 합니다.")
        else:
            value = 19
        return value

    @root_validator
    def root_validate_fields(cls, values):
        name = values.get('name')
        age = values.get('age')

        if name == 'John' and age < 18:
            raise ValueError("John은 미성년자일 수 없습니다.")

        return values


# 예시 데이터
data = {'name': 'asdfasdf', 'age': 150}

# 모델 인스턴스 생성
person = Person(**data)

# 유효성 검사 통과 확인
print(person.name)  # 출력: John
print(person.age)  # 출력: 20


from pydantic import validate_arguments, BaseModel

모델 정의
class User(BaseModel):
    id: int
    name: str

# validate_arguments를 이용한 함수 정의
@validate_arguments
def create_user(id: int, name: str):
    return User(id=id, name=name)

User 객체 생성
user = create_user(id=123, name='홍길동')

user = create_user(id='one-two-three', name='홍길동')
print(user.id)    # 123 출력
print(user.name)  # '홍길동' 출력



from dataclasses import dataclass as dc
from pydantic.dataclasses import create_pydantic_model_from_dataclass

@dc
class BaseUser:
    id: int
    name: str
# 그냥 dataclass는 타입힌트만을 지원하기 때문에 유효성 검사를 위해서 사용한다.
PydanticUser = create_pydantic_model_from_dataclass(BaseUser)
user = PydanticUser(id=123, name='홍길동')
print(user.id)    # 123 출력
print(user.name)  # '홍길동' 출력
