from app.core.database import get_connection

# Aquí se gestiona todo lo relacionado con la base de datos

def insert_telemetry(data):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO telemetry (device_id, temperature, humidity, timestamp)
        VALUES (%s, %s, %s, %s)
        """,
        (data.device_id, data.temperature, data.humidity, data.timestamp)
    )

    conn.commit()
    cursor.close()
    conn.close()


def get_all_telemetry():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT id, device_id, temperature, humidity, timestamp
        FROM telemetry
        ORDER BY timestamp DESC
    """)

    rows = cursor.fetchall()

    cursor.close()
    conn.close()

    # Convertimos a JSON (diccionario)
    result = []
    for row in rows:
        result.append({
            "id": row[0],
            "device_id": row[1],
            "temperature": row[2],
            "humidity": row[3],
            "timestamp": row[4]
        })

    return result