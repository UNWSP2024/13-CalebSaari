# The program will utilize a SQLite database to store the phone book entries, ensuring that data
# is persistent across sessions. Users will interact with the program through a command-line
# interface.

import sqlite3

# Connect to the SQLite database (or create it if it doesn't exist)
conn = sqlite3.connect('phonebook.db')
cursor = conn.cursor()

# Create a table for the phone book if it doesn't already exist
cursor.execute('''
CREATE TABLE IF NOT EXISTS phonebook (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    phone TEXT NOT NULL
)
''')
conn.commit()


def read_entries():
    cursor.execute("SELECT * FROM phonebook")
    entries = cursor.fetchall()
    for entry in entries:
        print(f"ID: {entry[0]}, Name: {entry[1]}, Phone: {entry[2]}")


def update_entry(entry_id, new_name, new_phone):
    cursor.execute("UPDATE phonebook SET name = ?, phone = ? WHERE id = ?", (new_name, new_phone, entry_id))
    conn.commit()
    print("Entry updated successfully.")


def delete_entry(entry_id):
    cursor.execute("DELETE FROM phonebook WHERE id = ?", (entry_id,))
    conn.commit()
    print("Entry deleted successfully.")


def main():
    while True:
        print("\nPhone Book Menu:")
        print("1. Read Entries")
        print("2. Update Entry")
        print("3. Delete Entry")
        print("4. Exit")

        choice = input("Select an option (1-4): ")

        if choice == '1':
            read_entries()
        elif choice == '2':
            entry_id = int(input("Enter the ID of the entry to update: "))
            new_name = input("Enter the new name: ")
            new_phone = input("Enter the new phone number: ")
            update_entry(entry_id, new_name, new_phone)
        elif choice == '3':
            entry_id = int(input("Enter the ID of the entry to delete: "))
            delete_entry(entry_id)
        elif choice == '4':
            break
        else:
            print("Invalid option. Please try again.")


if __name__ == "__main__":
    main()

# Close the database connection
conn.close()

# Caleb Saari 5/02/25 Wk13 Program 4: Phone Book Database