# Solución para el Laboratorio de ETL y Análisis de Datos

Este documento describe la solución implementada para cargar y analizar datos demográficos y de calidad del aire en una base de datos SQLite, y posteriormente realizar consultas para analizar las tendencias en las ciudades más pobladas.

## Funciones Implementadas

### 1. Cargar Datos Demográficos (`ej_1_cargar_datos_demograficos`)

Esta función se encarga de cargar los datos demográficos desde una URL dada. Los pasos principales incluyen:

- Descargar los datos demográficos desde la URL especificada en formato CSV.
- Eliminar las columnas 'Race', 'Count' y 'Number of Veterans' que no son necesarias para el análisis.
- Eliminar las filas duplicadas para asegurar la unicidad de los datos.

### 2. Cargar Calidad del Aire (`ej_2_cargar_calidad_aire`)

Esta función obtiene los datos de calidad del aire para un conjunto de ciudades utilizando una API externa. Los pasos principales son:

- Hacer solicitudes a la API de calidad del aire para cada ciudad en el conjunto.
- Extraer el índice de calidad del aire 'overall_aqi' de la respuesta de la API.
- Crear un DataFrame que asocie cada ciudad con su respectivo 'overall_aqi'.
- Filtrar y excluir las ciudades para las cuales no se tienen datos de calidad del aire.

### 3. Cargar Datos en SQLite y Consulta SQL (`cargar_datos_sqlite`)

Esta función integra los datos demográficos y de calidad del aire en una base de datos SQLite y realiza una consulta SQL para analizar tendencias. Los pasos principales incluyen:

- Cargar los DataFrames de datos demográficos y calidad del aire en la base de datos SQLite.
- Crear dos tablas en la base de datos: una para datos demográficos y otra para calidad del aire.
- Ejecutar una consulta SQL que se une a ambas tablas y selecciona las 10 ciudades más pobladas, mostrando su población y el índice de calidad del aire.

## Análisis y Consultas SQL

La consulta SQL realizada busca entender si existe una correlación entre la población de las ciudades y la calidad del aire. La hipótesis es que las ciudades más pobladas podrían tener peor calidad del aire.

La consulta ordena las ciudades por población de mayor a menor y muestra el índice de calidad del aire para cada una. Esta información es crucial para entender las dinámicas urbanas y ambientales en áreas densamente pobladas.

---

Este documento resume la solución desarrollada para el laboratorio, describiendo cada función y su papel en el proceso de ETL y análisis de datos.
