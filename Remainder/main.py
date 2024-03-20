'''Replace 'example.db' with the path to your SQL file. This code assumes an SQLite database, but if you're dealing with a different SQL database system (like MySQL, PostgreSQL, etc.), you'd need to use the appropriate library for that database.

Remember to handle exceptions and errors appropriately, especially when dealing with file I/O and database connections.'''

import sqlite3

# Connect to the SQLite database file
conn = sqlite3.connect('example.db')

# Create a cursor object to execute SQL queries
cursor = conn.cursor()

# Execute a SQL query
cursor.execute("SELECT * FROM my_table")

# Fetch results, if any
rows = cursor.fetchall()

# Print the results
for row in rows:
    print(row)

# Close the cursor and the connection
cursor.close()
conn.close()
