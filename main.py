from fastapi import FastAPI

from app.routes.telemetry import router as telemetry_router
from app.routes.device import router as devices_router
from app.routes.scale_events import router as scale_events_router
from app.routes.alarms import router as alarms_router
from app.routes.kpis import router as kpis_router

app = FastAPI()

app.include_router(telemetry_router)
app.include_router(devices_router)
app.include_router(scale_events_router)
app.include_router(alarms_router)
app.include_router(kpis_router)


@app.get("/")
def root():
    return {"message": "API IoT funcionando correctamente"}