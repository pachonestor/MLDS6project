# Definición de los datos

## Origen de los datos

Los datos son tienen su origen un paper del  profesor Fabio González, Ph.D. y a su alumno John Arevalo, llamado Gated Multimodal Units for Information Fusion.
La base de datos se puede leer del repositorio de github de profesor, Alejandro Correa Bahnsen Ph.D.

## Especificación de los scripts para la carga de datos

- El script de carga se encuentra en: 'scripts/data_acquisition/Carga_datos.ipynb'. 

## Referencias a rutas o bases de datos origen y destino

- https://github.com/albahnsen/MIAD_ML_and_NLP/raw/main/datasets/dataTraining.zip'
- https://arxiv.org/abs/1702.01992

### Rutas de origen de datos

Se descargo la base de datos en la carpeta local con la ruta:
- Modulo3/proyecto/datos/origen/

Esta base de datos está en formato csv, contiene 7895 filas y 5 columnas, las cuales se conderan relevantes para este proyecto la columna de 
plot que contiene un breve resumen en inglés de la trama de la película y la columna de genres, donde se encuentran los géneros en los cuales puede ser clasificado esa película.

Se le hara una limpieza de datos a las columnas de plot y genres de la base de datos. A plot se le haran los siguientes procesos de limpieza:
- Tokenización
- Normalización de textos.
- Limpieza con expresiones regulares
- Lematización
- Filtrado de palabras
- Stemming.

Por otro lado, a los géneros se la va a quitar todo lo que no sea las palabras que  las definen y se covertiran en variables dummies.

### Base de datos de destino
Ya con la columna plot limpia se procedera a transformar el texto limpio en un embedding, en este caso será el algoritmo TfidfVectorizer y se concatenará con las varibles de género dummies.

- Se guadara la data preprocesada en un archivo xlsx con la columna plot limpiada y las 24 variables dummies de los géneros de películas
- Se guardara en la carpeta Modulo3/proyecto/datos/preprocesada/.

