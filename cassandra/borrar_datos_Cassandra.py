from cassandra.cluster import Cluster

def borrar_datos(host, keyspace):
    try:
        # Conectar al clúster de Cassandra sin autenticación
        cluster = Cluster([host])
        session = cluster.connect(keyspace)

        # Obtener el nombre de todas las tablas en el keyspace
        session.set_keyspace(keyspace)
        query = "SELECT table_name FROM system_schema.tables WHERE keyspace_name = %s"
        result = session.execute(query, (keyspace,))

        # Borrar los datos de cada tabla
        for row in result:
            table_name = row.table_name
            # Realizar TRUNCATE en cada tabla
            truncate_query = f"TRUNCATE {table_name}"
            session.execute(truncate_query)
            print(f"Datos borrados de la tabla {table_name}")

    except Exception as e:
        print(f"Error al borrar los datos: {e}")
    finally:
        cluster.shutdown()

# Llamada a la función
borrar_datos('localhost', 'trabajo')
