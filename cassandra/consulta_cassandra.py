from cassandra.cluster import Cluster

# Conectar a Cassandra
cluster = Cluster(['localhost'])
session = cluster.connect()

# Seleccionar el keyspace (asegúrate de usar el keyspace adecuado)
session.set_keyspace('testkeyspace')

# Ejecutar la consulta
try:
    rows = session.execute("SELECT * FROM Clientes")
    for row in rows:
        print(row)
except Exception as e:
    print(f"Ocurrió un error en la consulta: {e}")

# Cerrar la conexión
cluster.shutdown()

