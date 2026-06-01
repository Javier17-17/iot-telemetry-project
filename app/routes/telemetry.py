from typing import Optional

from fastapi import APIRouter, Query

from app.models.telemetry import Telemetry
from app.services.telemetry_service import insert_telemetry, get_all_telemetry

# Router de telemetria
router = APIRouter(prefix="/telemetry", tags=["Telemetry"])


# POST -> guardar datos
@router.post("/")
def add_telemetry(data: Telemetry):
    insert_telemetry(data)
    return {"message": "Dato guardado correctamente"}


# GET -> obtener datos con filtros opcionales
@router.get("/")
def read_telemetry(
    device_id: Optional[int] = None,
    limit: int = Query(default=100, ge=1, le=1000)
):
    return get_all_telemetry(device_id=device_id, limit=limit)