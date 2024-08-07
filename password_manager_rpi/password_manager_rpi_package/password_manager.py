import sys
import os

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

#stores new user file to a specific file path in the user's computer
#txt file nu = new user
def new_store_password_txt_nu(user_pass):
    #consider resolving the file path to the current working directorys
    #get the users name instead and add it to the name of txt file 
    path = input("Enter the file path: \n")
    user_file_name_nw= input("Please enter the name of the file: \n")

        

    if os.path.exists(path):
        pass_purpose_nw= input("What website or organization is this password for?\n")
        pass_username_nw = input("What is the username of the account?\n")

        with open(f"{path}/{user_file_name_nw}.txt", "w+") as user_file: 
            user_file.write("Organization: {},Username: {} , Password: {}\n".format(pass_purpose_nw, pass_username_nw, user_pass))  

           

#Store reoccuring user passwords in a text file
#txt file ru = returning user
def store_password_txt_ru(user_pass):
    #get the users name and add it to the name of the txt file
    #consider resolving the file path to the current working directorys
    pass_purpose = input("What website or organization is this password for? \n")
    pass_username = input("What is the username of the accounts? \n")

    with open(f"user_pass.txt", "a+") as file: 
        file.write("Organization: {}, Username: {}, Password: {}\n".format(pass_purpose, pass_username, user_pass))


#new users store password decision tree
def store_password_decision_tree_newusers(user_pass_1):
    while True:
        print("How would you like to store your password? \n")
        print("1- SQL Database\n")
        print("2- Text file\n")
        print("3- AWS database\n")
        print("4- Go back\n")
        user_choice = input("What would you like to do? ")

        if user_choice == '1':
            pass

        elif user_choice == '2':
            new_store_password_txt_nu(user_pass_1)
        elif user_choice == '3':
            pass

        elif user_choice == '4':
            break
        else:
            print("Please enter a valid choice.")

#reoccuring user store password decision tree
def store_password_decision_tree_returninguser(user_pass_1):
    while True:
        print("How would you like to store your password? \n")
        print("1- SQL Database\n")
        print("2- Text file\n")
        print("3- AWS database\n")
        print("4- Go back\n")
        user_choice = input("What would you like to do? ")

        if user_choice == '1':
            pass

        elif user_choice == '2':
            store_password_txt_ru(user_pass_1)
        elif user_choice == '3':
            pass

        elif user_choice == '4':
            break
        else:
            print("Please enter a valid choice.")


    




#Checks if the user password is greater than or equal to 12 characters.
#runs help message otherwise
def check_password(user_pass):
   if(len(user_pass) >= 12):
        check_strength(user_pass)
   else:
      help_message()


#help message to create strong password
def help_message():
    print("-Make sure password is at least 12 characters long.\n")
    print("- Use a mix of uppercase and lowercase letters.\n")
    print("-Include special characters such as @, #, $, etc.\n")
    
#main method
def main():

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
  print('Welcome to password manager!\n')
  print('Please enter 1 you are new to this program and 2 if you have used this program before\n')

  while True:

    print('1- New User\n')
    print('2- Reoccuring User\n')
    print('3- Exit\n')
    user_choice = input('What would you like to do?: ')

    #new user options
    if user_choice == '1':
      while True:
        print("1- Check password\n")
        print("2- Store password\n")
        print("3- Go back\n")
        user_choice_2 = input("What would you like to do?: ")
        
        if user_choice_2 == '1': 
                user_pass_1 = input("Please enter password to be checked:\n")
                check_password(user_pass_1)

        elif user_choice_2 == '2':
            user_pass_1 = input("Please enter password stored: \n")
            store_password_decision_tree_newusers(user_pass_1)
            

        elif user_choice_2 == '3':
            break

        else:
            print("Please enter a valid choice.")

    #reoccuring user options
    elif user_choice == '2':

        while True:
            print("1- Check password\n")
            print("2- Store password\n")
            print("3- Go back\n")

            user_choice_3 = input("What would you like to do?: ")
            
            if user_choice_3 == '1': 

                user_pass_2 = input("Please enter password to be checked:\n")
                check_password(user_pass_2)

            elif user_choice_3 == '2':
                
                user_pass_2 = input("Please enter password stored: \n")
                store_password_decision_tree_returninguser(user_pass_2)

            elif user_choice_2 == '3':
                break
       
            else: 
                print("Please enter a valid choice.")

    elif user_choice == '3':
        sys.exit(0)

    else:
       print("Please enter a valid choice.")






if __name__ == "__main__":
    main()