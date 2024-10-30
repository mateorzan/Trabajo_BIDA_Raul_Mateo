import pandas as pd
import random
from faker import Faker
import argparse

# Configuración inicial para Faker
fake = Faker()

# Configuración de argumentos
parser = argparse.ArgumentParser(description='Generar un dataset con datos aleatorios.')
parser.add_argument('num_records', type=int, help='Número de registros a generar para cada tabla')

# Función para generar datos aleatorios y exportar a CSV
def generar_dataset(num_records):
    # Datos de Clientes
    clientes_data = {
        "ClienteID": range(1, num_records + 1),
        "Nombre": [fake.first_name() for _ in range(num_records)],
        "Apellido": [fake.last_name() for _ in range(num_records)],
        "Correo": [fake.email() for _ in range(num_records)],
        "Telefono": [fake.phone_number() for _ in range(num_records)],
        "FechaRegistro": [fake.date_between(start_date="-3y", end_date="today") for _ in range(num_records)]
    }
    clientes_df = pd.DataFrame(clientes_data)
    clientes_df.to_csv("Clientes.csv", index=False)

    # Datos de Productos
    categorias = ["Electrónica", "Ropa", "Hogar", "Juguetes", "Libros"]
    productos_data = {
        "ProductoID": range(1, num_records + 1),
        "NombreProducto": [fake.word().capitalize() for _ in range(num_records)],
        "Categoria": [random.choice(categorias) for _ in range(num_records)],
        "Precio": [round(random.uniform(5.0, 500.0), 2) for _ in range(num_records)],
        "Stock": [random.randint(1, 100) for _ in range(num_records)]
    }
    productos_df = pd.DataFrame(productos_data)
    productos_df.to_csv("Productos.csv", index=False)

    # Datos de Ventas
    ventas_data = {
        "VentaID": range(1, num_records + 1),
        "ClienteID": [random.randint(1, num_records) for _ in range(num_records)],
        "ProductoID": [random.randint(1, num_records) for _ in range(num_records)],
        "Cantidad": [random.randint(1, 5) for _ in range(num_records)],
        "FechaVenta": [fake.date_between(start_date="-2y", end_date="today") for _ in range(num_records)]
    }
    ventas_df = pd.DataFrame(ventas_data)
    ventas_df.to_csv("Ventas.csv", index=False)

    print(f"Los archivos Clientes.csv, Productos.csv y Ventas.csv con {num_records} registros han sido generados con éxito.")

if __name__ == "__main__":
    args = parser.parse_args()
    generar_dataset(args.num_record)
