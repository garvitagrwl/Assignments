import sqlite3

# 1. Create database (db1.db)
conn = sqlite3.connect("db_asgn.db")


conn.execute('''
CREATE TABLE  users (
    usid INTEGER PRIMARY KEY AUTOINCREMENT,
    usnm TEXT,
    pass TEXT
)
''')

conn.execute('''
CREATE TABLE products (
    pid INTEGER PRIMARY KEY AUTOINCREMENT,
    pname TEXT,
    price INTEGER
)
''')


conn.execute('''
INSERT INTO users (usnm, pass)
VALUES ("garvit", "@123"),
       ("gauri", "1234"),
       ("neha", "4567")
''')

conn.execute('''
INSERT INTO products (pname, price)
VALUES ("Laptop", 50000),
       ("Mouse", 800),
       ("Keyboard", 1200)
''')

conn.commit()


print("\n---------All Users---------")
data = conn.execute("SELECT * FROM users")
for x in data:
    print(x)

print("\n--- All Products ---")
data = conn.execute("SELECT * FROM products")
for x in data:
    print(x)

print("Updation")
conn.execute("UPDATE users SET usnm = 'updated_user' WHERE usid = 2")
conn.commit()
data = conn.execute("SELECT * FROM users")
for x in data:
    print(x)

i = int(input("\nEnter user id to delete: "))
conn.execute(f"DELETE FROM users WHERE usid = {i}")
conn.commit()

print("\n--- Remaining Users ---")
data = conn.execute("SELECT * FROM users")
for x in data:
    print(x)

conn.close()
