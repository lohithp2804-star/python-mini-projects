#Password checker
from getpass import getpass                                        #this statement is for the declaration of getpass
user_name = input("Enter username: ")
username = user_name.lower()
if (username=="lohith.active"):
    password = getpass("Enter password(hidden): ")                         #⚠️Note: The password field will appear empty while typing — but it's accepting input behind the scenes.
    if (password == "2804"):
        print("Access granted")
    else:
        print("Wrong password")
else:
    print("Unknown user")