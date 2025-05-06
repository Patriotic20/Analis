from fastapi import APIRouter , Depends
from src.schemas.user import  UserCreate
from src.service.auth import get_auth_service , Auth , oauth2_scheme
from fastapi.security import OAuth2PasswordRequestForm



auth_router = APIRouter(
    tags=["Auth"],
    prefix="/auth"
)




@auth_router.post("/register")
async def register(
    credentials: UserCreate,
    service: Auth = Depends(get_auth_service)
):
    return await service.register(db_obj=credentials)



@auth_router.post("/login")
async def login(
    form_data: OAuth2PasswordRequestForm = Depends(),
    service: Auth = Depends(get_auth_service)
):
    return await service.login(credential=form_data)

@auth_router.post("/refresh")
async def refesh(
    token: str,
    service: Auth = Depends(get_auth_service)
):
    return await service.refresh(token=token)