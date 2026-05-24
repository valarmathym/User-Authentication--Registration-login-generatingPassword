# Python program for Creating Registration  for new user and login system for registered user
# Created by Valarmathy Murugan on dated 14-06-22 
# As per the feedback given by the teacher, Created the functionality of viewing accounts.txt file by the 'admin' on dated 17-06-22
# I have used 'admin' as username and 'Pass' as the password for the admin to login and access the permission to view accounts.txt file


import time
import random
import string
from threading import Event

letters1 = string.ascii_lowercase
letters2 = string.ascii_uppercase
num = string.digits
symbols = string.punctuation


# login page for registered user and the username and password is checked with accounts.txt file
def login():
    Username = input("Enter your username : ")
    Password = input("Enter your password : ")

    # the values in the accounts.txt file is stored in a dictionary as key:value pair
    dataFile = open("accounts.txt", "r")  # opens the accounts.txt file
    data = {}
    for i in dataFile:
        a, b = i.split(" ")  # splits the username and password
        b = b.strip()  # strip is to remove space in password
        data[a] = b
    dataFile = open("accounts.txt", "r")
    if Username in data:
        if Password == data[Username]:                      # data[Username] gets the corresponding value(Password)
            print("Login success!")
            if Username == "admin" and Password == "Pass":
                print("You have the permission to view the accounts.txt file")
                for i in data:
                    print(i + " " + data[i])            # accounts.txt file - for the admin to view
        else:
            print("Login unsuccessful!. The username or password is incorrect. Please try again.")

    else:
        print("Login unsuccessful!. The username or password is incorrect. Please try again.")
    dataFile.close()
    Event().wait(2)
    exit()
    #login()


# The following function is for the new user to register
def register():
    Username = input("Create  username: ")
    Option = input("Do you want to auto-generate your password? Yes / No: ")

    # User registers with own password

    if (Option == 'No'):
        Password = input("Create your Password: ")
        # save()
        dataFile = open("accounts.txt", "a")
        dataFile.write(Username + " " + Password + "\n")
        dataFile.close()
        print("Registration Success! Go to login page!")
        Event().wait(2)
        login()

    # generating the password according the options to selection letters and numbers or symbols and password length
    elif (Option == 'Yes'):
        passLength = int(input("Enter the length of the password : "))
        userLet1 = input("Do you want to use 'Lowercase letters' in your password?(Yes/No) : ")
        userLet2 = input("Do you want to use 'Uppercase letters' in your password?(Yes/No) : ")
        userSym = input("Do you want to use 'symbols' in your password? (Yes/No) : ")
        userNum = input("Do you want to use 'numbers' in your password? (Yes/No) : ")

        # user selecting letters(lowercase,uppercase), symbols, digits to be present in the password generation
        if userLet1 == "Yes":
            selection1 = letters1
        else:
            selection1 = ""
        if userLet2 == "Yes":
            selection2 = letters2
        else:
            selection2 = ""

        if userSym == "Yes":
            selection3 = symbols
        else:
            selection3 = ""

        if userNum == "Yes":
            selection4 = num
        else:
            selection4 = ""

        all = selection1 + selection2 + selection3 + selection4
        temp = random.sample(all, passLength)                           # generating random password (auto)
        password = "".join(temp)
        print(password)
        dataFile = open("accounts.txt", "a")
        dataFile.write(Username + " " + password + "\n")               # writing username, password in accounts.txt file
        dataFile.close()  # closing the accounts.txt file
        # Event().wait(2)
        print("Go to login Page")
        login()


# Checking first if the user is a registered or new
user = input("Are you a new user? Y/N: ")
if user == "N":
    print("Go to login page")
    login()

else:
    print("Go to registration page")
    register()
