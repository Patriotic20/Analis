from fastapi import APIRouter , Depends




order_router = APIRouter()



@order_router.post("/create")
async def create():
    pass


@order_router.get("/get_by_id/{order_id}")
async def get_by_id():
    pass

@order_router.get("/get_all")
async def get_all():
    pass

@order_router.put("/")
async def update():
    pass

@order_router.delete()
async def delete():
    pass