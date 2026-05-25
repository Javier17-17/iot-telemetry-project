from app.core.database import get_connection


def get_all_alarms():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT id, device_id, alarm_type, value, message, timestamp
        FROM alarms
        ORDER BY timestamp DESC
    """)

    rows = cursor.fetchall()

    cursor.close()
    conn.close()

    return [
        {
            "id": row[0],
            "device_id": row[1],
            "alarm_type": row[2],
            "value": row[3],
            "message": row[4],
            "timestamp": row[5]
        }
        for row in rows
    ]