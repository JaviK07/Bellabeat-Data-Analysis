
import pandas as pd
import sqlite3

# Cantidad de pasos en promedio de toda la muestra segun dia de semana

conn = sqlite3.connect('Data Analytics Case Study - Coursera/FitabaseSQLite3.sqlite')
cur = conn.cursor()

conn1 = sqlite3.connect('Data Analytics Case Study - Coursera/Hallazgos.sqlite')
cur1 = conn.cursor()

query = '''
SELECT
    CASE
        WHEN strftime('%w', Date, 'start of day') = '0' THEN 'Domingo'
        WHEN strftime('%w', Date, 'start of day') = '1' THEN 'Lunes'
        WHEN strftime('%w', Date, 'start of day') = '2' THEN 'Martes'
        WHEN strftime('%w', Date, 'start of day') = '3' THEN 'Miércoles'
        WHEN strftime('%w', Date, 'start of day') = '4' THEN 'Jueves'
        WHEN strftime('%w', Date, 'start of day') = '5' THEN 'Viernes'
        WHEN strftime('%w', Date, 'start of day') = '6' THEN 'Sábado'
        ELSE 'Desconocido'
    END AS DiaSemana,
    ROUND(AVG(StepTotal), 1) AS PromedioPasos
FROM
    dailySteps_merged
WHERE
    Date BETWEEN strftime('%Y-%m-%d', '2016-04-12') AND strftime('%Y-%m-%d', '2016-05-12')
GROUP BY
    strftime('%w', Date, 'start of day')
ORDER BY
    strftime('%w', Date, 'start of day');
'''

df = pd.read_sql_query(query, conn)


tablaNueva = 'PasosPorDia'
df.to_sql(tablaNueva, conn1, if_exists='replace', index=False)


