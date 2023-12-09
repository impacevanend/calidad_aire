import sqlite3


df_demograficos = ej_1_cargar_datos_demograficos()
df_calidad_aire = ej_2_cargar_calidad_aire(set(df_demograficos["City"].tolist()))


conn = sqlite3.connect('mi_base_datos.db')
df_demograficos.to_sql('demograficos', conn, if_exists='replace', index=False)
df_calidad_aire.to_sql('calidad_aire', conn, if_exists='replace', index=False)

consulta_sql = """
SELECT d.City, d.Population, c.concentration
FROM demograficos d
JOIN calidad_aire c ON d.City = c.city
ORDER BY d.Population DESC
LIMIT 10
"""

resultado = pd.read_sql_query(consulta_sql, conn)
print(resultado)