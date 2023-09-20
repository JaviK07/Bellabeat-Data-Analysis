# Questions:
# 1. What are some trends in smart device usage?
# 2. How could these trends apply to Bellabeat customers?
# 3. How could these trends help influence Bellabeat marketing strategy?

import pandas as pd
import sqlite3

# Conexión a la base de datos SQLite
conn = sqlite3.connect('Data Analytics Case Study - Coursera/FitabaseSQLite3.sqlite')
cursor = conn.cursor()


# Se normalizan valores de la DB

# Query 1
query1 = '''
SELECT Id, ActivityDate, TotalSteps, ROUND(CAST(TotalDistance AS DECIMAL(10, 1)), 1) AS TotalDistance, ROUND(CAST(TrackerDistance AS DECIMAL(10, 1)), 1) AS TrackerDistance, ROUND(CAST(VeryActiveDistance AS DECIMAL(10, 1)),1) AS VeryActiveDistance, SedentaryActiveDistance, FairlyActiveMinutes, LightlyActiveMinutes, SedentaryMinutes, Calories
FROM dailyActivity_merged;
'''

df1 = pd.read_sql_query(query1, conn)
df1.to_sql('dailyActivity_merged', conn, index=False, if_exists='replace')
conn.commit()

# Query 2
query2 = '''
SELECT Id, ActivityDay, SedentaryMinutes, LightlyActiveMinutes, FairlyActiveMinutes, VeryActiveMinutes, SedentaryActiveDistance, ROUND(CAST(LightActiveDistance AS DECIMAL(10, 1)),1) AS LightActiveDistance, ROUND(CAST(ModeratelyActiveDistance AS DECIMAL(10, 1)),1) AS ModeratelyActiveDistance, ROUND(CAST(VeryActiveDistance AS DECIMAL(10, 1)),1) AS VeryActiveDistance
FROM dailyIntensities_merged;
'''

df2 = pd.read_sql_query(query2, conn)
df2.to_sql('dailyIntensities_merged', conn, index=False, if_exists='replace')
conn.commit()

# Query 3

query3 = '''
SELECT Id, ActivityHour, TotalIntensity, ROUND(CAST(AverageIntensity AS DECIMAL(10, 1)), 2) AS AverageIntensity
FROM hourlyIntensities_merged
'''
df3 = pd.read_sql_query(query3, conn)
df3.to_sql('hourlyIntensities_merged', conn, index=False, if_exists='replace')

# Query 4

query4 = '''
SELECT Id, ActivityMinute, ROUND(CAST(Calories AS DECIMAL(10,1)), 1) AS Calories
FROM minuteCaloriesNarrow_merged;
'''
df4 = pd.read_sql_query(query4, conn)
df4.to_sql('minuteCaloriesNarrow_merged', conn, index=False, if_exists='replace')

# Query 5

query5 = '''
SELECT Id, Date, ROUND(CAST(WeightKg AS DECIMAL(10,1)), 1) AS WeightKg, ROUND(CAST(WeightPounds AS DECIMAL(10,1)), 1) AS WeightPounds, ROUND(CAST(BMI AS DECIMAL(10,1)), 1) AS BMI
FROM weightLogInfo_merged
'''
df5 = pd.read_sql_query(query5, conn)
df5.to_sql('weightLogInfo_merged', conn, index=False, if_exists='replace')

query6 ='''
SELECT Id, SUBSTR(SleepDay, 0, 10) AS Date, TotalSleepRecords ,TotalMinutesAsleep, TotalTimeInBed
FROM sleepDay_merged
'''

df6 = pd.read_sql_query(query6, conn)
df6.to_sql('sleepDay_merged', conn, index=False, if_exists='replace')