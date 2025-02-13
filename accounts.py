#Importing Module
from utils import message

#Accounts
accounts = {
    0 : {
        "fname" : "fname",
        "lname" : "lname",
        "email" : "email",
        "phone" : "phone",
        "uname" : "uname",
        "pin" : "pin",
    }
}

#Login Manager
def login():
    pass

#Registration Manager
def register():
    txt = "Become Part Of The Py Bank Family Today"
    message(txt)
    
    while True:
        #Capturing User Details
        fname = str(input("Enter your first name:\t\t")).strip()
        lname = str(input("\nEnter your last name:\t\t")).strip()
        email= str(input("\nEnter your email:\t\t")).strip()
        phone= int(input("\nEnter your phone number:\t"))
        uname = str(input("\nSet a username:\t\t\t")).strip()
        pin = int(input("\nSet a pin [4 digits]:\t\t"))
        pin_conf = int(input("\nConfirm your pin:\t\t"))
        
        #Validating All Fields Are Filled
        if not (fname or lname or email or phone or uname or pin or pin_conf):
            err = "Please fill in all fields"
            message(err)
            
        #Validating Passwords Match
        elif (pin != pin_conf):
            err = "Passwords do not match"
            message(err)
            
        #Adding The User To The Dictionary Mock Database
        else:
            #Fetching Last User ID
            for account in accounts:
                if account:
                    id = account[-1]
                    id += 1
                else:
                    id = 1
            
            #Populating Accounts
            accounts[id] = {
                    "fname" : fname,
                    "lname" : lname,
                    "email" : email,
                    "phone" : phone,
                    "uname" : uname,
                    "pin" : pin,
                }
            
            success = "Your new account has been created successfully"
            message(success)
            
            user = accounts[id]
        
        print(f"Your new account details are:\n\n{user}")
        return accounts[id]