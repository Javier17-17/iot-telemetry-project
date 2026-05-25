from fastapi import APIRouter
from app.models.scale_events import ScaleEvent
from app.services.scale_event_service import insert_scale_event, get_all_scale_events

router = APIRouter(prefix="/scale-events", tags=["Scale Events"])


@router.post("/")
def add_scale_event(data: ScaleEvent):
    return insert_scale_event(data)


@router.get("/")
def read_scale_events():
    return get_all_scale_events()