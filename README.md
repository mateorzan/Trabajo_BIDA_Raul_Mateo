# Trabajo_BIDA_Ra-l_Mateo
Trabajo Cassandra vs MySQL

#SI NO TIENES INSTALADO CONDA

wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh

bash Miniconda3-latest-Linux-x86_64.sh
#CREAMOS ENVIROMETN /OPCIONAL

conda create --name nombre_del_entorno

conda env list

conda activate nombre_del_entorno


#SCRIPT DATASET 

Instala las bibliotecas necesarias:

conda install pandas faker

Ejecuta el script:

python generar_dataset.py
