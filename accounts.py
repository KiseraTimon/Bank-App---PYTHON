#Importing Module
from utils import message, timestp, error

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
    txt = "Become Part Of The Py Bank Family Today"
    message(txt)

#Registration Manager
def register():
    txt = "Become Part Of The Py Bank Family Today"
    message(txt)
    
    #Error Handling
        
    while True:
        try:
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
    
        #Error Handling
        except Exception as e:
            #Logging The Error
            log = f'Error: {e}'
            
            #Timestamp
            time_str = timestp()
            
            #Error Details
            error_details = error(e)
            
            with open('logs.txt', 'a') as f:
                f.write(f'***\n--------------------------------------------------\nTIME OF OCCURENCE:---\n{time_str}\n\nERROR:---\n{log}\n\nERROR DETAILS:---\n{error_details}---\n--------------------------------------------------\n\n')
            
            err = f'An error occured. Kindly try again in a few minutes'
            message(err)
            
            #Redirect to homepage
            from bank import main
            return main()
        
        return login()
    