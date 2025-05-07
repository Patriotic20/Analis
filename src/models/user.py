from sqlalchemy import Column , String , Integer  , Enum as SqlEnum
from src.core.base import Base
from sqlalchemy.orm import relationship
from datetime import datetime , timezone
from enum import Enum

class UserRole(str , Enum):
    admin = "admin"
    user = "user"

class User(Base):
    __tablename__ = "users"

    id = Column(Integer , primary_key=True)
    username = Column(String , nullable=False)
    password = Column(String , nullable=False)
    role = Column(SqlEnum(UserRole) , default=UserRole.user)
    last_login = Column(String , nullable=True)
    create_at = Column(String , default=datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S"))





