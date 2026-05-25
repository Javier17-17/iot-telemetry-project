from app.core.database import get_connection


def insert_device(data):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO devices (name, type, location)
        VALUES (%s, %s, %s)
        RETURNING id
        """,
        (data.name, data.type, data.location)
    )

    device_id = cursor.fetchone()[0]

    conn.commit()
    cursor.close()
    conn.close()

    return {
        "id": device_id,
        "name": data.name,
        "type": data.type,
        "location": data.location
    }


def get_all_devices():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT id, name, type, location
        FROM devices
        ORDER BY id ASC
    """)

    rows = cursor.fetchall()

    cursor.close()
    conn.close()

    return [
        {
            "id": row[0],
            "name": row[1],
            "type": row[2],
            "location": row[3]
        }
        for row in rows
    ]