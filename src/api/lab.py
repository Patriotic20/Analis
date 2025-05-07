from fastapi import APIRouter , Depends
from src.service import BaseService , get_base_service 
from src.schemas.lab import LabCreate , LabUpdate
from src.models import Lab 



lab_router = APIRouter(
    tags=["Lab"],
    prefix="/lab"
)


@lab_router.post("/create")
async def create_lab(
    lab_items: LabCreate,
    service: BaseService = Depends(get_base_service),
):
    return await service.create(model=Lab , db_obj=lab_items)


@lab_router.get("/get_by_id/{lab_id}")
async def get_by_id(
    lab_id: int,
    service: BaseService = Depends(get_base_service)
):
    return await service.get_by_id(model=Lab, item_id=lab_id)


@lab_router.get("/get_all")
async def get_all(
    service: BaseService = Depends(get_base_service)
):
    return await service.get_all(model=Lab)

@lab_router.put("/update/{lab_id}")
async def update(
    lab_id: int,
    lab_item: LabUpdate,
    service: BaseService = Depends(get_base_service)
):
    return await service.update(model=Lab , item_id=lab_id , db_obj=lab_item)

@lab_router.delete("/delete/{lab_id}")
async def delete(
    lab_id: int,
    service: BaseService = Depends(get_base_service)
):
    return await service.delete(model=Lab , item_id=lab_id)