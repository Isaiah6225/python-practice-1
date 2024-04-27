import sys

user_pass = 'abcdefGHIJKL1234@#'
pass_purpose = 'Google'
pass_username = 'Isaiah6225'




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
    num_rows_defined = 4
    cols = 4

    #Populate the matrix from pass_info
    for i in range(num_rows_defined):
        row = []
        for j in range(cols):
            #Calculates the index in pass info to the element in the matrix
            index = i * cols + j

            #if index is within bounds of the list append the value to the row
            if index < len(pass_info):

                row.append(pass_info[index])

            #If the index exceeds the length fo the list add padding
            else: 
                row.append(None)
        matrix.append(cols)

    print(matrix)

arrange_matrix()