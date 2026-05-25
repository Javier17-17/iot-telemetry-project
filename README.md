# IoT Telemetry Backend

Backend del proyecto de telemetría IoT industrial.

Permite recibir datos simulados de sensores, guardarlos en PostgreSQL, consultarlos mediante una API REST y generar alarmas automáticas.

## Tecnologías

- Python
- FastAPI
- PostgreSQL
- psycopg2
- Uvicorn
- Swagger

## Arquitectura

```text
Simulador -> Backend FastAPI -> PostgreSQL -> Grafana
```

## Estructura

```text
iot-backend/
├── app/
│   ├── core/
│   │   └── database.py
│   ├── models/
│   │   ├── device.py
│   │   ├── scale_events.py
│   │   └── telemetry.py
│   ├── routes/
│   │   ├── alarms.py
│   │   ├── device.py
│   │   ├── scale_events.py
│   │   └── telemetry.py
│   └── services/
│       ├── alarm_service.py
│       ├── device_service.py
│       ├── scale_event_service.py
│       └── telemetry_service.py
├── main.py
└── README.md
```

## Base De Datos

Base de datos utilizada:

```text
iot_db
```

Tablas principales:

```text
devices
telemetry
alarms
scale_events
```

La conexión está configurada en:

```text
app/core/database.py
```

```python
def get_connection():
    return psycopg2.connect(
        host="localhost",
        database="iot_db",
        user="postgres",
        password="1234"
    )
```

## Instalación

Entrar en la carpeta del backend:

```powershell
cd C:\xampp\htdocs\Prácticas\iot-backend
```

Activar el entorno virtual:

```powershell
venv\Scripts\activate
```

Instalar dependencias:

```powershell
pip install fastapi uvicorn psycopg2-binary requests
```

## Ejecución

Ejecutar el servidor:

```powershell
python -m uvicorn main:app --reload
```

La API estará disponible en:

```text
http://127.0.0.1:8000
```

Documentación Swagger:

```text
http://127.0.0.1:8000/docs
```

## Endpoints

### Dispositivos

```http
GET /devices/
POST /devices/
```

Ejemplo de creación:

```json
{
  "name": "Sensor Secadero 2",
  "type": "temperature_humidity",
  "location": "Secadero secundario"
}
```

### Telemetría

```http
GET /telemetry/
POST /telemetry/
```

Ejemplo de envío:

```json
{
  "device_id": 1,
  "temperature": 29.5,
  "humidity": 66,
  "timestamp": "2026-05-21T13:45:00"
}
```

Al enviar telemetría, el backend genera alarmas automáticamente si:

```text
temperature > 28
humidity > 65
```

### Alarmas

```http
GET /alarms/
```

Ejemplo de respuesta:

```json
[
  {
    "id": 1,
    "device_id": 1,
    "alarm_type": "HIGH_TEMPERATURE",
    "value": 29.5,
    "message": "Temperatura demasiado alta",
    "timestamp": "2026-05-21T13:45:00"
  }
]
```

### Eventos De Báscula

```http
GET /scale-events/
POST /scale-events/
```

Ejemplo de creación:

```json
{
  "weight": 1250.5,
  "truck_plate": "1234ABC",
  "timestamp": "2026-05-21T14:05:00"
}
```

## Estado Actual

Funcionalidades implementadas:

- Conexión con PostgreSQL
- Registro y consulta de dispositivos
- Registro y consulta de telemetría
- Generación automática de alarmas
- Consulta de alarmas
- Registro y consulta de eventos de báscula
- Pruebas desde Swagger

## Próximos Pasos

- Añadir filtros por fecha
- Añadir filtros por dispositivo
- Crear endpoints de KPIs
- Preparar consultas para Grafana
- Integrar Odoo más adelante