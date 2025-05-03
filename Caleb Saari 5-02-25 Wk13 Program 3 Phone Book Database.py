# This preparation involves creating a structured database that can store contact information.

import sqlite3

def create_phone_book_db(db_name='phone_book.db'):
    # Connect to the SQLite database (or create it if it doesn't exist)
    connection = sqlite3.connect(db_name)
    cursor = connection.cursor()

    # Create a table for the phone book
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS contacts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            phone_number TEXT NOT NULL UNIQUE
        )
    ''')

    # Commit the changes and close the connection
    connection.commit()
    connection.close()
    print(f"Phone book database '{db_name}' is ready for use.")

# Call the function to create the database
create_phone_book_db()

# Caleb Saari 5/02/25 Wk13 Program 3: Phone Book Database