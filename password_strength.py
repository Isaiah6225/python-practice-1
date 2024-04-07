import sys
import string 

def check_strength(user_pass):
    for char in user_pass:
        if(char.isupper()):
            letters_uc = char 
            print(letters_uc)

        elif(char.islower()):
            letters_lc = char 
            print(letters_lc)
        elif():
            non_letter = char
            print(non_letter)

def check_password(user_pass):
    if(len(user_pass) >= 12):
        check_strength(user_pass)
    else: 
        help_message()
        

def help_message():
    print("-Make sure password is at least 12 characters long.")
    print("- Use a mix of uppercase and lowercase letters.")
    print("-Include special characters such as @, #, $, etc.")
    

user_pass = input("Please enter a password to be checked: ")

check_password(user_pass)