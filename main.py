from fastapi import FastAPI
from app.routes.telemetry import router as telemetry_router

# Archivo principal de la API
# Aquí inicializamos FastAPI y registramos las rutas

app = FastAPI()

# Incluimos las rutas de telemetría
app.include_router(telemetry_router)

# Endpoint de prueba
@app.get("/")
def root():
    return {"message": "API IoT funcionando correctamente"}