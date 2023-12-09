
import pandas as pd
import requests
import sqlite3
from urllib.parse import quote


def ej_1_cargar_datos_demograficos() -> pd.DataFrame:
    url = "https://public.opendatasoft.com/explore/dataset/us-cities-demographics/download/?format=csv&timezone=Europe/Berlin&lang=en&use_labels_for_header=true&csv_separator=%3B"
    data = pd.read_csv(url, sep=';')
    data.drop(columns=['Race', 'Count', 'Number of Veterans'], inplace=True)
    data.drop_duplicates(inplace=True)
    return data

df_demograficos = ej_1_cargar_datos_demograficos()
print(df_demograficos.head())

"""
def ej_2_cargar_calidad_aire(ciudades: set) -> pd.DataFrame:
    datos_calidad_aire = []

    for ciudad in ciudades:
        api_url = f'https://api.api-ninjas.com/v1/airquality?city={ciudad}'
        respuesta = requests.get(api_url, headers={'X-Api-Key': '+lfg1qy3mBFAuV8wSvwEaA==UzrOTgOUbVAFoQJ9'})  # Reemplaza con tu clave API real
        if respuesta.status_code == 200:
            datos = respuesta.json()
            
            datos_ciudad = {
                "city": ciudad,
                "data": datos
            }
            datos_calidad_aire.append(datos_ciudad)
        else:
            print(f"No se pudo obtener datos para la ciudad: {ciudad}, Error: {respuesta.status_code}")

  
    if datos_calidad_aire:
        df_calidad_aire = pd.DataFrame(datos_calidad_aire)
    else:
        df_calidad_aire = pd.DataFrame()
    
    return df_calidad_aire
ciudades_prueba = {'New York', 'Los Angeles', 'Chicago'}  
df_calidad_aire = ej_2_cargar_calidad_aire(ciudades_prueba)
print(df_calidad_aire.head())
"""

def ej_2_cargar_calidad_aire(ciudades: set) -> pd.DataFrame:
    datos_calidad_aire = []

    for ciudad in ciudades:
        api_url = f'https://api.api-ninjas.com/v1/airquality?city={ciudad}'
        respuesta = requests.get(api_url, headers={'X-Api-Key': '+lfg1qy3mBFAuV8wSvwEaA==UzrOTgOUbVAFoQJ9'})
        if respuesta.status_code == 200:
            datos = respuesta.json()
            overall_aqi = datos.get('overall_aqi', None)
            datos_ciudad = {"city": ciudad, "overall_aqi": overall_aqi}
            datos_calidad_aire.append(datos_ciudad)
        else:
            print(f"No se pudo obtener datos para la ciudad: {ciudad}, Error: {respuesta.status_code}")

    df_calidad_aire = pd.DataFrame(datos_calidad_aire)
    return df_calidad_aire
ciudades_prueba = {'New York', 'Los Angeles', 'Chicago'}  
df_calidad_aire = ej_2_cargar_calidad_aire(ciudades_prueba)
print(df_calidad_aire.head())

def cargar_datos_sqlite():
    df_demograficos = ej_1_cargar_datos_demograficos()

    df_calidad_aire = ej_2_cargar_calidad_aire(set(df_demograficos["City"].tolist()))

    df_calidad_aire = df_calidad_aire.dropna(subset=['overall_aqi'])

    conn = sqlite3.connect('mi_base_datos.db')

    df_demograficos.to_sql('demograficos', conn, if_exists='replace', index=False)
    df_calidad_aire.to_sql('calidad_aire', conn, if_exists='replace', index=False)

    consulta_sql = """
    SELECT d.City, d.Total Population, c.overall_aqi
    FROM demograficos d
    JOIN calidad_aire c ON d.City = c.city
    ORDER BY d.Total Population DESC
    LIMIT 10
    """

    resultado = pd.read_sql_query(consulta_sql, conn)
    print(resultado)

cargar_datos_sqlite()
