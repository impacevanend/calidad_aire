import pandas as pd
import requests

def ej_2_cargar_calidad_aire(ciudades: set) -> pd.DataFrame:
    datos_calidad_aire = []

    for ciudad in ciudades:
        # Asegúrate de tener una clave API válida para la API https://api-ninjas.com/api/airquality
        headers = {"X-Api-Key": "+lfg1qy3mBFAuV8wSvwEaA==UzrOTgOUbVAFoQJ9"}
        respuesta = requests.get(f"https://api-ninjas.com/api/airquality?city={ciudad}", headers=headers)
        if respuesta.status_code == 200:
            datos = respuesta.json()
            # Procesar los datos y añadir a la lista
            # Supongamos que extraemos el elemento 'concentration'
            datos_ciudad = {
                "city": ciudad,
                "CO": datos['CO'],
                "NO2": datos['NO2'],
                "O3": datos['O3'],
                "SO2": datos['SO2'],
                "PM2.5": datos['PM2.5'],
                "PM10": datos['PM10'],
                "overall_aqi": datos['overall_aqi']
            }
            datos_calidad_aire.append(datos_ciudad)

    # Crear DataFrame con los datos recopilados
    df_calidad_aire = pd.DataFrame(datos_calidad_aire)
    return df_calidad_aire