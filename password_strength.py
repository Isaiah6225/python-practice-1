

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
    elif( 4 < total_strength > 6):
        print("Strength: medium")
    elif(total_strength <= 2):
        print("Strength: low")


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