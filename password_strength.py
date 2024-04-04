import sys
import string 

def check_strength(user_pass):
    for char in user_pass:
        if(char.isupper() | char.islower() ):
            
            pass



def check_password(user_pass):
    if(len(user_pass) >= 12):
        check_strength(user_pass)
    else: 
        help_message()
        

def help_message():
    print("- Use a mix of uppercase and lowercase letters.")
    print("-Include special characters such as @, #, $, etc.")

user_pass = input("Please enter a password to be checked: ")

check_password(user_pass)