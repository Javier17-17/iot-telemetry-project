from app.core.database import get_connection


def insert_scale_event(data):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO scale_events (weight, truck_plate, timestamp)
        VALUES (%s, %s, %s)
        RETURNING id
        """,
        (data.weight, data.truck_plate, data.timestamp)
    )

    event_id = cursor.fetchone()[0]

    conn.commit()
    cursor.close()
    conn.close()

    return {
        "id": event_id,
        "weight": data.weight,
        "truck_plate": data.truck_plate,
        "timestamp": data.timestamp
    }


def get_all_scale_events():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT id, weight, truck_plate, timestamp
        FROM scale_events
        ORDER BY timestamp DESC
    """)

    rows = cursor.fetchall()

    cursor.close()
    conn.close()

    return [
        {
            "id": row[0],
            "weight": row[1],
            "truck_plate": row[2],
            "timestamp": row[3]
        }
        for row in rows
    ]