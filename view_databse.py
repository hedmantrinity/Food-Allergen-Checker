import sqlite3

conn = sqlite3.connect('ingredients.db')  # or 'ingredients.db' if you switched
cursor = conn.cursor()

# Get list of all tables
cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
tables = cursor.fetchall()

print("Tables in database:")
for table in tables:
    print(f"  - {table[0]}")

conn.close()