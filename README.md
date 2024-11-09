# Trabajo BIDA: Comparativa entre Cassandra y MySQL

Autores: **Mateo Rzan** y **Raúl E.**

---

## Índice

- [Introducción](#introducción)
- [Contenido del Repositorio](#contenido-del-repositorio)
- [Requisitos Previos](#requisitos-previos)
- [Instrucciones de Ejecución](#instrucciones-de-ejecución)
- [Automatización de la Carga de Datos](#automatización-de-la-carga-de-datos)
- [Consultas a las Bases de Datos](#consultas-a-las-bases-de-datos)
- [Comparación de Rendimiento](#comparación-de-rendimiento)
- [Notas](#notas)
- [Autores](#autores)

---

## Introducción

Trabajo Cassandra vs MySQL.

## Contenido del repositorio

- **cassandra/** - Carpeta que contiene los archivos de carga de datos y consultas específicas para Cassandra.
	- **carga_datos_Cassandra.py** - Archivo que realiza la carga de datos a la base de datos.
	- **consulta_cassandra.py** - Archivo que realiza una consulta a la base de datos.
        - **comparar_Cassandra.py** - Archivo que comprueba el rendimiento.
        - **borrar_datos_Cassandra.py** - Archivo opcional que borra los datos insertados.
- **mysql/** - Carpeta que contiene los archivos  de carga de datos y consultas específicas para MySQL.
	- **carga_datos_SQL.py** - Archivo que realiza la carga de datos a la base de datos.
        - **consulta_mysql.py** - Archivo que realiza una consulta a la base de datos.
        - **comparar_MYSQL.py** - Archivo que comprueba el rendimiento.
        - **borrar_datos_SQL.py** - Archivo opcional que borra los datos insertados.
- **README.md** - Archivo de documentación del proyecto.
- **comparar.py** - Script en Python para realizar comparaciones entre Cassandra y MySQL.
- **docker-compose_Cassandra.yml** - Archivo Docker Compose para desplegar el servidor Cassandra.
- **docker-compose_MYSQL.yml** - Archivo Docker Compose para desplegar el servidor MySQL.
- **generar_datos.py** - Script en Python para generar datos que se insertarán en las bases de datos y se utilizarán en las pruebas de comparación.
- **generar_datos.py** - Script en Python para generar datos que se insertarán en las bases de datos y se utilizarán en las pruebas de comparacion.
- **Clientes.csv** - Datos generados con el script
- **Productos.csv** - Datos generados con el script
- **Ventas.csv** - Datos generados con el script

# Instrucciones de funcionamiento completas

## Requisitos Previos

Instrucciones sobre los requisitos necesarios para el proyecto.

- **Docker**: Asegúrate de tener Docker instalado en tu sistema para levantar los servicios de bases de datos.
- **Python 3**: Necesario para ejecutar el script `generar_datos.py`.

### Instalación de Miniconda(Si no lo tienes ya instalado)

Instrucciones para instalar Miniconda.

Si no tienes instalado Conda, ejecuta los siguientes comandos en tu terminal de Ubuntu:

```bash
mkdir -p ~/miniconda3
wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh -O ~/miniconda3/miniconda.sh
bash ~/miniconda3/miniconda.sh -b -u -p ~/miniconda3
rm ~/miniconda3/miniconda.sh
```

### Crear un Entorno Conda (Opcional)

Instrucciones para crear y activar un entorno con Conda.

```bash
conda create --name nombre_del_entorno 
conda env list
conda activate nombre_del_entorno
```
### Clonamos el repositorio en la ubicación deseada

```bash
git clone https://github.com/mateorzan/Trabajo_BIDA_Raul_Mateo.git
cd Trabajo_BIDA_Raul_Mateo
```

## DOCKER

Importante abrir Docker Desktop primero.
### Ejecucion Docker Compose Cassandra.

```bash
docker-compose -f docker-compose_Cassandra.yml up
```

### Ejecucion Docker Compose MySQL.


```bash
docker-compose -f docker-compose_MySQL.yml up
```

### Instalación de Bibliotecas Necesarias para ejecutar el script.

Instrucciones para instalar las bibliotecas necesarias.

```bash
conda config --add channels conda-forge
conda install python3.10.0
conda install pandas faker
```
### Generación del Dataset.

Instrucciones para ejecutar el script que generará el conjunto de datos.

Al final especificas el numero de datos que quieras generar, en este caso vamos a probar con 10.

```bash
python generar_datos.py 10
```

## Automatizar Carga de datos en BD

### Carga en MySQL

Instalamos librerias necesarias.
```bash
conda install mysql-connector-python
```
Ejecutamos archivo carga datos SQL.py

```bash
cd mysql
python carga_datos_SQL.py
```

### Carga en Cassandra

Instalamos librerias necesarias.
```bash
conda install cassandra-driver
```
Ejecutamos archivo carga datos SQL.py

```bash
cd cassandra
python carga_datos_Cassandra.py
```

## Consultas BD

### Consulta SQL

Ejecutamos consultas.

```bash
cd mysql
python consulta_SQL.py
```

### Consulta Cassandra

Ejecutamos consultas.

```bash
cd cassandra
python consulta_Cassandra.py
```

## Comparamos rendimiento

### Comparador general

Este script hace una comparacion de rendimiento cuandos los dos servidores estan activos.

```bash
python comparar.py
```

### MySQL

Este script hace una comparacion de rendimiento especifica a mysql, la idea es ejecutarlo con el servidor de cassandra apagado.
```bash
cd mysql
python comparar_MYSL.py
```
### Cassandra

Este script hace una comparacion de rendimiento especifica a cassandra, la idea es ejecutarlo con el sevidor de mysql apagado. 
```bash
cd cassandra
python comparar_Cassandra.py
```

## Notas

- Asegúrate de revisar las configuraciones de conexión en los archivos de Docker y en el script `generar_datos.py` si necesitas personalizarlos para tu entorno.

## Autor

Creado por **mateorzan** y **Raul**.
