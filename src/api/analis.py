from fastapi import APIRouter , Depends
from src.service import BaseService , get_base_service
from src.schemas.analis import AnalisBase , AnalisUpdate
from src.models.analis import Analis


analis_router = APIRouter(
    tags=["Analis"],
    prefix="/analis"
)


@analis_router.post("/create")
async def create(
    analis_item: AnalisBase,
    service: BaseService = Depends(get_base_service)
):
    return await service.create(model=Analis , db_obj=analis_item)

@analis_router.get("/get_by_id/{analis_id}")
async def get_by_id(
    analis_id: int,
    service : BaseService = Depends(get_base_service)
):
    return await service.get_by_id(model=Analis , item_id=analis_id)

@analis_router.get("/get_all")
async def get_all(
    service: BaseService = Depends(get_base_service)
):
    return await service.get_all(model=Analis)

@analis_router.put("/update/{analis_id}")
async def update(
    analis_id: int,
    analis_item: AnalisUpdate ,
    service : BaseService = Depends(get_base_service)
):
    return await service.update(model=Analis, item_id=analis_id , db_obj=analis_item)


@analis_router.delete("/delete/{analis_id}")
async def delete(
    analis_id: int,
    service: BaseService = Depends(get_base_service)
):
    return await service.delete(model=Analis , item_id=analis_id)