"""
name: create_tables.py
author: Trinity Hedman
created: 10/16/2025
purpose: Create master and user tables for allergen categories with standardized structure.
"""

DATABASE_NAME = "ingredients.db"
CATEGORY_NAME = "dairy"  # Change this for each allergen category (gluten, soy, etc.)

import sqlite3

conn = sqlite3.connect(DATABASE_NAME)
cursor = conn.cursor()

# Create master table (with UNIQUE constraint on display_name)
cursor.execute(f'''
    CREATE TABLE IF NOT EXISTS {CATEGORY_NAME}_master (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        display_name TEXT NOT NULL UNIQUE,
        search_keywords TEXT NOT NULL,
        additional_info TEXT,
        also_in_tables TEXT,
        frequency TEXT NOT NULL DEFAULT 'always:always',
        added_by TEXT NOT NULL,
        date_added TEXT DEFAULT CURRENT_TIMESTAMP
    )
''')

# Create user table (no UNIQUE constraint on display_name)
cursor.execute(f'''
    CREATE TABLE IF NOT EXISTS {CATEGORY_NAME}_user (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        display_name TEXT NOT NULL,
        search_keywords TEXT NOT NULL,
        additional_info TEXT,
        also_in_tables TEXT,
        frequency TEXT NOT NULL DEFAULT 'always:always',
        added_by TEXT NOT NULL,
        date_added TEXT DEFAULT CURRENT_TIMESTAMP
    )
''')

conn.commit()
conn.close()

print(f"✓ {CATEGORY_NAME}_master table created successfully!")
print(f"✓ {CATEGORY_NAME}_user table created successfully!")