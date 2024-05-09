import sqlite3 as sql

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

