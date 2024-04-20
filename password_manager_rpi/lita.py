import sys

# this class will be the encryption alogrithm for the password manager
def format_data(user_pass, pass_purpose, pass_username):

    pass_info = f"{user_pass} {pass_purpose} {pass_username}"

    pass_info_bits = sys.getsizeof(pass_info) * 8


def lita(user_pass, pass_purpose, pass_username):
    format_data(user_pass, pass_purpose, pass_username)
    