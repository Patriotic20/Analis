from src.schemas.user import UserLogin
from fastapi import Depends , HTTPException , status
from passlib.context import CryptContext
from src.schemas.user import *
from fastapi.security import OAuth2PasswordBearer 
from src.service import BaseService , get_base_service
from src.models.user import User
from src.core.config import settings
from src.service.jwt_auth import AuthJwt
from typing import List
import jwt



pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth/login")

def get_jwt_service(service: BaseService = Depends(get_base_service)):
    return AuthJwt(service=service)

def get_auth_service(
    base_service: BaseService = Depends(get_base_service),
    jwt_service: AuthJwt = Depends(get_jwt_service)
):
    return Auth(service=base_service, jwt_service=jwt_service)



class Auth:
    def __init__(
            self, 
            service: BaseService = Depends(),
            jwt_service: AuthJwt = Depends()
            ):
        self.service = service
        self.jwt_service = jwt_service

    async def login(self , credential: UserLogin):
        username = credential.username.strip()
        password = credential.password.strip()

        user = await self.service.get_by_field(User , "username" , username)

        if not pwd_context.verify(password, user.password):
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Incorrect username or password",
                headers={"WWW-Authenticate": "Bearer"},
            )
        
        access_token = await self.jwt_service.create_access_token(data={"sub": user.username})
        refresh_token = await self.jwt_service.create_refresh_token(data={"sub": user.username})

        return {
            "access_token": access_token,
            "refresh_token": refresh_token,
            "token_type": "bearer",
        }

    async def register(self , db_obj: UserCreate):
        return await self.service.create(User , db_obj)


    async def refresh(self , token: str):
        return await self.jwt_service.refresh_access_token(token=token)
    