from sqlalchemy import Column , String , Integer
from src.core.base import Base

class Lab(Base):
    __tablename__ = "labs"

    id = Column(Integer , primary_key=True)
    name = Column(String , nullable=False)
    description = Column(String , nullable=False)


