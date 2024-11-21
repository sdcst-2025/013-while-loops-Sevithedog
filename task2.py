#! python3
"""
Have the user enter a username and password.
Repeat this until both the username and password match the 
following:

username: admin
password: 12345
(2 marks)

inputs:
str (username)
str (password)

outputs:
Access granted
Access denied

example:
Enter username: fred
Enter password: password
Access denied
Enter username: admin
Enter password: password
Access denied
Enter username: admin
Enter password: 12345
Access granted


"""
import os
import time
username = input("Enter username: ")
password = input("Enter password: ")


while not password == "12345" or not username == "admin":
    print("Access Denied")
    time.sleep(1)
    os.system('cls')
    username = input("Enter Username: ")
    password = input("Enter Password: ")
else:
    print("Access Granted")
