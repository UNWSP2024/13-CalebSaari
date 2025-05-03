# This program will utilize the SQLite database.

import sqlite3


def display_cities():
    # Establish a connection to the SQLite database
    connection = sqlite3.connect('cities.db')

    # Create a cursor object to interact with the database
    cursor = connection.cursor()

    # SQL query to select all data from the cities table
    query = "SELECT * FROM cities"

    try:
        # Execute the query
        cursor.execute(query)

        # Fetch all results from the executed query
        cities = cursor.fetchall()

        # Display the results
        print("City Data:")
        print("ID\tName\t\tCountry\t\tPopulation")
        print("-" * 40)
        for city in cities:
            print(f"{city[0]}\t{city[1]}\t{city[2]}\t{city[3]}")

    except sqlite3.Error as e:
        print(f"An error occurred: {e}")

    finally:
        # Close the cursor and connection
        cursor.close()
        connection.close()


# Call the function to display city data
display_cities()

# Caleb Saari 5/02/25 Wk13 Program 2 Cities Database