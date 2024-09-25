import pandas as pd
import sqlite3

# Create connection to SQLite db
conn = sqlite3.connect('stroke_predict.db')

# Create Pandas DataFrame
df = pd.read_csv('stroke_predict.csv')

# Get column names to know what to query
print('\n-----Column Names------\n')
print(df.columns)

# Load data to SQLite db
df.to_sql('stroke_prediction', conn, if_exists='replace', index=False)

# Query 1: Select all records based on a specific filter of your choice 
query_1 = 'SELECT * FROM stroke_prediction WHERE residence_type = "Rural"'
query_1_results = pd.read_sql(query_1, conn)
print('\n-----QUERY 1: Records of those living in rural areas------\n')
print(query_1_results)

# Query 2: Count the number of records that meet a certain condition
query_2 = 'SELECT COUNT(*) FROM stroke_prediction WHERE residence_type = "Rural" AND stroke = 1'
query_2_results = pd.read_sql(query_2, conn)
print('\n-----QUERY 2: Total records of those living in rural areas and had stroke(s) before------\n')
print(query_2_results)

# Query 3: Group the data by a specific column and calculate a summary statistic (e.g., average, sum, count) for each group.
query_3 = """
    SELECT residence_type, COUNT(stroke) total_stroke, AVG(bmi) average_bmi
    FROM stroke_prediction
    WHERE stroke = 1
    GROUP BY residence_type
"""
query_3_results = pd.read_sql(query_3, conn)
print('\n-----QUERY 3: Data grouped by residence type------\n')
print(query_3_results)

# Query 4: Sort the records based on a numerical or categorical field and return a limited set of results (e.g., top 5 records).
query_4 = """
    SELECT * 
    FROM stroke_prediction
    ORDER BY avg_glucose_level DESC
    LIMIT 10
"""
print('\n-----QUERY 4: Data sorted by average glucose level------\n')
query_4_results = pd.read_sql(query_4, conn)
print(query_4_results)