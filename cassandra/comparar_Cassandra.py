from cassandra.cluster import Cluster
import pandas as pd
import time

# Conexión a Cassandra
def conectar_cassandra():
    try:
        cassandra_cluster = Cluster(['localhost'])
        cassandra_session = cassandra_cluster.connect('trabajo')  # Asegúrate de que el keyspace 'trabajo' esté creado
        return cassandra_session, cassandra_cluster
    except Exception as err:
        print(f"Error de conexión a Cassandra: {err}")
        return None, None

# Función para medir el tiempo de inserción en Cassandra
def medir_insercion_cassandra(cassandra_session):
    start_time = time.time()
    # Cargar datos y hacer inserciones
    clientes_df = pd.read_csv("../Clientes.csv")
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

# Función para medir el tiempo de consulta en Cassandra
def medir_consulta_cassandra(cassandra_session):
    start_time = time.time()
    rows = cassandra_session.execute("SELECT * FROM Clientes")
    return time.time() - start_time, len(list(rows))

# Ejecución de las pruebas
cassandra_session, cassandra_cluster = conectar_cassandra()
if cassandra_session is None:
    exit()

# 1. Inserción de datos en Cassandra
print("Insertando en Cassandra...")
cassandra_insercion_tiempo = medir_insercion_cassandra(cassandra_session)
print(f"Tiempo de inserción en Cassandra: {cassandra_insercion_tiempo:.2f} segundos")

# 2. Consulta en Cassandra
print("Consultando en Cassandra...")
cassandra_consulta_tiempo, cassandra_resultado_cantidad = medir_consulta_cassandra(cassandra_session)
print(f"Tiempo de consulta en Cassandra: {cassandra_consulta_tiempo:.2f} segundos, Resultados: {cassandra_resultado_cantidad}")

# Cierre de conexiones
cassandra_cluster.shutdown()
