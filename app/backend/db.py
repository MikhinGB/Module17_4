from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase
from sqlalchemy import Column, Integer, String

# Строка подключения:
SQLALCHEMY_DATABASE_URL = 'sqlite:///taskmanager.db'

# Создание движка
engine = create_engine(SQLALCHEMY_DATABASE_URL, echo=True)

SessionLocal = sessionmaker(bind=engine)


#  Создаем базовый класс для моделей
class Base(DeclarativeBase):
    pass

class User_1(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True)
    username = Column(String)
    passsword = Column(String)

# Создаем таблицы
Base.metadata.create_all(bind=engine)
