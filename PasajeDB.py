# Script para cargar los archivos CSV a SQLite3 para manejo de analisis ya que algunos archivos CSV del DataSet superan el tope de celdas

import pandas as pd
import sqlite3
from pathlib import Path


# Lista de nombres de archivos CSV
csv_files = ['Data Analytics Case Study - Coursera/Fitabase DataSet/dailyActivity_merged.csv',
             'Data Analytics Case Study - Coursera/Fitabase DataSet/dailyCalories_merged.csv',
             'Data Analytics Case Study - Coursera/Fitabase DataSet/dailyIntensities_merged.csv',
             'Data Analytics Case Study - Coursera/Fitabase DataSet/dailySteps_merged.csv',
             'Data Analytics Case Study - Coursera/Fitabase DataSet/heartrate_seconds_merged.csv',
             'Data Analytics Case Study - Coursera/Fitabase DataSet/hourlyCalories_merged.csv',
             'Data Analytics Case Study - Coursera/Fitabase DataSet/hourlyIntensities_merged.csv',
             'Data Analytics Case Study - Coursera/Fitabase DataSet/hourlySteps_merged.csv',
             'Data Analytics Case Study - Coursera/Fitabase DataSet/minuteCaloriesNarrow_merged.csv',
             'Data Analytics Case Study - Coursera/Fitabase DataSet/minuteCaloriesWide_merged.csv',
             'Data Analytics Case Study - Coursera/Fitabase DataSet/minuteIntensitiesNarrow_merged.csv',
             'Data Analytics Case Study - Coursera/Fitabase DataSet/minuteIntensitiesWide_merged.csv',
             'Data Analytics Case Study - Coursera/Fitabase DataSet/minuteMETsNarrow_merged.csv',
             'Data Analytics Case Study - Coursera/Fitabase DataSet/minuteSleep_merged.csv',
             'Data Analytics Case Study - Coursera/Fitabase DataSet/minuteStepsNarrow_merged.csv',
             'Data Analytics Case Study - Coursera/Fitabase DataSet/minuteStepsWide_merged.csv',
             'Data Analytics Case Study - Coursera/Fitabase DataSet/sleepDay_merged.csv',
             'Data Analytics Case Study - Coursera/Fitabase DataSet/weightLogInfo_merged.csv'
             ]

# Crear una conexión a la base de datos SQLite
db_connection = sqlite3.connect('Data Analytics Case Study - Coursera/FitabaseSQLite3.sqlite')

for csv_file in csv_files:
    df = pd.read_csv(csv_file)
    # Obtengo el nombre de la tabla (utilizo el nombre del archivo origen CSV)
    table_name = Path(csv_file).stem

    # Guardar el DataFrame en la base de datos
    df.to_sql(table_name, db_connection, index=False, if_exists='replace')

# Cerrar la conexión a la base de datos
db_connection.close()










