import time

# Medición en MySQL
start = time.time()
cursor.execute("SELECT * FROM Clientes WHERE Nombre LIKE 'A%'")
mysql_results = cursor.fetchall()
mysql_time = time.time() - start
print(f"Tiempo de consulta en MySQL: {mysql_time} segundos")

# Medición en Cassandra
start = time.time()
cassandra_results = session.execute("SELECT * FROM Clientes WHERE Nombre LIKE 'A%'")
cassandra_time = time.time() - start
print(f"Tiempo de consulta en Cassandra: {cassandra_time} segundos")
