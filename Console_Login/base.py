import sqlite3
import hashlib
import getpass
import re

def is_valid_input(value):
    return re.match("^[A-Za-z0-9]+$", value) is not None




conn = sqlite3.connect("user_info.db")

# conn.execute("DROP TABLE IF EXISTS users")

# conn.execute('''
# CREATE TABLE users (
#     usid INTEGER PRIMARY KEY AUTOINCREMENT,
#     usnm TEXT NOT NULL,
#     cid TEXT UNIQUE,
#     pass TEXT NOT NULL
# )
# ''')
# conn.commit()
# conn.execute('''
# CREATE TABLE IF NOT EXISTS user_status (
#     usid INTEGER PRIMARY KEY,
#     status TEXT NOT NULL,
#     FOREIGN KEY (usid) REFERENCES users(usid)
# )
# ''')
# conn.commit()

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()


def register():
        while True:
            name = input("Enter your name: ").strip()
            if not name:
                print("Name cannot be blank.")
                continue
            if not is_valid_input(name):
                print("Name must not contain special characters.")
                continue
            break

        while True:
            cid = input("Enter your college id:").strip()
            if not cid:
                print("Please fill this blank.")
                continue
            if not is_valid_input(name):
                print("ID must not contain special characters.")
                continue
            if len(cid) != 6:
                print("College ID must be exactly 6 characters.")
                continue
            break
        while True:
            pas = getpass.getpass("Enter your password: ")
            if pas:
                break
            print("Please fill this blank .")

        while True:
            cpass = getpass.getpass("Enter your confirm password").strip()
            if not cpass:
             print("Please fill this blank .")
             continue
            if cpass != pas:
                print(" Passwords do not match. Try again.")
                continue
            break
        hashed_pass = hash_password(pas)

        try:
            conn.execute("INSERT INTO users (usnm, cid, pass) VALUES (?, ?, ?)", (name, cid, hashed_pass))
            conn.commit()
            print(" Registration successful.")
            cursor = conn.execute("SELECT usid, usnm, cid FROM users WHERE cid = ?", (cid,))
            user = cursor.fetchone()
            print(f" Login successful. Welcome, {user[1]}!")
            conn.execute("INSERT OR REPLACE INTO user_status (usid, status) VALUES (?, 'active')", (user[0],))
            conn.commit()
            logged(user)
        except Exception as e:
            print(" College ID already exist!:", e)


def change(cid):
    while True:
        opass = getpass.getpass("Enter your current password: ")
        hashed_old = hash_password(opass)

        cursor = conn.execute("SELECT * FROM users WHERE cid = ? AND pass = ?", (cid, hashed_old))
        if cursor.fetchone():
            break
        print("Current password incorrect.")

    while True:
        npass = getpass.getpass("Enter new password: ").strip()
        if not npass:
            print("Password cannot be empty.")
            continue
        confirm_pass = getpass.getpass("Confirm new password: ").strip()
        if npass != confirm_pass:
            print("Passwords do not match. Try again.")
            continue
        break

    hashed_new = hash_password(npass)
    conn.execute("UPDATE users SET pass = ? WHERE cid = ?", (hashed_new, cid))
    conn.commit()
    print("Password changed successfully.")

def logged(user):
    while True:

        print("1. Display your details")
        print("2. Change password")
        print("3. Logout")
        choice = input("Enter your choice: ")

        if choice == '1':
            print(f"\nUser Info:")
            print(f"User ID: {user[0]}")
            print(f"Name   : {user[1]}")
            print(f"College ID: {user[2]}")

        elif choice == '2':
            change(user[2])  # Use college ID to find the record

        elif choice == '3':
            conn.execute("UPDATE user_status SET status = 'inactive' WHERE usid = ?", (user[0],))
            conn.commit()
            print("Logged out successfully.")
            break

        else:
            print(" Invalid choice!!")


def login():
    cid = input("Enter your college ID: ").strip()
    password = getpass.getpass("Enter your password: ")
    hashed_pass = hash_password(password)

    cursor = conn.execute("SELECT usid, usnm, cid FROM users WHERE cid = ? AND pass = ?", (cid, hashed_pass))
    user = cursor.fetchone()

    if user:
        print(f" Login successful. Welcome, {user[1]}!")
        logged(user)
    else:
        print(" Invalid college ID or password.")

while True:
    print("\n=== MAIN MENU ===")
    print("1. Register")
    print("2. Login")
    print("3. Exit")
    choice = input("Enter your choice: ")

    if choice == '1':
        register()
    elif choice == '2':
        login()
    elif choice == '3':

        print(" Exiting program...")
        break
    else:
        print("Invalid option. Please try again.")
conn.close()