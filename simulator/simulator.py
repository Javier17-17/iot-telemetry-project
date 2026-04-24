import requests
import random
from datetime import datetime
import time

# Simula un dispositivo IoT enviando datos cada 5 segundos

print("Simulador iniciado...")

while True:
    data = {
        "device_id": 1,
        "temperature": round(random.uniform(20, 30), 2),
        "humidity": round(random.uniform(40, 70), 2),
        "timestamp": datetime.now().isoformat()
    }

    try:
        response = requests.post(
            "http://127.0.0.1:8000/telemetry/",
            json=data
        )

        print("Enviado:", data)
        print("Respuesta:", response.json())

    except Exception as e:
        print("Error al enviar datos:", e)

    time.sleep(5)