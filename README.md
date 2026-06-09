# IoT Telemetry Project

Proyecto de telemetria IoT industrial con backend en FastAPI, base de datos PostgreSQL, simulador de datos y dashboards en Grafana.

## Arquitectura

```text
Simulador -> Backend FastAPI -> PostgreSQL -> Grafana
```

El simulador genera datos de secadero y bascula.
El backend recibe los datos mediante endpoints REST y los guarda en PostgreSQL.
Grafana se conecta a PostgreSQL para visualizar los datos.

## Tecnologias

- Python
- FastAPI
- PostgreSQL
- psycopg2
- Uvicorn
- Requests
- Grafana
- Docker / Docker Compose

## Estructura principal

```text
iot-telemetry-project/
├── app/
│   ├── core/
│   ├── models/
│   ├── routes/
│   └── services/
│
├── db/
│   └── iot_db_backup.sql
│
├── grafana/
│   ├── dashboard-dryers.json
│   ├── dashboard-scales.json
│   ├── dashboard-summary-kpis.json
│   └── provisioning/
│
├── iot-telemetry-project-simulator/
│   └── src/
│
├── docker-compose.yml
├── Dockerfile
├── requirements.txt
├── main.py
└── README.md
```

## Ejecucion con Docker

Requisito:

```text
Docker Desktop
```

Desde la raiz del proyecto:

```powershell
docker compose up --build
```

Servicios disponibles:

```text
Backend: http://localhost:8000
Swagger: http://localhost:8000/docs
Grafana: http://localhost:3001
PostgreSQL Docker: localhost:5433
```

Credenciales de Grafana:

```text
Usuario: admin
Password: 1234
```

La base de datos se inicializa automaticamente con:

```text
db/iot_db_backup.sql
```

Grafana carga automaticamente:

```text
grafana/dashboard-dryers.json
grafana/dashboard-scales.json
grafana/dashboard-summary-kpis.json
```

Para parar los contenedores:

```powershell
docker compose down
```

Para borrar tambien los volumenes y reiniciar la base desde el backup:

```powershell
docker compose down -v
```

## Ejecucion local sin Docker

### Base de datos

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

Backup SQL:

```text
db/iot_db_backup.sql
```

Para importarlo en pgAdmin:

1. Crear una base de datos llamada `iot_db`.
2. Abrir `Query Tool`.
3. Ejecutar el contenido de `db/iot_db_backup.sql`.

### Backend

Desde la raiz del proyecto:

```powershell
cd C:\xampp\htdocs\Practicas\iot-backend
venv\Scripts\activate
python -m uvicorn main:app --reload
```

La API queda disponible en:

```text
http://127.0.0.1:8000
```

Swagger:

```text
http://127.0.0.1:8000/docs
```

### Simulador

Con el backend encendido, abrir otra terminal:

```powershell
cd C:\xampp\htdocs\Practicas\iot-backend
venv\Scripts\activate
cd iot-telemetry-project-simulator
python -m src
```

El simulador envia datos a:

```text
POST /telemetry/
POST /scale-events/
```

## Configuracion PostgreSQL

La conexion esta en:

```text
app/core/database.py
```

Por defecto usa:

```text
host: localhost
database: iot_db
user: postgres
password: 1234
```

En Docker se configura mediante variables de entorno:

```text
DB_HOST
DB_PORT
DB_NAME
DB_USER
DB_PASSWORD
```

## Endpoints principales

### Telemetria

```http
GET /telemetry/
POST /telemetry/
```

Filtros:

```http
GET /telemetry/?limit=5
GET /telemetry/?device_id=1&limit=5
```

### Dispositivos

```http
GET /devices/
POST /devices/
```

### Alarmas

```http
GET /alarms/
```

Se generan automaticamente si:

```text
temperature > 28
humidity > 65
```

### Bascula

```http
GET /scale-events/
POST /scale-events/
```

### KPIs

```http
GET /kpis/
```

Devuelve:

```text
total_measurements
total_scale_events
total_alarms
avg_temperature
avg_humidity
latest_telemetry
```

## Grafana

Dashboards disponibles:

- Secaderos
- Basculas
- Resumen/KPIs

Los dashboards usan filtros temporales para funcionar con rangos como:

```text
Last 15 minutes
Last 1 hour
```

## Estado actual

Implementado:

- Backend FastAPI conectado a PostgreSQL
- Simulador integrado con el backend
- Insercion y consulta de telemetria
- Insercion y consulta de eventos de bascula
- Generacion automatica de alarmas
- Endpoint de KPIs
- Filtros basicos en telemetria
- Dashboards de Grafana
- Backup SQL de la base de datos
- Despliegue reproducible con Docker Compose

## Proximos pasos

- Probar Docker desde cero en otro equipo
- Revisar documentacion final
- Integrar Odoo mas adelante si es necesario

## Enlaces a drive
Memoria técnica: https://docs.google.com/document/d/1C8_U_U42fcCT8gRmF4g4ekj3xwPEQLh1j2lcCkqg1Gw/edit?tab=t.0

Instrucciones de instalación: https://docs.google.com/document/d/1E4RkOAvJt63hg2NI5PAdFhsly5ZLQ6dm0Jf-ZPPFiIU/edit?tab=t.0
