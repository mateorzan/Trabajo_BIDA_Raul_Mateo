import mysql.connector
from mysql.connector import Error

def borrar_datos(host, dbname, user, password):
    try:
        # Conectar a la base de datos
        conn = mysql.connector.connect(
            host=host,
            database=dbname,
            user=user,
            password=password
        )

        if conn.is_connected():
            print(f"Conexión exitosa a la base de datos {dbname}")
            cursor = conn.cursor()

            # Obtener el nombre de todas las tablas
            cursor.execute("SHOW TABLES")
            tablas = cursor.fetchall()

            # Borrar los datos de cada tabla
            for tabla in tablas:
                cursor.execute(f"TRUNCATE TABLE {tabla[0]}")
                print(f"Datos borrados de la tabla {tabla[0]}")

            # Confirmar los cambios y cerrar la conexión
            conn.commit()

    except Error as e:
        print(f"Error al borrar los datos: {e}")
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()
            print("Conexión cerrada")

# Llamada a la función
borrar_datos('localhost', 'Trabajo', 'root', '')
