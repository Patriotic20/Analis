from datetime import timedelta, datetime, timezone
from fastapi import HTTPException, status, Depends
import jwt
from src.core.config import settings
from src.service import BaseService , get_base_service
from src.models import User  



class AuthJwt:
    def __init__(self, service: BaseService = Depends(get_base_service)):
        self.service = service

    async def _create_token(self, data: dict, expire_delta: timedelta, secret_key: str):
        to_encode = data.copy()
        expire = datetime.now(timezone.utc) + expire_delta
        to_encode.update({"exp": expire})
        return jwt.encode(to_encode, secret_key, algorithm=settings.ALGORITHM)

    async def create_access_token(self, data: dict):
        expire_delta = timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
        return await self._create_token(data=data, expire_delta=expire_delta, secret_key=settings.ACCESS_SECRET_KEY)

    async def create_refresh_token(self, data: dict):
        expire_delta = timedelta(days=settings.REFRESH_TOKEN_EXPIRE_DAYS)
        return await self._create_token(data=data, expire_delta=expire_delta, secret_key=settings.REFRESH_SECRET_KEY)
    
    async def refresh_access_token(self, token: str):
        try:
            payload = jwt.decode(
                token,
                settings.REFRESH_SECRET_KEY,
                algorithms=[settings.ALGORITHM]
            )

            username = payload.get("sub")
            if not username:
                raise HTTPException(
                    status_code=status.HTTP_401_UNAUTHORIZED,
                    detail="Invalid refresh token: missing username",
                    headers={"WWW-Authenticate": "Bearer"},
                )


            user = await self.service.get_by_field(User, "username", username)

            new_access_token = await self.create_access_token(data={"sub": user.username})
            return {
                "access_token": new_access_token,
                "token_type": "bearer"
            }

        except jwt.ExpiredSignatureError:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Refresh token has expired",
                headers={"WWW-Authenticate": "Bearer"},
            )

        except jwt.InvalidTokenError:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid refresh token",
                headers={"WWW-Authenticate": "Bearer"},
            )

    

    async def get_current_user(self, token: str):
        try:
            payload = jwt.decode(
                token,
                settings.ACCESS_SECRET_KEY,
                algorithms=[settings.ALGORITHM]
            )
            username = payload.get("sub")
            if not username:
                raise HTTPException(
                    status_code=status.HTTP_401_UNAUTHORIZED,
                    detail="Username not found in token",
                    headers={"WWW-Authenticate": "Bearer"},
                )

            user = await self.service.get_by_field(User, "username", username)
            return user

        except jwt.ExpiredSignatureError:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Token has expired",
                headers={"WWW-Authenticate": "Bearer"},
            )

        except jwt.InvalidTokenError:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid token",
                headers={"WWW-Authenticate": "Bearer"},
            )
        
