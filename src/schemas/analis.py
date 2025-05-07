from pydantic import BaseModel

class AnalisBase(BaseModel):
    name: str
    price : float
    description : str

class AnalisCreate(AnalisBase):
    pass


class AnalisUpdate(BaseModel):
    name: str | None = None
    price : float | None = None
    description : str | None = None
