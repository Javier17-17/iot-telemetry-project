# IoT Telemetry Project

Proyecto de telemetría IoT industrial con backend en FastAPI, base de datos PostgreSQL, simulador de datos y dashboards en Grafana.

## Arquitectura

```text
Simulador -> Backend FastAPI -> PostgreSQL -> Grafana
```

El simulador genera datos de secadero y báscula.  
El backend recibe los datos mediante endpoints REST y los guarda en PostgreSQL.  
Grafana se conecta a PostgreSQL para visualizar los datos.

## Tecnologías

- Python
- FastAPI
- PostgreSQL
- psycopg2
- Uvicorn
- Requests
- Grafana

## Estructura Principal

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
│   └── dashboard-summary-kpis.json
│
├── iot-telemetry-project-simulator/
│   └── src/
│
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

Backup SQL:

```text
db/iot_db_backup.sql
```

Para importarlo en pgAdmin:

1. Crear una base de datos llamada `iot_db`.
2. Abrir `Query Tool`.
3. Ejecutar el contenido de `db/iot_db_backup.sql`.

## Configuración PostgreSQL

La conexión está en:

```text
app/core/database.py
```

Configuración actual:

```text
host: localhost
database: iot_db
user: postgres
password: 1234
```

Si se cambia la contraseña o el nombre de la base de datos, hay que actualizar ese archivo.

## Ejecutar Backend

Desde la raíz del proyecto:

```powershell
cd C:\xampp\htdocs\Prácticas\iot-backend
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

## Ejecutar Simulador

Con el backend encendido, abrir otra terminal:

```powershell
cd C:\xampp\htdocs\Prácticas\iot-backend
venv\Scripts\activate
cd iot-telemetry-project-simulator
python -m src
```

El simulador envía datos a:

```text
POST /telemetry/
POST /scale-events/
```

## Endpoints Principales

### Telemetría

```http
GET /telemetry/
POST /telemetry/
```

También permite filtros:

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

Se generan automáticamente si:

```text
temperature > 28
humidity > 65
```

### Báscula

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

Grafana se conecta directamente a PostgreSQL.

Configuración de la fuente de datos:

```text
Host: localhost:5432
Database: iot_db
User: postgres
Password: 1234
TLS/SSL: disable
```

Dashboards exportados:

```text
grafana/dashboard-dryers.json
grafana/dashboard-scales.json
grafana/dashboard-summary-kpis.json
```

Dashboards disponibles:

- Secaderos
- Básculas
- Resumen/KPIs

Los dashboards usan filtros temporales para funcionar con rangos como `Last 15 minutes` o `Last 1 hour`.

## Estado Actual

Implementado:

- Backend FastAPI conectado a PostgreSQL
- Simulador integrado con el backend
- Inserción y consulta de telemetría
- Inserción y consulta de eventos de báscula
- Generación automática de alarmas
- Endpoint de KPIs
- Filtros básicos en telemetría
- Dashboards de Grafana
- Backup SQL de la base de datos

## Próximos Pasos

- Hacer prueba completa desde cero
- Revisar documentación final
- Integrar Odoo más adelante si es necesario