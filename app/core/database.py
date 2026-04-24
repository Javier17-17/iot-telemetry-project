import psycopg2

# Función para conectarse a PostgreSQL
# Se reutiliza en todo el proyecto

def get_connection():
    return psycopg2.connect(
        host="localhost",
        database="iot_db",
        user="postgres",
        password="1234"
    )