import sqlite3

#Connect to the database (creates file if it doesn't exist)
conn = sqlite3.connect('ingredients.db')
cursor = conn.cursor()

#Create the categories table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS categories(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        category_name TEXT NOT NULL UNIQUE,
        display_name TEXT NOT NULL,
        installed INTEGER NOT NULL DEFAULT 0,
        active INTEGER NOT NULL DEFAULT 0,
        master_version TEXT,
        last_updated TEXT DEFAULT CURRENT_TIMESTAMP
    )           
''')

#Save the changes
conn.commit()

#Close the connection
conn.close()

#Tells me it didn't  hit an error before the end.
print("Categories table created successfully!")