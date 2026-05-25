from fastapi import APIRouter
from app.services.alarm_service import get_all_alarms

router = APIRouter(prefix="/alarms", tags=["Alarms"])


@router.get("/")
def read_alarms():
    return get_all_alarms()