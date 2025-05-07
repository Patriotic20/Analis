from fastapi import APIRouter
from .auth import auth_router
from .lab import lab_router
from .analis import analis_router



api_router = APIRouter()

api_router.include_router(auth_router)
api_router.include_router(lab_router)
api_router.include_router(analis_router)