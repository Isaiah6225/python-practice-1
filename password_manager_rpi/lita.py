import sys

user_pass = 'abcdefGHIJKL1234@#'
pass_purpose = 'Google'
pass_username = 'Isaiah6225'
pass_info = user_pass + pass_purpose + pass_username



def format_data(pass_info):
    pass_info = []
    return [pass_info[i:i+4] for i in range(0, len(pass_info), 4)]

def encrypt_block(pass_info):
    assert len(pass_info) == 16 

    matrix = format_data(pass_info)

    print(matrix)

encrypt_block(pass_info)