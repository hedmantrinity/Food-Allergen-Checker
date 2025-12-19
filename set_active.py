import sqlite3

def set_active(CATEGORY):
    DATABASE = 'ingredients.db'
    # Open a short-lived connection for this operation
    with sqlite3.connect(DATABASE) as conn:
        cursor = conn.cursor()
        cursor.execute('''
            UPDATE categories 
            SET active = 1 
            WHERE category_name = ?
        ''', (CATEGORY,))
        conn.commit()

    print(f"✓ {CATEGORY} category set to active")
