"""
name: reset_dairy_tables.py
author: Trinity Hedman
created: 10/16/2025
purpose: Drop and recreate dairy tables with corrected structure.
"""

DATABASE_NAME = "ingredients.db"
CATEGORY_NAME = "dairy"

import sqlite3

conn = sqlite3.connect(DATABASE_NAME)
cursor = conn.cursor()

# Drop existing tables
cursor.execute(f'DROP TABLE IF EXISTS {CATEGORY_NAME}_master')
cursor.execute(f'DROP TABLE IF EXISTS {CATEGORY_NAME}_user')

print(f"✓ Dropped old {CATEGORY_NAME}_master table")
print(f"✓ Dropped old {CATEGORY_NAME}_user table")

conn.commit()
conn.close()

print("\nTables reset. Now run create_tables.py to recreate them.")