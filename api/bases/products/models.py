from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
# 모델의 메타데이터 생성
Base = declarative_base()

class Product(Base):
    __tablename__ = 'products'

    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    price = Column(Integer)
