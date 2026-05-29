from fastapi import APIRouter
from app.services.kpi_service import get_kpis

router = APIRouter(prefix="/kpis", tags=["KPIs"])


@router.get("/")
def read_kpis():
    return get_kpis()