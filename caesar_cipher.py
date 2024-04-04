import sys
import getpass



def encrypt_text(text, shift):
        encrypted_text = ""

        for char in text: 

            if char.isalpha():
                if char.isupper():
                    encrypted_char = chr((ord(char) - 65 + shift) % 26 + 65)

                else:
                    encrypted_char = chr((ord(char) - 97 + shift) % 26 + 97)
            else : 
                encrypted_char = char

            encrypted_text += encrypted_char
        return encrypted_text 

def decrpyt_text(x, y):
    encrypted_text = ""

    for char in x: 
        if char.isalpha():
            if char.isupper():
                encrypted_char = chr((ord(char) - 65 - y)% 26 +65)
            else: 
                encrypted_char = chr((ord(char) - 97 - y)% 26 + 97)
        else: 
              encrypted_char = char

        encrypted_text += encrypted_char
    return encrypted_text


help_message =  "Usage: python3 main.py [arg] Example: python3 main.py -d Command list: -d, -e(decrypt, encrypt)"
    
if sys.argv[1] == "-e":
        if len(sys.argv) < 4:
            user_input_e = getpass.getpass("Please enter text to encrypt: ")
            shift_e = int(input("Please enter your key: "))
            encrypted_text_e = encrypt_text(user_input_e, shift_e)

            print("Encrypted text: ", encrypted_text_e)

        sys.exit(1)

elif sys.argv[1] == "-d":
            user_input_d = input("Please enter text to decrpyt: ")
            shift_d = int(input("Please enter shift: "))
            encrypted_text_d = decrpyt_text(user_input_d, shift_d)

            print("Decrypted text: ", encrypted_text_d)

elif sys.argv[1] == "-h" or sys.argv[1] == "--help":
        print(help_message)

else: 
        print("First argument not found " ,sys.argv[1])    
        print(help_message)
