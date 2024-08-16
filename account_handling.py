import sqlite3 as sql
import os
import hashlib
import re


# Connect to the database
con = sql.connect("db/users.db")
cur = con.cursor()


# Check the username and the password are correct or not and return a boolean
def check(username, password):
    # Get salt from database
    statement = "SELECT salt FROM users WHERE username=?;"
    cur.execute(statement, (username,))
    salt = cur.fetchone()

    if not salt:  # If salt not existing
        correct = False
    else:
        salt = salt[0]  # Convert list to str

        # Encrypt the given password with salt
        byte_password = (password + salt).encode()
        hash_password = hashlib.sha256(byte_password).hexdigest()

        # Compare to the original encrypted password
        statement = """SELECT username FROM users WHERE username=? AND Password=?;"""
        cur.execute(statement, (username, hash_password))

        if not cur.fetchone():  # An empty result evaluates to False.
            correct = False
        else:
            correct = True

    return correct


# Check the password is legal or not and return a boolean
def checkLegalPassword(password):
    regex = r"^(?=.*[A-Z])(?=.*[a-z])(?=.*\d).{6,}$"
    if re.search(regex, password):
        return True
    else:
        return False


# Add the username and the password to database with encrypt
def add(username, password):
    # Encrypt password with salt
    salt = os.urandom(32).hex()
    byte_password = (password + salt).encode()
    hash_password = hashlib.sha256(byte_password).hexdigest()
    statement = """INSERT INTO users (username, password, salt) VALUES (?, ?, ?);"""
    cur.execute(statement, (username, hash_password, salt))
    con.commit()


# Close the connect with the database
def exitDB():
    cur.close()
    con.close()
