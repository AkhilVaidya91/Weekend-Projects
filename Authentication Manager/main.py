# exec code

from auth import *

flag = ""
while flag != "exit":
    flag = ""
    flag = (input("Do you want to login, signup or exit ? (Enter: login/signup/exit): ").rstrip()).lower()
    if flag == "exit":
        break
    elif flag == "signup":
        userName = input('Enter username: ')
        password = input('Enter password: ')
        sign_up(userName, password)
    elif flag == "login":
        userName = input('Enter username: ')
        password = input('Enter password: ')
        val = login(userName, password)
        if val == 1:
            break
    else:
        print("Invalid input.")