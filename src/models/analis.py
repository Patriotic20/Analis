from sqlalchemy import Column , String , Integer , Float 
from src.core.base import Base

class Analis(Base):
    __tablename__ = "analyzes"

    id = Column(Integer , primary_key=True)
    name = Column(Integer , nullable=False)
    price = Column(Float , nullable=False)
    description = Column(String , nullable=False)





