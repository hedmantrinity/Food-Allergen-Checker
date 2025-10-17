"""
name: import_data.py
author: Trinity Hedman
created: 10/16/2025
purpose: Import data from the master excel sheets to the SQLite Database.
note: INSERT OR REPLACE updates timestamps. For minor updates, create a small
      CSV with only new ingredients. For major updates, use full CSV to 
      re-verify all data. Git tracks historical versions.
note: Save CSV file as CSV UTF-8(Comma delimited) if available. Otherwise use CSV (Comma delimited).
"""

DATABASE_NAME = "ingredients.db"
CSV_FILENAME = "milk_allergy_master_table_excel.csv"
TABLE_NAME = "dairy_master"
# Version structure: major-update.minor-update.patch
NEW_VERSION = "2.0.0"
CATEGORY_NAME = "dairy"

import sqlite3
import csv

conn = sqlite3.connect(DATABASE_NAME)
cursor = conn.cursor()

# Update version first to mark that changes are being made
cursor.execute('''
    UPDATE categories 
    SET master_version = ?, last_updated = CURRENT_TIMESTAMP 
    WHERE category_name = ?
''', (NEW_VERSION, CATEGORY_NAME))
conn.commit()

print(f"✓ Updated {CATEGORY_NAME} to version {NEW_VERSION}")

# This file opener works with the way excel is saving the file on my windows11, but may need to be changed for a different computer. File saved as CSV (Comma delimited).
with open(CSV_FILENAME, 'r', encoding='cp1252') as file:
    csv_reader = csv.reader(file)
    total_rows = 0
    successes = 0
    errors = 0
    for row in csv_reader:
        # These are all the names of the colums that have data entered. The ID and timestamp auto generate.
        display_name = row[0]
        search_keywords = row[1]
        additional_info = row[2]
        also_in_tables = row[3]
        frequency = row[4]
        added_by = row[5]

        try:
            # This inserts the data one row at a time.
            cursor.execute(f'''
                INSERT OR REPLACE INTO {TABLE_NAME} (display_name, search_keywords, additional_info, also_in_tables, frequency, added_by)
                VALUES (?, ?, ?, ?, ?, ?)''',
                (display_name, search_keywords, additional_info, also_in_tables, frequency, added_by))
            successes += 1
        except Exception as e:
            # This catches all exceptions and tells you what happened and what it is. Duplicates are no longer errors because of the REPLACE function.
            print(f"x Error importing '{display_name}': {e}")
            errors += 1
        total_rows += 1
    print(f"""
          Import Summary:
          Total rows processed: {total_rows}
          Successes: {successes}
          Errors: {errors}""")

# This makes it actually put it into the database, not just exist in memory.
conn.commit()
conn.close()

print(f"\nData committed to {DATABASE_NAME}.")