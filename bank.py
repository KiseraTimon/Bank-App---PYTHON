#Bank
def main():
    #Bank Messaging Format
    def message(text):
        message = f"\n***\n{text}\n***\n"
        
        print(message)
    
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
                        def account(service):
                            pass
                        print(service)
                        break
                    
                    #Option 2
                    case 2:
                        def account(service):
                            pass
                        print(service)
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