from math import exp
import sqlite3 as sql
import os
import hashlib

con = sql.connect("db/users.db")
cur = con.cursor()

def check(username,password):
    # Get salt from database
    statement = f"SELECT salt from users WHERE username='{username}';"
    cur.execute(statement)
    salt = cur.fetchone()
    salt = salt[0] # Convert tuple to str

    # Encrypt the given password with salt
    byte_password = (password+salt).encode()
    hash_password = hashlib.sha256(byte_password).hexdigest()

    # Compare to the origin encrypt password
    statement = f"SELECT username from users WHERE username='{username}' AND Password = '{hash_password}';"
    cur.execute(statement)

    if not cur.fetchone():  # An empty result evaluates to False.
        correct = False
    else:
        correct = True

    return correct

def add(username,password):
    # Encrypt password with salt
    salt = os.urandom(32).hex()
    byte_password = (password+salt).encode()
    hash_password = hashlib.sha256(byte_password).hexdigest()
    statement = f"INSERT INTO users VALUES ('{username}','{hash_password}','{salt}');"
    cur.execute(statement)
    con.commit()