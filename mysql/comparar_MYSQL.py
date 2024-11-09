import mysql.connector
import pandas as pd
import time

# Conexión a MySQL
def conectar_mysql():
    try:
        mysql_conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",  # Cambiar según tu configuración
            database="Trabajo",
            port=3306
        )
        return mysql_conn
    except mysql.connector.Error as err:
        print(f"Error de conexión a MySQL: {err}")
        return None

# Función para medir el tiempo de inserción en MySQL
def medir_insercion_mysql(mysql_cursor, mysql_conn):
    start_time = time.time()
    # Cargar datos y hacer inserciones
    clientes_df = pd.read_csv("../Clientes.csv")
    for _, row in clientes_df.iterrows():
        # Verificar si el cliente ya existe antes de insertar
        mysql_cursor.execute(
            "SELECT ClienteID FROM Clientes WHERE ClienteID = %s", (row['ClienteID'],)
        )
        result = mysql_cursor.fetchone()
        if not result:  # Si no se encuentra el cliente, insertamos
            mysql_cursor.execute(
                "INSERT INTO Clientes (ClienteID, Nombre, Apellido, Correo, Telefono, FechaRegistro) VALUES (%s, %s, %s, %s, %s, %s)",
                tuple(row)
            )
    mysql_conn.commit()  # Commit sobre la conexión, no el cursor
    return time.time() - start_time

# Función para medir el tiempo de consulta en MySQL
def medir_consulta_mysql(mysql_cursor):
    start_time = time.time()
    mysql_cursor.execute("SELECT * FROM Clientes")
    rows = mysql_cursor.fetchall()
    return time.time() - start_time, len(rows)

# Ejecución de las pruebas
mysql_conn = conectar_mysql()
if mysql_conn is None:
    exit()

mysql_cursor = mysql_conn.cursor()

# 1. Inserción de datos en MySQL
print("Insertando en MySQL...")
mysql_insercion_tiempo = medir_insercion_mysql(mysql_cursor, mysql_conn)
print(f"Tiempo de inserción en MySQL: {mysql_insercion_tiempo:.2f} segundos")

# 2. Consulta en MySQL
print("Consultando en MySQL...")
mysql_consulta_tiempo, mysql_resultado_cantidad = medir_consulta_mysql(mysql_cursor)
print(f"Tiempo de consulta en MySQL: {mysql_consulta_tiempo:.2f} segundos, Resultados: {mysql_resultado_cantidad}")

# Cierre de conexiones
mysql_cursor.close()
mysql_conn.close()
