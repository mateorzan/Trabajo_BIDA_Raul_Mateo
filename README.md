# Trabajo BIDA Raul Mateo

## Introducción

Trabajo Cassandra vs MySQL

## Contenido del repositorio

- **cassandra/** - Carpeta que contiene los archivos y configuraciones específicas para Cassandra.
- **mysql/** - Carpeta que contiene los archivos y configuraciones específicas para MySQL.
- **README.md** - Archivo de documentación del proyecto.
- **comparar_r.py** - Script en Python para realizar comparaciones entre Cassandra y MySQL.
- **docker-compose_Cassandra.yml** - Archivo Docker Compose para desplegar el servidor Cassandra.
- **docker-compose_MYSQL.yml** - Archivo Docker Compose para desplegar el servidor MySQL.
- **generar_datos.py** - Script en Python para generar datos que se insertarán en las bases de datos y se utilizarán en las pruebas de comparación.

# INSTRUCCIONES FUNCIONAMIENTO COMPLETAS

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
```
```bash
git clone git@github.com:mateorzan/Trabajo_BIDA_Raul_Mateo.git
```

## DOCKER

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

```bash
python generar_dataset.py
```


## Automatizar Carga de datos en BD


### Carga en MySQL


Instalamos librerias necesarias.
```bash
conda install mysql-connector-python
```
Ejecutamos archivo carga datos SQL.py

```bash
python carga_datos_SQL.py
```

### Carga en Cassandra

Instalamos librerias necesarias.
```bash
conda install cassandra-driver
```
Ejecutamos archivo carga datos SQL.py

```bash
python carga_datos_Cassandra.py
```

## Consultas BD

### Consulta SQL

Ejecutamos consultas.

```bash
python consulta_SQL.py
```

### Consulta Cassandra

Ejecutamos consultas.

```bash
python consulta_Cassandra.py
```

## Comparamos rendimiento

```bash
python rendimiento.py
```

## Notas

- Asegúrate de revisar las configuraciones de conexión en los archivos de Docker y en el script `generar_datos.py` si necesitas personalizarlos para tu entorno.

## Autor

Creado por **mateorzan** y **Raul**.
