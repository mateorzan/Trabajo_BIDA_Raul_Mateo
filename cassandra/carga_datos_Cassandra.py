from cassandra.cluster import Cluster
import pandas as pd

# Conectar a Cassandra
cluster = Cluster(['localhost'])
session = cluster.connect()

# Crear keyspace y tablas en Cassandra
session.execute("""
CREATE KEYSPACE IF NOT EXISTS trabajo WITH REPLICATION = 
{ 'class' : 'SimpleStrategy', 'replication_factor' : 1 }
""")
session.set_keyspace('trabajo')

session.execute("""
CREATE TABLE IF NOT EXISTS Clientes (
    ClienteID int PRIMARY KEY,
    Nombre text,
    Apellido text,
    Correo text,
    Telefono text,
    FechaRegistro date
)
""")

session.execute("""
CREATE TABLE IF NOT EXISTS Productos (
    ProductoID int PRIMARY KEY,
    NombreProducto text,
    Categoria text,
    Precio decimal,
    Stock int
)
""")

session.execute("""
CREATE TABLE IF NOT EXISTS Ventas (
    VentaID int PRIMARY KEY,
    ClienteID int,
    ProductoID int,
    Cantidad int,
    FechaVenta date
)
""")

# Función para cargar datos desde CSV
def cargar_datos_cassandra(csv_path, table_name, columns):
    df = pd.read_csv(csv_path)
    for _, row in df.iterrows():
        session.execute(f"INSERT INTO {table_name} ({', '.join(columns)}) VALUES ({', '.join(['%s'] * len(columns))})", tuple(row))

# Cargar datos en Cassandra
cargar_datos_cassandra("../Clientes.csv", "Clientes", ["ClienteID", "Nombre", "Apellido", "Correo", "Telefono", "FechaRegistro"])
cargar_datos_cassandra("../Productos.csv", "Productos", ["ProductoID", "NombreProducto", "Categoria", "Precio", "Stock"])
cargar_datos_cassandra("../Ventas.csv", "Ventas", ["VentaID", "ClienteID", "ProductoID", "Cantidad", "FechaVenta"])

cluster.shutdown()
