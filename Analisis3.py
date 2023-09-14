# MUESTRA DE SUEÑO CORRESPONDIENTE A 24 USUARIOS DE LA APP, COMO SE MENCIONA EN ANALISIS1 NOS ENCONTRAMOS CON UN SESGO DE MUESTRA,
# POR LO QUE LOS DATOS RECOLECTADOS Y ANALISIS SUBYACENTE PODRÍA NO REFLEJAR LA REALIDAD DE LA POBLACION EN GENERAL.


# ¿Afecta el sueño a la distancia recorrida? 

# Referencia: chrome-extension://efaidnbmnnnibpcajpcglclefindmkaj/https://www.redalyc.org/pdf/337/33720206.pdf

# Sueño Corto < 5 horas y media por dia
# Sueño Intermedio 7 < x < 8
# Sueño Largo > 9 horas por dia

import sqlite3
import pandas as pd

conn = sqlite3.connect('Data Analytics Case Study - Coursera/FitabaseSQLite3.sqlite')
cur = conn.cursor()


# Como nos encontramos con una muestra mas reducida a la inicial (24 ids), vamos a utilizar la clausula INNER JOIN para que devuelva los registros de aquellos Ids que se encuentren tanto en dailyActivity como sleepDay-
query= '''
SELECT s.Id,
       ROUND(AVG(s.TotalMinutesAsleep / 60.0), 1) AS TotalHorasDormidas,
       CASE
           WHEN AVG(s.TotalMinutesAsleep) <= 330 THEN 'Sueño Corto'
           WHEN AVG(s.TotalMinutesAsleep) > 330 AND AVG(s.TotalMinutesAsleep) <= 480 THEN 'Sueño Intermedio'
           ELSE 'Sueño Largo'
       END AS Tipo_de_Sueño,
       ROUND(AVG(d.TotalDistance), 1) AS Promedio_Distancia
FROM sleepDay_merged s
INNER JOIN dailyActivity_merged d ON s.Id = d.Id
WHERE s.Id IN (SELECT Id FROM dailyActivity_merged)
GROUP BY s.Id;
'''

conn1 = sqlite3.connect('Data Analytics Case Study - Coursera/Hallazgos.sqlite')
cur1 = conn1.cursor()

tablaNueva = 'sueño'
df2 = pd.read_sql_query(query, conn)
df2.to_sql(tablaNueva, conn1, if_exists='replace', index=False)

