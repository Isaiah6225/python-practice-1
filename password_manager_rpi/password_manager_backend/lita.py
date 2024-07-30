import hashlib
import os 
import binascii
'''
So far code takes in password, what the password is used
for and the username associated with the password to create a matrix that spilts 
the user data and adds padding to the input if the input is less than 16 bytes.

Looking to implement an unpadding function as well as xor function 
'''

user_pass = b'abcdefGHIJKL1234@#'
pass_purpose = b'Google'
pass_username = b'Isaiah6225'




def format_data(user_pass, pass_purpose, pass_username):
    pass_info = []
    
    pass_info = user_pass + pass_purpose + pass_username
    ex = [pass_info[i:i+4] for i in range(0, len(pass_info), 4)]
    
    return ex

# generates padding if user block isn't 16 bytes 
def generate_padding(pass_info):
    num_of_bytes_pad = 16 % len(pass_info)
    padding = []

    for x in range(1, num_of_bytes_pad + 1):
        padding.append(bytes(x))

    return pass_info.extend(padding)
    
#take data from format data to arrange the data into a matrix

def arrange_matrix():

    pass_info = format_data(user_pass, pass_purpose, pass_username)
    generate_padding(pass_info)

    

    matrix = []
    num_rows = 4
    num_cols = 4

    #Populate the matrix from pass_info
    for i in range(num_rows):
        row = []
        for j in range(num_cols):
            #Calculates the index in pass info to the element in the matrix
            index = i * num_cols + j

            #if index is within bounds of the list append the value to the row
            if index < len(pass_info):

                row.append(pass_info[index])

            #If the index exceeds the length fo the list add padding
            else: 
                row.append(None)
        matrix.append(row)

    plain_text = [print(row) for row in matrix]

    return plain_text

'''
Generates key based on the username and password from the user. 
A secure random salt is then generate and combines with the username in bytes.
The users pasword, combined salt, number of iterations, and the desired length are then used
to generate the intial key.
'''
def generate_key(user_pass, pass_username, iterations=10000, dklen=32):

    #generates a cryptographically secure random salt 
    random_salt = os.urandom(16)

    #combines users information with the random salt 
    combined_salt = hashlib.sha256(pass_username + random_salt).digest()

    #get the key using the Password-Based Key Derivation Function 2 
    inital_key = hashlib.pbkdf2_hmac('sha256', user_pass, combined_salt, iterations, dklen)

    return inital_key

key = generate_key(user_pass, pass_username)

print(f"Key: {binascii.hexlify(key)}")
    





