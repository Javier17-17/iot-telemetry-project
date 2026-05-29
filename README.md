# IoT Telemetry Project

Proyecto de telemetría IoT industrial con backend en FastAPI, base de datos PostgreSQL, simulador de datos y dashboards en Grafana.

## Arquitectura

```text
Simulador -> Backend FastAPI -> PostgreSQL -> Grafana
```

El simulador genera datos de secadero y báscula.  
El backend recibe esos datos mediante endpoints REST y los guarda en PostgreSQL.  
Grafana se conecta a PostgreSQL para visualizar la información en dashboards.

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
│   ├── dashboard-secaderos.json
│   └── dashboard-resumen-kpis.json
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

Archivo de backup/exportación:

```text
db/iot_db_backup.sql
```

Para importarlo en pgAdmin:

1. Crear una base de datos llamada `iot_db`.
2. Abrir `Query Tool`.
3. Ejecutar el contenido de `db/iot_db_backup.sql`.

## Configuración PostgreSQL

El backend usa la conexión definida en:

```text
app/core/database.py
```

Configuración actual:

```python
host="localhost"
database="iot_db"
user="postgres"
password="1234"
```

Si se cambia el usuario, contraseña o nombre de la base de datos, hay que modificar ese archivo.

## Ejecutar Backend

Desde la raíz del proyecto:

```powershell
cd C:\xampp\htdocs\Prácticas\iot-backend
venv\Scripts\activate
python -m uvicorn main:app --reload
```

La API quedará disponible en:

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

El simulador envía datos cada pocos segundos a:

```text
POST /telemetry/
POST /scale-events/
```

Actualmente usa fecha y hora actual para que Grafana pueda mostrar datos recientes.

## Endpoints Principales

### Telemetría

```http
GET /telemetry/
POST /telemetry/
```

Ejemplo de `POST /telemetry/`:

```json
{
  "device_id": 1,
  "temperature": 22,
  "humidity": 40,
  "timestamp": "2026-05-29T13:15:10"
}
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

Las alarmas se generan automáticamente al recibir telemetría si:

```text
temperature > 28
humidity > 65
```

### Eventos De Báscula

```http
GET /scale-events/
POST /scale-events/
```

Ejemplo de `POST /scale-events/`:

```json
{
  "weight": 2.83,
  "truck_plate": "1234ABC",
  "timestamp": "2026-05-29T13:15:10"
}
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
grafana/dashboard-secaderos.json
grafana/dashboard-resumen-kpis.json
```

Para importarlos en Grafana:

1. Ir a `Dashboards`.
2. Seleccionar `Import`.
3. Cargar el archivo JSON.
4. Seleccionar la fuente de datos PostgreSQL.

## Dashboards

### Dashboard Secaderos

Incluye:

- Temperatura por tiempo
- Humedad por tiempo
- Temperatura y humedad
- Última temperatura
- Última humedad
- Últimas mediciones

### Dashboard Resumen KPIs

Incluye:

- Total de mediciones
- Total de pesajes
- Total de alarmas
- Temperatura media
- Humedad media
- Últimas alarmas

Los dashboards usan filtros temporales de Grafana para mostrar datos según el rango seleccionado.

## Estado Actual

Funcionalidades implementadas:

- Backend FastAPI funcionando
- PostgreSQL conectado
- Simulador integrado con backend
- Inserción de datos de telemetría
- Inserción de eventos de báscula
- Generación automática de alarmas
- Dashboards de Grafana creados y exportados
- Backup SQL de base de datos incluido

## Próximos Pasos

- Finalizar dashboard de básculas
- Añadir endpoint de KPIs en backend
- Añadir filtros en endpoints de telemetría
- Mejorar gestión de errores
- Preparar integración con Odoo más adelante