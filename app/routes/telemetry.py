from fastapi import APIRouter
from app.models.telemetry import Telemetry
from app.services.telemetry_service import insert_telemetry, get_all_telemetry

# Router de telemetría
router = APIRouter(prefix="/telemetry", tags=["Telemetry"])

# POST → guardar datos
@router.post("/")
def add_telemetry(data: Telemetry):
    insert_telemetry(data)
    return {"message": "Dato guardado correctamente"}

# GET → obtener datos
@router.get("/")
def read_telemetry():
    return get_all_telemetry()