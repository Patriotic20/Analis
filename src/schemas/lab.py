from pydantic import BaseModel


class LabBase(BaseModel):
    name : str
    description: str


class LabCreate(LabBase):
    pass


class LabUpdate(BaseModel):
    name: str | None = None
    description : str | None = None
