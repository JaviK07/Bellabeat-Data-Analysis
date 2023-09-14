import pandas as pd
import sqlite3

conn = sqlite3.connect('Data Analytics Case Study - Coursera/Hallazgos.sqlite')
cur = conn.cursor()

query1 = '''
SELECT * FROM categorias_porcentaje
'''
query2 = '''
SELECT * FROM PasosPorDia
'''

query3 = '''
SELECT * FROM promedios
'''

query4 = '''
SELECT * FROM sueño
'''

df1 = pd.read_sql_query(query1, conn)
df2 = pd.read_sql_query(query2, conn)
df3 = pd.read_sql_query(query3, conn)
df4 = pd.read_sql_query(query4, conn)

df1.to_excel('Data Analytics Case Study - Coursera/Porcentaje de Categorias.xlsx', index=False)
df2.to_excel('Data Analytics Case Study - Coursera/Pasos por Dia.xlsx', index=False)
df3.to_excel('Data Analytics Case Study - Coursera/Promedios.xlsx', index=False)
df4.to_excel('Data Analytics Case Study - Coursera/Sueño.xlsx', index=False)

print("Datos exportados exitosamente a Excel.")