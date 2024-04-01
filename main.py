import hashlib
import sys
import getpass


def hashPassword(x):
    hash = hashlib.sha256()
    hash.update(x.encode('utf-8'))
    print(hash.hexdigest())


help_message =  "Usage: python3 main.py [arg] Example: python3 main.py -d Command list: -hA(sha256 hash"

if sys.argv[1] == "-hA":
    if len(sys.argv) < 4:
        userPass = getpass.getpass("Please enter the password: ")
        hashPassword(userPass)
        sys.exit(1)

elif sys.argv[1] == "-d":
    pass

elif sys.argv[1] == "-h" or sys.argv[1] == "--help":
    print(help_message)

else: 
    print("First argument no found " + sys.argv[1])    
    print(help_message)










