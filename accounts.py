#Importing Module
from utils import message, errhandler

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
    txt = "Welcome Back. Enter Your Details To Continue"
    message(txt)
    
    #Error Handling
    while True:
        try:
            #Capturing Details
            user_email = str(input("Enter your username or email:\n"))
            pin = int(input("Enter your pin:\n"))
            
            for account, details in accounts:
                for detail, value in details:
                    
                    #Checking Username/Email Exists
                    if user_email in value:
                        #Validating Pin
                        if pin == detail["pin"]:
                            
                            #Populating Session
                            session = {
                                "userID": account,
                                "fname" : detail["fname"],
                                "lname" : detail["lname"],
                                "email" : detail["email"],
                                "phone" : detail["phone"],
                                "uname" : detail["uname"],
                            }
                            
                            #Success Messaage
                            success = "You have been logged in successfully"
                            message(success)
                            
                            from pages import home
                            return home(session)
                        
                        else:
                            err = "Your pin is invalid"
                            message(err)
                        
                    else:
                        err = "The username/email does not exists"
                        message(err)
        
        #Error Handling
        except Exception as e:
            errhandler(e)
    
        def users():
            print (accounts)
            
        return users()

#Registration Manager
def register():
    txt = "Become Part Of The Py Bank Family Today"
    message(txt)
    
    #Error Handling
        
    while True:
        try:
            #Capturing User Details
            fname = str(input("Enter your first name:\n")).strip()
            lname = str(input("\nEnter your last name:\n")).strip()
            email= str(input("\nEnter your email:\n")).strip()
            phone= int(input("\nEnter your phone number:\n"))
            uname = str(input("\nSet a username:\n")).strip()
            pin = int(input("\nSet a pin [4 digits]:\n"))
            pin_conf = int(input("\nConfirm your pin:\n"))
            
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
    
        #Error Handling
        except Exception as e:
            errhandler(e)
        
        return login()
    