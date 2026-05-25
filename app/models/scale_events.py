from pydantic import BaseModel, Field
from datetime import datetime


class ScaleEvent(BaseModel):
    weight: float
    truck_plate: str
    timestamp: datetime = Field(default_factory=datetime.now)