import os
import hashlib

#Checks the strength of the password.
#Does this by taking the amount of uppercase, lowercase, and non characters in the string.
# It then creates a score out of 6 with 6 or more of a charcter type being equal to 2
#ex: 6 or more uppercase letter = score of 2
def check_strength(user_pass):
    letters_uc = []
    letters_lc = []
    non_letters = []
    lc_strength_number =0
    nc_strength_number =0 
    uc_strength_number =0

    for char in user_pass:
      
        if char.isupper():
            
            letters_uc.append(char)
            
            if( 2 > len(letters_uc) < 6):
                uc_strength_number = 1
                
            elif(len(letters_uc) < 2):
                uc_strength_number =0

            elif(len(letters_uc) >= 6):
                uc_strength_number = 2

        elif char.islower():

            letters_lc.append(char)

            if( 2 > len(letters_lc) < 6):
                lc_strength_number = 1
                
            elif(len(letters_lc) < 2):
                lc_strength_number =0

            elif(len(letters_lc) >= 6):
                lc_strength_number = 2
        
        else: 
            
            non_letters.append(char)

            if( 2 > len(non_letters) < 6):
                nc_strength_number = 1
                
            elif(len(non_letters) < 2):
                nc_strength_number =0

            elif(len(non_letters) >= 6):
                nc_strength_number = 2

    total_strength = (uc_strength_number + lc_strength_number + nc_strength_number)


    if(total_strength == 6):
        print("Strength: high!")
    elif(4 < total_strength < 6):
        print("Strength: medium")
        help_message()
    elif(total_strength  <= 4):
        print("Strength: low")
        help_message()
        
    store_password(total_strength, user_pass)
#prompts user if they want to store a password ABCDEFGhijklm1234@3
# will store the name of the file the user wants to create to store the password along with encryption key, and generating public and private key to decrpyt the file
def store_password(total_strength, user_pass):


    if(total_strength == 6):
        user_store_pass_opt = input("Would you like to store the password? y/n: ")
        if(user_store_pass_opt == "y"):

            new_user = input("Have you used this program before? y/n ")
            if(new_user == "y"):
                path = input("Enter the file path: ")
                user_file_name_ex = input("Please enter the name of the file: " )

                if os.path.exists(path):
                    pass_purpose_ex = input("What website or organization is this password for? ")

                    with open(f"{path}/{user_file_name_ex}", "a+") as user_file: 
                        user_file.write("Organization: {}, Password: {}\n".format(pass_purpose_ex, user_pass))
                        

            else: 
                user_file_name = input("Enter file name: ")
                pass_purpose = input("What website or organization is this password for? ")



                with open(f"{user_file_name}.txt", "w+") as file: 
                    file.write("Organization: {}, Password: {}\n".format(pass_purpose, user_pass))


        
        elif(user_store_pass_opt == "n"):
            print("Thank you for using password manager!")
            SystemExit
        else:
            print("Please enter either y/n")
            
    


#Checks if the user password is greater than or equal to 12 characters.
#runs help message otherwise
def check_password(user_pass):
    print(
'''
    Y
  .-^-.
 /     \      .- ~ ~ -.
()     ()    /   _ _   `.                     _ _ _
 \_   _/    /  /     \   \                . ~  _ _  ~ .
   | |     /  /       \   \             .' .~       ~-. `.
   | |    /  /         )   )           /  /             `.`.
   \ \_ _/  /         /   /           /  /                `'
    \_ _ _.'         /   /           (  (
                    /   /             \  \\
                   /   /               \  \\
                  /   /                 )  )
                 (   (                 /  /
                  `.  `.             .'  /
                    `.   ~ - - - - ~   .'
                       ~ . _ _ _ _ . ~
'''
  )
    if(len(user_pass) >= 12):
        check_strength(user_pass)
        
    else: 
        help_message()
        
#help message to create strong password
def help_message():
    print("-Make sure password is at least 12 characters long.")
    print("- Use a mix of uppercase and lowercase letters.")
    print("-Include special characters such as @, #, $, etc.")
    

user_pass = input("Please enter a password to be checked: ")

check_password(user_pass)