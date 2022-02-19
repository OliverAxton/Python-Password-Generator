import os
import string
import random
import xml.etree.ElementTree as ET
import os.path


characters = list(string.ascii_letters + string.digits + "!@#$%^&*()")

def main():
    get_main_option()





def generate_password():
    cls()
    length=int(input("Enter Password Length: "))

    random.shuffle(characters)

    password = []

    for i in range(length):
        password.append(random.choice(characters))

    random.shuffle(password)


    pw=("".join(password))
    print(pw)
    return pw


def get_main_option():
    print("Password Manager")
    print("")
    print("1: Generate new password (unsaved)")
    print("2: Generate new password for site (saved)")
    print("3: View Password for site")
    option = int(input("Please select option: "))

    if option == 1:
        generate_password()
    elif option == 2:
        generate_password_save()
    elif option == 3:
        get_main_option()
    else:
        print("Wrong number entered, please enter a valid number: ")
        print("")
        get_main_option()


def generate_password_save():
    cls()
    print("Create password and save")
    print("")
    site_name=input("Name of site: ")
    site_type=input("Type of site (social media, shopping etc.): ")
    site_username=input("Username or email of site: ")
    site_pw=generate_password()
    cls()

    print("Site name: " + site_name)
    print("Site Type: " + site_type)
    print("Site Username/Email: " + site_username)
    print("Site Password: " + site_pw)
    print("")

    while True:
        user_happy = input("Are you happy with this information? y/n: ")
        if user_happy == "Y" or "y" or "N" or "n":
            False
        else:
             True



def cls():
    os.system('cls' if os.name=='nt' else 'clear')


main()