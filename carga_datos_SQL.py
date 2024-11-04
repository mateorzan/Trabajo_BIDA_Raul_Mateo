import mysql.connector
import pandas as pd

# Conectar a MySQL
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="rootpassword",
    database="testdb",
    port=3306
)
cursor = conn.cursor()

# Crear tablas en MySQL
cursor.execute("""
CREATE TABLE IF NOT EXISTS Clientes (
    ClienteID INT PRIMARY KEY,
    Nombre VARCHAR(50),
    Apellido VARCHAR(50),
    Correo VARCHAR(100),
    Telefono VARCHAR(20),
    FechaRegistro DATE
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS Productos (
    ProductoID INT PRIMARY KEY,
    NombreProducto VARCHAR(50),
    Categoria VARCHAR(50),
    Precio DECIMAL(10, 2),
    Stock INT
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS Ventas (
    VentaID INT PRIMARY KEY,
    ClienteID INT,
    ProductoID INT,
    Cantidad INT,
    FechaVenta DATE
)
""")

# Cargar y guardar los datos desde los CSV en las tablas
def cargar_datos(csv_path, table_name, columns):
    df = pd.read_csv(csv_path)
    for _, row in df.iterrows():
        cursor.execute(f"INSERT INTO {table_name} ({', '.join(columns)}) VALUES ({', '.join(['%s'] * len(columns))})", tuple(row))
    conn.commit()

cargar_datos("Clientes.csv", "Clientes", ["ClienteID", "Nombre", "Apellido", "Correo", "Telefono", "FechaRegistro"])
cargar_datos("Productos.csv", "Productos", ["ProductoID", "NombreProducto", "Categoria", "Precio", "Stock"])
cargar_datos("Ventas.csv", "Ventas", ["VentaID", "ClienteID", "ProductoID", "Cantidad", "FechaVenta"])

cursor.close()
conn.close()
