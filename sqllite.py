import sqlite3

# Connect to the database. If it does not exist, it will be created.
conn = sqlite3.connect('forum.db')

c = conn.cursor()

# Create the 'posts' table
c.execute('''
    CREATE TABLE posts (
        id INTEGER PRIMARY KEY,
        title TEXT NOT NULL,
        content TEXT NOT NULL,
        author TEXT NOT NULL
    )
''')

# Commit the changes and close the connection
conn.commit()
conn.close()
