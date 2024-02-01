from datetime import datetime
from decimal import Decimal
from typing import List, Union, Optional
from pydantic import BaseModel, validator, Field, EmailStr, SecretStr


class MyDateClass:
    id: int


class User(BaseModel):
    name: str = Field(..., alias='username')

# Initialize with 'username' alias
user = User(username='johndoe')
print(user)
#> name='johndoe'
user_dict_alias = user.dict(by_alias=True)
print(user_dict_alias)
#> {'username': 'johndoe'}





class User(BaseModel):
    age: int = Field(description='Age of the user')
    email: EmailStr = Field(examples=['marcelo@mail.com'])
    name: str = Field(title='Username')
    password: SecretStr = Field(
        json_schema_extra={
            'title': 'Password',
            'description': 'Password of the user',
            'examples': ['123456'],
        }
    )

print(User.model_json_schema())