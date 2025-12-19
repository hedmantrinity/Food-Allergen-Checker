import sqlite3

# Establish DB connection and cursor
def get_data(ingredients_to_search):
    conn = sqlite3.connect('ingredients.db')
    cursor = conn.cursor()

    # Get active categories
    CATEGORY_NAME_LIST = []
    try:
        cursor.execute("SELECT category_name FROM categories WHERE active = 1")
        rows = cursor.fetchall()
        for (name,) in rows:
            CATEGORY_NAME_LIST.append(name)
    except sqlite3.Error as e:
        print("SQLite error while fetching categories:", e)

    # print(f"Active categories: {CATEGORY_NAME_LIST}")

    # TEST: Hardcoded ingredients to search for
    # ingredients_to_search = ["milk", "whey", "butter"]

    # print(f"\nSearching for: {ingredients_to_search}")

    results = []

    for category in CATEGORY_NAME_LIST:
        cursor.execute("SELECT severity FROM categories WHERE category_name == ?",(category,))
        severity = cursor.fetchone()[0]
        master_table = f"{category}_master"
        user_table = f"{category}_user"
        
        for ingredient in ingredients_to_search:
            # Search master table
            cursor.execute(f'''
                SELECT display_name, search_keywords, frequency
                FROM {master_table} 
                WHERE search_keywords LIKE ?
            ''', (f'%{ingredient}%',))
            matches = cursor.fetchall()
            
            # Search user table and add to matches
            cursor.execute(f'''
                SELECT display_name, search_keywords, frequency
                FROM {user_table}
                WHERE search_keywords LIKE ?
            ''', (f'%{ingredient}%',))
            matches += cursor.fetchall()
            
            # Check for exact match with "never" frequency
            exact_match_is_never = False
            for row in matches:
                if row[0].lower() == ingredient.lower():  # Exact display_name match
                    intolorance, allergy = row[2].split(':')
                    frequency = intolorance if severity == 0 else allergy
                    if frequency == "never":
                        exact_match_is_never = True
                        break
            
            # If exact match is "never", skip this entire ingredient
            if exact_match_is_never:
                continue
            
            # Process all matches (skip individual "never" entries)
            for row in matches:
                intolorance, allergy = row[2].split(':')
                frequency = intolorance if severity == 0 else allergy
                
                if frequency == "never":
                    continue
                
                results.append({
                    'category': category,
                    'display_name': row[0],
                    'frequency': frequency,
                    'matched_term': ingredient
                })

    # Print results
    # print(f"\n=== Found {len(results)} matches ===")
    # for result in results:
    #     print(f" '{result['display_name']}' in {result['category']} ({result['frequency']})")
    #     print(f"   Matched on: '{result['matched_term']}'")

    conn.close()
    return results

