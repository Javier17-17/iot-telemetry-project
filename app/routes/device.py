from fastapi import APIRouter
from app.models.device import Device
from app.services.device_service import insert_device, get_all_devices

router = APIRouter(prefix="/devices", tags=["Devices"])


@router.post("/")
def add_device(data: Device):
    return insert_device(data)


@router.get("/")
def read_devices():
    return get_all_devices()