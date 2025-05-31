# Importing required libraries
import os
from datetime import date
from colorama import Fore, Style, init, Back

# Function to clear the console screen
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')
# Initializing Colorama
init(autoreset=True)

# Function to reset color and style
def reset():
    print(Style.RESET_ALL)

# Functions to get user details of name and gender
    
def get_name():
    print(Fore.CYAN + Style.BRIGHT + "Welcome to the Voting Eligibility Checker!")
    reset()
    global name
    name = input("Enter your name : ")
    name = name.title()
    if len(name) == 0:
        print("You haven't entered name, code terminated")
        exit()   
    # Clearing the screen after input
    clear_screen()    
    return name
def get_gender():
    global gender
    gender = input("Enter your gender \n1)Male 2)Female:")
    if len(gender) != (1 or 4) :
        print("You haven't entered any value, code terminated")
        exit()     
    # Clearing the screen after input
    clear_screen()    
    return gender

# Function to validate gender
def gender_validate(gender):
    if(gender == "1" or "M" or "Male" or "m" or "male" ):
        print("Welcome Mr.",name)
    elif(gender == "2" or "F" or "f" or "Female" or "female"):
        print("Welcome Miss.",name)
    else:
        print("You have entered a wrong value")
        print("Please try again")
        print("Thank you for your time")
        print("Exiting the program")
        exit()
    return True    

# Function to get date of birth
def get_dob():
    print("Please enter your date of birth in YYYYMMDD format")
    print("For example, if your date of birth is 1st January 2000, you should enter 20000101")
    global dob
    dob = input("Enter your Date of Birth (YYYYMMDD):")
    # Clearing the screen after input
    # Clearing the screen after input
    clear_screen()

# Function to validate the date of birth
def validate_dob(dob):
    if len(dob) == 0 :
        print("You haven't entered any value, code terminated")
        exit()
    if len(dob) != 8 :
        print("Try writing your date of birth in YYYYMMDD format")
        exit()    
    if dob.isdigit()== True and len(dob) == 8:
        pass
    elif dob.isdigit() == False :
        print("Try writing your date of birth in YYYYMMDD format")
        exit()
    # if dob[5:6] > 12 or dob[6:8] > 31 or date.year()>dob[0:4] > 1900:
    #     print("Try writing your date of birth in YYYYMMDD format")
    #     exit()


    # Function to extract the year, month, and day from the date of birth

    def extract_dob(dob):
        global year, month, day
        year = int(dob[:4])
        month = int(dob[4:6])
        day = int(dob[6:8])
        return year, month, day        

    # Extracting year, month, and day from the date of birth
    extract_dob(dob)

    if month < 1 or month > 12:
        print("You have entered a wrong date of birth in month")
        exit()
    if day < 1 or day > 31:
        print("You have entered a wrong date of birth in day")
        exit()      
    if month == 2:  
        if day > 29 or (day == 29 and not (year % 4 == 0 and (year % 100 != 0 or year % 400 == 0))):
            print("You have entered a wrong date of birth, February has only 28 days in non-leap years")
            exit()
    if month in [4, 6, 9, 11] and day > 30:
        print("You have entered a wrong date of birth, 04, 06, 09, 11 months have only 30 days")
        exit()
    if year < 1900 or year > date.today().year:
        print("You have entered a wrong date of birth, the year should be between 1900 and the current year")
        exit()
    return True    



# Function to calculate age based on date of birth
def calculate_age(dob):
    today = date.today()
    global age
    age = today.year - year
    if (today.month, today.day) < (month,day):
        age -= 1
    return age

# Function to check eligibility of voting based on age
def eligibility():
    global eligible
    if age < 18:
        print("Your age is:", age)
        eligible = False
    if age>= 18 :
        print("As you are a major, You are eligible to vote.")
        eligible = True

# Function to ask major user to acceptance of applying vote
def acceptance_to_vote():
    if eligible == True :
        print('''Do you want to apply for vote?''')
        print("1)Yes 2)No")
        global acceptance
        acceptance = input()
    elif eligible == False :
        age_left = 18 - age
        if(age_left == 1):
            print("You are not eligible to vote yet.Thank you for your time.Dont't forget to vote after 1 year.")
            exit()
        else:    
            print("You are not eligible to vote yet.Thank you for your time.Dont't forget to vote after",age_left,"years.")
            exit()

def decision():
    if  acceptance == "1" :
        # Clearing the screen after input
        clear_screen()
        print("Enter your details")
    elif acceptance == "2":
        print("You have chosen not to apply for vote")
        print("Thank you for your time")
        exit()       
    else :
        print("Given value is out of range, code terminated")
        exit() 
        

def get_Aadhar():
    global Aadhar
    Aadhar = input("Enter your Aadhar no. :")
    return Aadhar
def get_PAN():
    global PAN
    PAN = input("Enter your PAN no. (use capitals):")
    PAN = PAN.upper()
    # Clearing the screen after input
    clear_screen()
    return PAN
def validate_Aadhar():
    if(Aadhar.isdigit() == False or len(Aadhar) != 12):
        print("You have entered a wrong Aadhar number")
        exit()
    elif Aadhar[0] == '0':
        print("You have entered a wrong Aadhar number")
        exit()    
    # Clearing the screen after input
    clear_screen() 
def validate_PAN():
    if(PAN[0:5].isalpha() == False or PAN[5:9].isdigit() == False or len(PAN) != 10 or PAN[9].isalpha() == False):
        print("You have entered a wrong PAN number")
        exit()
def show():
    print("Name : "+ Fore.CYAN + Style.BRIGHT + name.upper() )
    reset()
    print("Age : " + Fore.CYAN + Style.BRIGHT + str(age))
    reset()
    print("Aadhar : "+ Fore.CYAN + Style.BRIGHT +  Aadhar)
    reset()
    print("PAN : "+ Fore.CYAN + Style.BRIGHT + PAN)
    reset()
    print("Applied : " + Fore.CYAN + Style.BRIGHT + "Yes" )
    reset()  
    print("If You need further info check in google.") 

### Main program starts here

# Getting user's name
get_name()

# Getting user's gender
get_gender()

# Gender validation 
gender_validate(gender)

# Input for date of birth
get_dob()


# Validating the date of birth
validate_dob(dob)

# Calculating age
calculate_age(dob)

# Displaying age and eligibility to vote
eligibility()

#Asking Major user weather if he wants to apply to vote
acceptance_to_vote()

# Validation for voting decision
decision()

# Getting User's Aadhar details and validating them
get_Aadhar()
validate_Aadhar()

# Getting User's PAN details and validating them
get_PAN()
validate_PAN()

# Showing the final details
show()

# Ending the program