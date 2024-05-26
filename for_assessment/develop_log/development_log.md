## Week 3, Term 5
### Notes
1. Connect the database
2. Coding the login and register function
3. Connect these two functions to the UI
### Evidence
#### 1. Connect the database
##### - Code

```python
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
```
##### - Results
- When the database already exists the account is called “admin” with the password “admin 12345”
  Console print: Welcome
- When the database already exists the account is called “admin” with the password “54321nimda”
  Console print: Login failed
- When the database doesn’t exist the account is called “admin”
  Console print: Login failed
##### - Comments
- The connection to the database works well.
#### 2. Coding the login and register function.
##### - Code

```python
import sqlite3 as sql
import os
import hashlib

con = sql.connect("db/users.db")
cur = con.cursor()

def check():
    username = "admin_1"
    password = "12345"
    statement = f"SELECT salt from users WHERE username='{username}';"
    cur.execute(statement)
    salt = cur.fetchall()
    salt = salt[0][0]
    byte_password = (password+salt).encode()
    hash_password = hashlib.sha256(byte_password).hexdigest()
    statement = f"SELECT username from users WHERE username='{username}' AND Password = '{hash_password}';"
    cur.execute(statement)
    if not cur.fetchone():
        print("Login failed")
    else:
        print("Welcome")

def add():
    username = "admin_1"
    password = "12345"
    salt = os.urandom(32).hex()
    byte_password = (password+salt).encode()
    hash_password = hashlib.sha256(byte_password).hexdigest()
    statement = f"INSERT INTO users VALUES ('{username}','{hash_password}','{salt}');"
    print(statement)
    cur.execute(statement)
    con.commit()

add()
check()
```
##### - Results
- Console print: Welcome
- The database has been added an account with the username ”admin_1” and an encrypted password with its salt.
##### - Comments
- The encrypted part works well.
- The adding account function works well.
#### 3. Connect the login function to the UI
##### - Code

```python
import account_handling

class loginDialog(QDialog):
    def __init__(self):
        super(loginDialog,self).__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.init_slot()

    def init_slot(self):
        self.ui.signInButton.clicked.connect(self.check_account)

    def check_account(self):
        username = self.ui.usernameLineEdit.text().strip()
        password = self.ui.passwordLineEdit.text().strip()
        correct = account_handling.check(username,password)
        if correct:
            self.jumpMain()
        else:
            QMessageBox.critical(None,"Error","Incorrect user name or password.")

    def jumpMain(self):
        self.close()
        window.show()
```

##### - Results
![][W3T2/developmentlog_w3t2_1.gif]
##### - Comments
- The login function works well. It will lead users to the main window when they enter the correct username and password.