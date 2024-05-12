import sqlite3 as sql
import os
import hashlib
con = sql.connect("db/users.db")
cur = con.cursor()

def check():
    username = "admin"
    password = "admin12345"
    statement = f"SELECT username from users WHERE username='{username}' AND Password = '{password}';"
    cur.execute(statement)
    if not cur.fetchone():  # An empty result evaluates to False.
        print("Login failed")
    else:
        print("Welcome")

def add():
    username = "admin"
    password = "12345"
    salt = os.urandom(32).hex()
    byte_password = (password+salt).encode()
    hash_password = hashlib.sha256(byte_password).hexdigest()

    statement = f"INSERT INTO users VALUES ('{username}','{hash_password}','{salt}');"
    print(statement)
    cur.execute(statement)
    con.commit()
add()