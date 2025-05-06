from pydantic import BaseModel , field_validator
from passlib.context import CryptContext
from src.models.user import UserRole
from datetime import datetime


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


class UserLogin(BaseModel):
    username : str
    password : str




class UserBase(BaseModel):
    username: str


class UserCreate(UserBase):
    password: str

    @field_validator("password" , mode="before")
    @classmethod
    def hash_password(cls , password):
        return pwd_context.hash(password)
    



class UserResponse(UserBase):
    id: int
    role: str
    last_login: datetime
    create_at: datetime | None = None
