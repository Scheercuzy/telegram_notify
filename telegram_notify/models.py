from sqlalchemy import Column, Integer, Boolean
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class Person(Base):
    __tablename__ = 'person'
    id = Column(Integer, primary_key=True)
    chat_id = Column(Integer, nullable=False)
    access = Column(Boolean, default=False)
