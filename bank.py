#Importing Modules
from utils import message
from accounts import login, register


#Bank
def main():
    
    #Welcome Message
    welcome = "Hello & Welcome To Py Bank | Your One Stop Digital Banking Solution"
    
    message(welcome)
    
    while True:
        service = input(f'Pick A Service To Continue:\n'
                        f'1. Sign in to your profile\n'
                        f'2. Register a new account\n'
                        f'3. Exit\n\n'
                        )
        
        #Validating Entry
        if service.isdigit():
            service = int(service)
            
            if 1 <= service <= 3:
                
                #Matching Options
                match service:
                    
                    #Option 1
                    case 1:
                        login()
                        break
                    
                    #Option 2
                    case 2:
                        register()
                        break
                    
                    #Option 3
                    case 3:
                        txt = "[ABORTING]...\n[SUCCESS]..."
                        message(txt)
                        break
            
            else:
                err = "Please enter a number between 1 and 3"
                message(err)
        else:
            err = "Please enter a valid number"
            message(err)


#Calling Bank Function
main()