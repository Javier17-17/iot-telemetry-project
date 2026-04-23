# IoT Telemetry Project

Proyecto de visualización de datos industriales.

## Estructura

- backend: API y lógica
- frontend: visualización
- simulator: generación de datos
- db: base de datos
- docs: documentación


Proyecto de telemetría IoT
==========================

Este proyecto simula un sistema de telemetría industrial basado en IoT.

Permite generar datos de sensores (simulados), enviarlos a una API, almacenarlos en una base de datos y consultarlos posteriormente.

---

## Objetivo del proyecto

El objetivo es construir una arquitectura básica IoT capaz de:

- Generar datos de sensores (temperatura, humedad, etc.)
- Enviar datos a una API REST
- Guardar la información en una base de datos PostgreSQL
- Consultar los datos mediante endpoints GET
- Preparar el sistema para futuras visualizaciones (Grafana u otros)

---

## Arquitectura del sistema

El flujo de datos es el siguiente:

Simulador → Backend (FastAPI) → Base de datos (PostgreSQL) → Consultas API

---

## Tecnologías utilizadas

- Python
- FastAPI
- PostgreSQL
- Requests (simulador)
- Uvicorn

---

## Estructura del proyecto

backend: API REST y lógica de negocio  
simulador: generación de datos aleatorios tipo IoT  
db: scripts y estructura de base de datos  
docs: documentación del proyecto  

---

## Endpoints principales

### POST /telemetry/
Guarda un nuevo dato de telemetría.

Ejemplo de body:
{
  "device_id": 1,
  "temperature": 25.5,
  "humidity": 60,
  "timestamp": "2026-04-23T10:00:00"
}

---

### GET /telemetry/
Devuelve todos los datos almacenados en la base de datos.

---

## Cómo ejecutar el proyecto

1. Instalar dependencias:

pip install fastapi uvicorn psycopg2 requests

---

2. Iniciar el backend:

uvicorn app.main:app --reload

---

3. Ejecutar el simulador:

python simulator/simulator.py

---

## Notas

- El simulador genera datos automáticamente cada X segundos
- La API está pensada para ampliarse con alertas, KPIs y dashboards
- El proyecto es una base para un sistema IoT más completo
