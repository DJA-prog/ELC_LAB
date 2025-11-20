import sqlite3

# create connection to the database (or create it if it doesn't exist)

conn = sqlite3.connect('components_users.db')
cursor = conn.cursor()


# create a sample table
cursor.execute('''
CREATE TABLE IF NOT EXISTS components (
            id INTEGER PRIMARY KEY,
            identifier TEXT NOT NULL,
            description TEXT,
            price FLOAT DEFAULT 0.0,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS categories (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            description TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS component_category (
            component_id INTEGER,
            category_id INTEGER,
            PRIMARY KEY (component_id, category_id),
            FOREIGN KEY (component_id) REFERENCES components(id),
            FOREIGN KEY (category_id) REFERENCES categories(id)
    )
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            number TEXT UNIQUE,
            email TEXT UNIQUE,
            balance FLOAT DEFAULT 0.0,
            phone TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
''')

# commit changes and close the connection
conn.commit()
conn.close()