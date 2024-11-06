import mysql.connector
import pandas as pd

try:
    # Conectar a MySQL
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",  # Asegúrate de reemplazar por la contraseña correcta
        port=3306
    )
    cursor = conn.cursor()

    # Crear la base de datos "Trabajo" si no existe
    cursor.execute("CREATE DATABASE IF NOT EXISTS Trabajo")
    
    # Seleccionar la base de datos "Trabajo"
    cursor.execute("USE Trabajo")

    # Crear tablas en MySQL
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Clientes (
        ClienteID INT PRIMARY KEY,
        Nombre VARCHAR(50),
        Apellido VARCHAR(50),
        Correo VARCHAR(100),
        Telefono VARCHAR(100),
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
            cursor.execute(
                f"INSERT INTO {table_name} ({', '.join(columns)}) VALUES ({', '.join(['%s'] * len(columns))})",
                tuple(row)
            )
        conn.commit()

    # Cargar los datos de cada archivo CSV en su respectiva tabla
    cargar_datos("Clientes.csv", "Clientes", ["ClienteID", "Nombre", "Apellido", "Correo", "Telefono", "FechaRegistro"])
    cargar_datos("Productos.csv", "Productos", ["ProductoID", "NombreProducto", "Categoria", "Precio", "Stock"])
    cargar_datos("Ventas.csv", "Ventas", ["VentaID", "ClienteID", "ProductoID", "Cantidad", "FechaVenta"])

except mysql.connector.Error as err:
    print(f"Error: {err}")
finally:
    if conn.is_connected():
        cursor.close()
        conn.close()
