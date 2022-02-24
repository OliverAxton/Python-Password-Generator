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
    print("4: Check Password Strength Against Common Password List")
    option = int(input("Please select option: "))

    if option == 1:
        generate_password()
    elif option == 2:
        generate_password_save()
    elif option == 3:
        get_main_option()
    elif option == 4:
        check_password_strength()
    else:
        print("Wrong number entered, please enter a valid number: ")
        print("")
        get_main_option()


def generate_password_save():
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


def check_password_strength():
    cls()
    print("Check Password Strength")
    print("")
    print("How this works:")
    print("1: You enter the password")
    print("2: Your password is checked if it has been used in one of a couple main word lists")
    print("3: If your password is found in the list then it will be a very weak and common password")
    print("4: If your password isn't found then you will be told, this however does not mean that your password is safe")
    print("")
    password=input("Please enter the password you want to check: ")
    print("")
    passwordfound=check_password_wordlist(password)

    if passwordfound == True:
        print("Your password was found in the common password file")
        print("It is recommended that you change any logins that use this password")
        print("")
        print("Returning to menu")
        print("")
        main()

    else:
        print("Your password was not found in the common passwords file")
        print("However, this does not mean that your password has the best security.")
        print("")
        print("Returning to menu")
        print("")
        main()



def check_password_wordlist(password):
    cls()
    rockyou_passwords=open('rockyou.txt','r', encoding="utf8")
    Lines = rockyou_passwords.readlines()
    count_rock_you=0
    found_password=False
    for line in Lines:
        if line.strip() == password:
            print("Password found in password list!")
            found_password=True
            break
        else:
            count_rock_you += 1
    return found_password


def cls():
    os.system('cls' if os.name=='nt' else 'clear')


main()