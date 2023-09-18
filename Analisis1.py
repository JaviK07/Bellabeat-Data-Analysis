# Debido a la limitación de tamaño y la falta de información demográfica, podríamos enfrentar un sesgo de muestra. 
# la muestra podria o no ser representativa de la población en su totalidad. 
# Otro problema que podríamos encontrar es que el conjunto de datos no es actual y también existe una limitación de tiempo en la encuesta (2 meses de duración).
# Es por eso que abordo el estudio de caso con un enfoque operativo.

import pandas as pd
import sqlite3

# ANALISIS 1 = CATEGORIZACION DE GRUPOS Y PORCENTAJE QUE REPRESENTA

# https://www.sciencedirect.com/science/article/pii/S0212656714002911

# Proponemos la siguiente clasificación, adaptada de la de Tudor-Locke et al.24:

# Sedentario - menos de 5.000 pasos/día.
# Algo activo - 5.000 y 9.999 pasos/día.
# Activo - 10.000 y 12.499 pasos/día.
# Muy activo - 12.500 pasos al día o más.

conn = sqlite3.connect('Data Analytics Case Study - Coursera/FitabaseSQLite3.sqlite')
cur = conn.cursor()

# Se hace consulta del promedio de pasos realizado para poder categorizar segun Sedentario, AlgoActivo, Activo, MuyActivo
query = '''
SELECT Id, ROUND(AVG(TotalSteps), 1) AS Promedio_TotalSteps, ROUND(AVG(Calories), 1) AS Promedio_Calories, ROUND(AVG(TotalDistance), 1) AS Promedio_TotalDistance
FROM dailyActivity_merged
GROUP BY Id;
'''

# Paso informacion a excel (paso no necesario, unicamente hecho para poder tener libros excel disponibles)
consulta = pd.read_sql_query(query, conn)

Promedios = 'Data Analytics Case Study - Coursera/Promedios.xlsx'
consulta.to_excel(Promedios, index=False, sheet_name='Hoja1', engine='openpyxl')

# Paso la informacion a otra DB para ir agrupando resultados de lo investigado
conn2 = sqlite3.connect('Data Analytics Case Study - Coursera/Hallazgos.sqlite')
cur2 = conn2.cursor()

df = pd.read_excel('Data Analytics Case Study - Coursera/Promedios.xlsx')

nombreTabla = 'promedios'
df.to_sql(nombreTabla, conn2, if_exists='replace', index=False)


# Se categoriza segun rango de pasos
query1 = '''
SELECT Id, Promedio_TotalSteps, Promedio_Calories, Promedio_TotalDistance,
CASE
    WHEN Promedio_TotalSteps < 5000 THEN 'Sedentario'
    WHEN Promedio_TotalSteps > 5000 AND Promedio_TotalSteps <= 9999 THEN 'Algo Activo'
    WHEN Promedio_TotalSteps > 9999 AND Promedio_TotalSteps <= 12499 THEN 'Activo'
    ELSE 'Muy Activo'
END AS Categoria
FROM promedios;
'''
consulta1 = pd.read_sql_query(query1, conn2)
consulta1.to_excel(Promedios, index=False, sheet_name='Hoja1', engine='openpyxl')
df = pd.read_excel('Data Analytics Case Study - Coursera/Promedios.xlsx')
nombreTabla = 'promedios'
df.to_sql(nombreTabla, conn2, if_exists='replace', index=False)


# Sacamos cantidad por categoria y el porcentaje que representa de la muestra y guardo en tabla nueva
query3 = '''
SELECT Categoria, 
    COUNT(*) AS Cantidad, 
    ROUND((COUNT(*) * 1.0) / (SELECT COUNT(*) FROM promedios), 2) AS PorcentajeDelTotal
FROM promedios
GROUP BY Categoria;
'''

tablaNueva = 'categorias_porcentaje'
df2 = pd.read_sql_query(query3, conn2)
df2.to_sql(tablaNueva, conn2, if_exists='replace', index=False)


