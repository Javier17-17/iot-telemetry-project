from app.core.database import get_connection


def get_kpis():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT COUNT(*)
        FROM telemetry
        WHERE timestamp <= NOW()
    """)
    total_measurements = cursor.fetchone()[0]

    cursor.execute("""
        SELECT COUNT(*)
        FROM scale_events
        WHERE timestamp <= NOW()
    """)
    total_scale_events = cursor.fetchone()[0]

    cursor.execute("""
        SELECT COUNT(*)
        FROM alarms
        WHERE timestamp <= NOW()
    """)
    total_alarms = cursor.fetchone()[0]

    cursor.execute("""
        SELECT ROUND(AVG(temperature)::numeric, 2)
        FROM telemetry
        WHERE timestamp <= NOW()
    """)
    avg_temperature = cursor.fetchone()[0]

    cursor.execute("""
        SELECT ROUND(AVG(humidity)::numeric, 2)
        FROM telemetry
        WHERE timestamp <= NOW()
    """)
    avg_humidity = cursor.fetchone()[0]

    cursor.execute("""
        SELECT temperature, humidity, timestamp
        FROM telemetry
        WHERE timestamp <= NOW()
        ORDER BY timestamp DESC
        LIMIT 1
    """)
    latest_telemetry = cursor.fetchone()

    cursor.close()
    conn.close()

    return {
        "total_measurements": total_measurements,
        "total_scale_events": total_scale_events,
        "total_alarms": total_alarms,
        "avg_temperature": float(avg_temperature) if avg_temperature is not None else 0,
        "avg_humidity": float(avg_humidity) if avg_humidity is not None else 0,
        "latest_telemetry": {
            "temperature": latest_telemetry[0],
            "humidity": latest_telemetry[1],
            "timestamp": latest_telemetry[2]
        } if latest_telemetry else None
    }