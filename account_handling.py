import sqlite3 as sql
import os
import hashlib

con = sql.connect("db/users.db")
cur = con.cursor()

def check():
    # Will connect to slots of the login UI
    username = "admin"
    password = "12345"

    # Get salt from database
    statement = f"SELECT salt from users WHERE username='{username}';"
    cur.execute(statement)
    salt = cur.fetchall()
    salt = salt[0][0] # Convert tuple to str

    # Encrypt the given password with salt
    byte_password = (password+salt).encode()
    hash_password = hashlib.sha256(byte_password).hexdigest()

    # Compare to the origin encrypt password
    statement = f"SELECT username from users WHERE username='{username}' AND Password = '{hash_password}';"
    cur.execute(statement)
    if not cur.fetchone():  # An empty result evaluates to False.
        print("Login failed")
    else:
        print("Welcome")

def add():
    # Will connect to slots of the sign up UI
    username = "admin_1"
    password = "54321"

    # Encrypt password with salt
    salt = os.urandom(32).hex()
    byte_password = (password+salt).encode()
    hash_password = hashlib.sha256(byte_password).hexdigest()
    statement = f"INSERT INTO users VALUES ('{username}','{hash_password}','{salt}');"
    print(statement) # Debug
    cur.execute(statement)
    con.commit()

# Debug
print("Check:")
check()
print("Add:")
add()