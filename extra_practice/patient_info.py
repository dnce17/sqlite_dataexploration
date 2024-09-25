import pandas as pd
import sqlite3

# Create connection to SQLite db
conn = sqlite3.connect('patient_info.db')

# Create Pandas DataFrame
df = pd.read_csv('patient_info.csv')
print(df.columns)

# Load data to SQLite db
df.to_sql('patient_info', conn, if_exists='replace', index=False)

# Getting unique values from categories of interest
med_conditions = df['Medical Condition'].unique()
ins = df['Insurance Provider'].unique()

print(med_conditions)
print(ins)

# Query 1: Select all records based on a specific filter of your choice 
query_1 = 'SELECT UPPER(name) AS "Name", age, "Medical Condition", "Insurance Provider" AS "Insurance" FROM patient_info'
query_1_results = pd.read_sql(query_1, conn)
print(query_1_results)

# Query 2: Count the number of records that meet a certain condition
query_2 = 'SELECT COUNT("Insurance Provider") FROM patient_info WHERE "Medical Condition" = "Cancer"'
query_2_results = pd.read_sql(query_2, conn)
print(query_2_results)

# Query 3: Group the data by a specific column and calculate a summary statistic (e.g., average, sum, count) for each group.
query_3 = """
    SELECT "Insurance Provider" AS ins, COUNT("Medical Condition") AS cancer 
    FROM patient_info 
    WHERE "Medical Condition" = \'Cancer\' 
    GROUP BY ins
"""
query_3_results = pd.read_sql(query_3, conn)
print(query_3_results)

# Query 4: Sort the records based on a numerical or categorical field and return a limited set of results (e.g., top 5 records).
query_4 = """
    SELECT "Name", ROUND("Billing Amount", 2) AS "Billing Amt", "Medical Condition", "Admission Type", "Test Results" 
    FROM patient_info 
    WHERE NOT "Medical Condition" = 'Cancer'
    ORDER BY "Billing Amount" DESC 
    LIMIT 10
"""
query_4_results = pd.read_sql(query_4, conn)
print(query_4_results)