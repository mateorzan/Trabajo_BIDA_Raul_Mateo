import mysql.connector

# Conectar a MySQL
try:
    conn = mysql.connector.connect(
        host="localhost",
        user="root",  # Asegúrate de usar el usuario adecuado
        password="",  # Asegúrate de usar la contraseña adecuada
        database="Trabajo"  # Asegúrate de usar el nombre del database adecuado
    )
    cursor = conn.cursor()

    # Ejecutar la consulta
    try:
        cursor.execute("SELECT * FROM Clientes")
        rows = cursor.fetchall()
        for row in rows:
            print(row)
    except Exception as e:
        print(f"Ocurrió un error en la consulta: {e}")
    finally:
        # Cerrar el cursor después de usarlo
        cursor.close()

except mysql.connector.Error as err:
    print(f"Error en la conexión a MySQL: {err}")

finally:
    # Cerrar la conexión
    if conn.is_connected():
        conn.close()
