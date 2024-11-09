import mysql.connector
from cassandra.cluster import Cluster
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

# Conexión a Cassandra
def conectar_cassandra():
    try:
        cassandra_cluster = Cluster(['localhost'])
        cassandra_session = cassandra_cluster.connect('trabajo')  # Asegúrate de que el keyspace 'trabajo' esté creado
        return cassandra_session, cassandra_cluster
    except Exception as err:
        print(f"Error de conexión a Cassandra: {err}")
        return None, None

# Función para medir el tiempo de inserción en MySQL
def medir_insercion_mysql(mysql_cursor, mysql_conn):
    start_time = time.time()
    # Cargar datos y hacer inserciones
    clientes_df = pd.read_csv("Clientes.csv")
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

# Función para medir el tiempo de inserción en Cassandra
def medir_insercion_cassandra(cassandra_session):
    start_time = time.time()
    # Cargar datos y hacer inserciones
    clientes_df = pd.read_csv("Clientes.csv")
    for _, row in clientes_df.iterrows():
        # Verificar si el cliente ya existe antes de insertar (upsert en Cassandra)
        query = "SELECT ClienteID FROM Clientes WHERE ClienteID = %s"
        result = cassandra_session.execute(query, (row['ClienteID'],))
        if not result:  # Si el cliente no existe, lo insertamos
            cassandra_session.execute(
                "INSERT INTO Clientes (ClienteID, Nombre, Apellido, Correo, Telefono, FechaRegistro) VALUES (%s, %s, %s, %s, %s, %s)",
                tuple(row)
            )
    return time.time() - start_time

# Función para medir el tiempo de consulta en MySQL
def medir_consulta_mysql(mysql_cursor):
    start_time = time.time()
    mysql_cursor.execute("SELECT * FROM Clientes")
    rows = mysql_cursor.fetchall()
    return time.time() - start_time, len(rows)

# Función para medir el tiempo de consulta en Cassandra
def medir_consulta_cassandra(cassandra_session):
    start_time = time.time()
    rows = cassandra_session.execute("SELECT * FROM Clientes")
    return time.time() - start_time, len(list(rows))

# Ejecución de las pruebas
# Conexiones
mysql_conn = conectar_mysql()
if mysql_conn is None:
    exit()

mysql_cursor = mysql_conn.cursor()

cassandra_session, cassandra_cluster = conectar_cassandra()
if cassandra_session is None:
    exit()

# 1. Apaga el servidor de Cassandra y realiza la prueba en MySQL
print("Insertando en MySQL...")
mysql_insercion_tiempo = medir_insercion_mysql(mysql_cursor, mysql_conn)
print(f"Tiempo de inserción en MySQL: {mysql_insercion_tiempo:.2f} segundos")

print("Consultando en MySQL...")
mysql_consulta_tiempo, mysql_resultado_cantidad = medir_consulta_mysql(mysql_cursor)
print(f"Tiempo de consulta en MySQL: {mysql_consulta_tiempo:.2f} segundos, Resultados: {mysql_resultado_cantidad}")

# 2. Apaga el servidor de MySQL y enciende Cassandra para realizar la prueba en Cassandra
print("Insertando en Cassandra...")
cassandra_insercion_tiempo = medir_insercion_cassandra(cassandra_session)
print(f"Tiempo de inserción en Cassandra: {cassandra_insercion_tiempo:.2f} segundos")

print("Consultando en Cassandra...")
cassandra_consulta_tiempo, cassandra_resultado_cantidad = medir_consulta_cassandra(cassandra_session)
print(f"Tiempo de consulta en Cassandra: {cassandra_consulta_tiempo:.2f} segundos, Resultados: {cassandra_resultado_cantidad}")

# Cierre de conexiones
mysql_cursor.close()
mysql_conn.close()
cassandra_cluster.shutdown()
