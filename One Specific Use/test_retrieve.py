import sqlite3
from add_category import add_category
from random import randint
from set_active import set_active
from retrieve_data import test_1

conn = sqlite3.connect('ingredients.db')
cursor = conn.cursor()

print("=== STEP 1: Inserting test data ===")

test_catetories = ["test_1",'test_2','test_3','test_4','test_5','test_6','test_7','test_8','test_9','test_10']
for i in test_catetories:
    add_category(i)
    print(f'{i} category added.')
    value = randint(0,1)
    if value == 1:
        set_active(i)
    
test_1()
# test_catetories = ['test_1','test_2','test_3','test_4']
skip = input("Press Enter to Continue: ")
print("=== STEP 2: Cleaning up test data ===")
for i in test_catetories:
    cursor.execute('''
        DELETE FROM categories 
        WHERE category_name = ?
    ''', (i,))
    conn.commit()
    print(f'{i} category removed.')

conn.close()

