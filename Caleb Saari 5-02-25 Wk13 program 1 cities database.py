# The objective is to create a structured database that can be easily queried and manipulated.

import sqlite3

# Connect to the SQLite database (or create it if it doesn't exist)
conn = sqlite3.connect('cities.db')

# Create a cursor object using the cursor() method
cursor = conn.cursor()

# Create a table for cities
cursor.execute('''
CREATE TABLE IF NOT EXISTS cities (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    country TEXT NOT NULL,
    population INTEGER,
    area REAL
)
''')

# Commit the changes and close the connection
conn.commit()
conn.close()

# Caleb Saari 5/02/25 Wk13 Porgram 1: Cities Database