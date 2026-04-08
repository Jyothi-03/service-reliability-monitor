from pydantic import BaseModel

class Service(BaseModel):
    id: int | None = None
    url: str

class Status(BaseModel):
    service_id: int
    status: str
    response_time: int