import hashlib
import getpass


def hashPassword(x):
    hash = hashlib.sha256()
    hash.update(x.encode('utf-8'))
    print(hash.hexdigest())

userInput = getpass.getpass("Enter your password: ")
hashPassword(userInput)







