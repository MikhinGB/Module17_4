import app.backend.db
from app.backend.db import Base
from sqlalchemy import Column, ForeignKey, Integer, String, Boolean, Float
from sqlalchemy.orm import relationship
from app.models import *


# Создаём модель Task, объекты которой будут храниться в БД
class Task(Base):
    __tablename__ = 'tasks'
    __table_args__ = {'keep_existing': True}
    id = Column(Integer, primary_key=True, index=True)
    priority = Column(Integer, default=0)
    user_id = Column(Integer, ForeignKey('users.id', ondelete='CASCADE'))
    content = Column(String)
    title = Column(String)
    completed = Column(Boolean, default=False)
    slug = Column(String, unique=True, index=True)

    user = relationship('User', back_populates='tasks')

from sqlalchemy.schema import CreateTable

Base.metadata.create_all(bind=app.backend.db.engine)

print(CreateTable(Task.__table__))