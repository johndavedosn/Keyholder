import sqlite3

def add_row(row_data: list, cur: sqlite3.Cursor):
    cur.execute('''INSERT INTO keys(key_name, key_value) VALUES (?, ?);''', row_data)

def remove_row(row_name: str, cur: sqlite3.Cursor):
    cur.execute(f'''DELETE FROM keys WHERE key_name=\"{row_name}\";''')
        