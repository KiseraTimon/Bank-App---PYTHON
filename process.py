#Modules
from utils import message, errhandler

#Homepage Function
def home(session):
    welcome = f'Hello {session["lname"]}. Choose an option to continue'
    message(welcome)
    
    #Capturing Input
    while True:
        try:
            opt = input(f'1. Deposit Money\n'
                        f'2. Withdraw Money\n'
                        f'3. Transfer Funds'
                        f'4. Check Balance\n'
                        f'5. Access Loans\n'
                        f'6. View & Edit Details\n'
                        f'7. Logout\n'
                        )
            
            #Validating Input
            if opt.isdigit():
                if 0 < opt <= 7:
                    
                    #Processing Cases
                    match opt:
                        case 1:
                            return deposit()
                        case 2:
                            return withdraw()
                        case 3:
                            return transfer()
                        case 4:
                            return balance()
                        case 5:
                            return loans()
                        case 6:
                            return edit()
                        case 7:
                            del session
                            
                            from bank import main
                            return main()
                
                else:
                    err = "Enter a valid option number"
                    message(err)
            
            else:
                err = "Enter the number matching the option"
                message(err)
        
        #Capturing Exception
        except Exception as e:
            logger = 'logs/process-logs.txt'
            errhandler(e, logger)


#Global Variables
finances = {
    "userID" : "userID",
    "balance" : "balance",
    "loan" : "loan",
    "credits" : "credits"
}

#Handling Deposits
def deposit():
    pass

#Handling Withdrawals
def withdraw():
    pass

#Handling Transfers
def transfer():
    pass

#Handling Balances
def balance():
    pass

#Handling Loans
def loans():
    pass

#Handling Account Edits
def edit():
    pass
