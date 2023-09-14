# ¿La distancia recorrida se relaciona de alguna manera con las calorías quemadas? 

# Análisis de promedio:

# Ventajas: Al calcular el promedio de calorías quemadas y distancia realizada para todos los individuos,
# se obtiene una visión general de la relación promedio entre estas dos variables en el conjunto de datos.

# Desventajas: esto puede ocultar variaciones individuales significativas. 
# Si existen diferencias importantes en la forma en que diferentes personas responden a la distancia recorrida en términos de calorías quemadas, el promedio podría no ser representativo de esas diferencias.


# Sabiendo ventajas y desventajas, comienzo a analizar utilizando el promedio por individuo ya que estoy interesado en ver la relación entre calorías quemadas y distancia recorrida en el grupo en su conjunto

# Se debe instalar Scipy (pip install scipy) - tambien numpy y pandas
import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import pearsonr

conn = sqlite3.connect('Data Analytics Case Study - Coursera/Hallazgos.sqlite')
cur = conn.cursor()


query = '''
SELECT Promedio_Calories, Promedio_TotalDistance
FROM promedio_pasos
'''
df = pd.read_sql_query(query, conn)

# Corrige el nombre de las columnas
calorias_quemadas = df['Promedio_Calories']
distancia = df['Promedio_TotalDistance']

plt.figure(figsize=(10, 6))
plt.scatter(distancia, calorias_quemadas, alpha=0.5)
plt.title('Distancia vs Calorias Quemadas')
plt.xlabel('Distancia (KM)')
plt.ylabel('Calorias Quemadas')
plt.grid(True)

# Se calcula la pendiente de la regresion lineal (funcion)
coefficientes = np.polyfit(distancia, calorias_quemadas, 1)
# se 'crea' la funcion polinomica de grado 1 (poly-1Dimension)
polinomio = np.poly1d(coefficientes)

# Dibujo la línea de regresión
plt.plot(distancia, polinomio(distancia), color='red', linestyle='solid', label='Regresión Lineal')
plt.legend()
plt.show()
# La grafica nos sugiere una correlacion positiva (pendiente positiva), por lo que calculamos el grado de correlacion numerico.

correlacion = df['Promedio_Calories'].corr(df['Promedio_TotalDistance'])
print(correlacion)

# Al verificar un grado moderado/positivo de correlacion, realizo una prueba estadistica (prueba hipotesis de correlacion)
# para ver si ay una correlacion estadisticamente significativa (es decir no sea resultado de azar)

correlacion, p_value = pearsonr(df['Promedio_TotalDistance'], df['Promedio_Calories'])

alpha = 0.05
if p_value < alpha:
    print('Correlacion Significativa')
else:
    print('Sin evidencia')

# Se afirma la correlacion entre distancia/calorias









