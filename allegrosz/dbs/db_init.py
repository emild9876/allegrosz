import os

import sqlite3


db_abs_path = os.path.abspath(os.path.dirname(__file__))
db_path = os.path.join(db_abs_path, '..', 'allegrosz.db')


conn = sqlite3.connect(db_path)
c = conn.cursor()

c.execute('DROP TABLE IF EXISTS item')
c.execute('DROP TABLE IF EXISTS category')
c.execute('DROP TABLE IF EXISTS subcategory')
c.execute('DROP TABLE IF EXISTS comment')

c.execute('''CREATE TABLE category (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT
)''')

c.execute('''CREATE TABLE subcategory (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    category_id INTEGER,
    FOREIGN KEY (category_id) REFERENCES category (id)
)''')

c.execute('''CREATE TABLE item(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT,
    description TEXT,
    price REAL,
    image TEXT,
    category_id INTEGER,
    subcategory_id INTEGER,
    FOREIGN KEY (category_id) REFERENCES category (id),
    FOREIGN KEY (subcategory_id) REFERENCES subcategory (id)
)''')

c.execute('''CREATE TABLE comment (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    content TEXT,
    item_id INTEGER,
    FOREIGN KEY (item_id) REFERENCES item (id)
)''')

categories = [
    ('Food',),
    ('Instruments',),
    ('Drugs',)
]

c.executemany('INSERT INTO category (name) VALUES (?)', categories)

subcategories = [
    ('Fruits', 1),
    ('Vegetables', 1),
    ('Dairy', 1),
    ('Guitars', 2),
    ('Drums', 2),
    ('Flutes', 2),
    ('Painkillers', 3),
    ('Antidepressants', 3),
    ('SleepingPills', 3)
]

c.executemany('INSERT INTO subcategory (name, category_id) VALUES (?,?)', subcategories)

items = [
    ('Bananas', '1 kg of fresh bananas', 6.50, '', 1, 1),
    ('Milk', 'Fresh milk from straight cow', 3.49, '', 1, 3),
    ('Ibuprom', 'na ból dupy', 12.99, '', 3, 7),
    ('Marihuanen', 'A po co to komu?', 6.66, '', 3, 8)
]

c.executemany('INSERT INTO item (title, description, price, image, category_id, subcategory_id) VALUES (?,?,?,?,?,?)',
              items)

conn.commit()
conn.close()

print('Database is created and initialised.')
