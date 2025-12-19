import sqlite3

#Connect to the database (creates file if it doesn't exist)
conn = sqlite3.connect('ingredients.db')
cursor = conn.cursor()

cursor.execute('ALTER TABLE categories ADD COLUMN severity INTEGER DEFAULT 1')
conn.commit()
conn.close()