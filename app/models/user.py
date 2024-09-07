import app.backend.db
from app.backend.db import Base
from sqlalchemy import Column, ForeignKey, Integer, String, Boolean, Float
from sqlalchemy.orm import relationship
from app.models import *



# Создаём модель User, объекты которой будут храниться в БД
class User(Base):
    __tablename__ = 'users'
    __table_args__ = {'extend_existing': True}
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String)
    firstname = Column(String)
    secondname = Column(String)
    age = Column(Integer)
    slug = Column(String, unique=True, index=True)

    tasks = relationship("Task", back_populates="user")

from sqlalchemy.schema import CreateTable

Base.metadata.create_all(bind=app.backend.db.engine)

print(CreateTable(User.__table__))


