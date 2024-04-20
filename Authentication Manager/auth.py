# This file contains function definitions for the Authentication Manager

# Requirements:
# 1. Two options for the user - Sign up or Login
# 2. When a user chooses to Sign up
#    Store the user id and password in the login table in authManager database
# 3. When the user chooses the Login option
#    Input the username and password from the uesr
#    search within the table the username; if not exists throw error 'invalid username'
#    if the username is found, check if the password is same
#    if the password is same - 'Login successful' and exit else throw 'invalid password'
from cryptography.fernet import Fernet
import mysql.connector

#creaiting a database object db
db = mysql.connector.connect(
    host= "localhost",
    user= "root",
    passwd= "akhil912004"
)

#creating a databse cursor
cursor = db.cursor()


#this is a one time use function to generate the encryption key and store it in file key.key
# def write_key():
#     key = Fernet.generate_key()
#     with open("key.key", 'wb') as kf:
#         kf.write(key)
# write_key()

#this finction reads the key value from the key.key file and returns it
def load_key():
    file = open("key.key", 'rb')
    key = file.read()
    file.close()
    return key

key = load_key()
# fernet object created by the Fernet() function using the key
fer = Fernet(key)


# login function takes in the user input userID and password and compares it with the user ID and password in the db
# returns 1 for successful login else returns 0
def login(user_id, password):
    cursor.execute("USE authManager")
    data = [user_id]
    cmd = "select passw from login where user_id = %s;"
    cursor.execute(cmd, data)
    res = str(cursor.fetchall())
    if res == "[]":
        print("Invlaid username.")
        return 0
    passw = str(res[3:len(res)- 4])
    passw = fer.decrypt(passw.encode()).decode()
    if passw == password:
        print("Login successful.")
        return 1
    else:
        print("Invlaid password.")
        return 0

# signup function adds the username and password (in encrypted form) to the db
def sign_up(user_id, password):
    password = fer.encrypt(password.encode()).decode()
    cursor.execute("USE authManager")
    data = [user_id, password]
    stri = "insert into login values(%s, %s);"
    cursor.execute(stri, data)
    db.commit()
