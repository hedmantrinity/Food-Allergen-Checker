"""
name: add_category.py
author: Trinity Hedman
created: 10/16/2025
purpose: Add a new allergen category to the categories metadata table.
"""

DATABASE_NAME = "ingredients.db"
CATEGORY_NAME = "dairy"
DISPLAY_NAME = "Dairy Ingredients"
INITIAL_VERSION = "1.0.0"

import sqlite3

conn = sqlite3.connect(DATABASE_NAME)
cursor = conn.cursor()

cursor.execute('''
    INSERT INTO categories (category_name, display_name, master_version)
    VALUES (?, ?, ?)
''', (CATEGORY_NAME, DISPLAY_NAME, INITIAL_VERSION))

conn.commit()
conn.close()

print(f"✓ {DISPLAY_NAME} category added as '{CATEGORY_NAME}' (version {INITIAL_VERSION})!")