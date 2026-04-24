from pydantic import BaseModel
from datetime import datetime

# Modelo de datos que recibe la API
# Valida automáticamente el JSON

class Telemetry(BaseModel):
    device_id: int
    temperature: float
    humidity: float
    timestamp: datetime