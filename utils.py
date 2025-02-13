from datetime import datetime
import traceback  # Import the traceback module

# Bank Messaging Format
def message(text):
    message = f"\n***\n{text}\n***\n"
    print(message)

# Timestamp
def timestp():
    #Get the current date and time
    now = datetime.now()
    return now.strftime("%d-%m-%Y %H:%M:%S")

#Error Details Extractor
def error(e):
    #Get Exception Details [Error Type & Message]
    err_type = type(e).__name__
    err_msg = str(e)
    
    #Traceback Details
    #Last Traceback Entry
    tb = traceback.extract_tb(e.__traceback__)[-1]
    
    #Filename & Line Number Of The Error
    filename = tb.filename
    line_no = tb.lineno
    
    # Formatting Error Details
    error_details = (
        f"Error: {err_type} - {err_msg}\n"
        f"File: {filename}\n"
        f"Line: {line_no}"
    )
    
    #Return Error Details
    return error_details