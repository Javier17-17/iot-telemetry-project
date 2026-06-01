from app.core.database import get_connection


def create_alarm_if_needed(cursor, data):
    if data.temperature > 28:
        cursor.execute(
            """
            INSERT INTO alarms (device_id, alarm_type, value, message, timestamp)
            VALUES (%s, %s, %s, %s, %s)
            """,
            (
                data.device_id,
                "HIGH_TEMPERATURE",
                data.temperature,
                "Temperatura demasiado alta",
                data.timestamp
            )
        )

    if data.humidity > 65:
        cursor.execute(
            """
            INSERT INTO alarms (device_id, alarm_type, value, message, timestamp)
            VALUES (%s, %s, %s, %s, %s)
            """,
            (
                data.device_id,
                "HIGH_HUMIDITY",
                data.humidity,
                "Humedad demasiado alta",
                data.timestamp
            )
        )


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

    create_alarm_if_needed(cursor, data)

    conn.commit()
    cursor.close()
    conn.close()


def get_all_telemetry(device_id=None, limit=100):
    conn = get_connection()
    cursor = conn.cursor()

    query = """
        SELECT id, device_id, temperature, humidity, timestamp
        FROM telemetry
    """

    params = []

    if device_id is not None:
        query += " WHERE device_id = %s"
        params.append(device_id)

    query += " ORDER BY timestamp DESC LIMIT %s"
    params.append(limit)

    cursor.execute(query, params)
    rows = cursor.fetchall()

    cursor.close()
    conn.close()

    return [
        {
            "id": row[0],
            "device_id": row[1],
            "temperature": row[2],
            "humidity": row[3],
            "timestamp": row[4]
        }
        for row in rows
    ]