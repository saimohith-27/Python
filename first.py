# Importing required libraries

import os
from datetime import date
from colorama import Fore, Style, init, Back

# Initialize colorama

init(autoreset=True)

# Function to clear the console screen
clear_screen = lambda: os.system('cls' if os.name == 'nt' else 'clear')


# Function to calculate age from date of birth
def calculate_age(dob):
    today = date.today()
    age = today.year - year
    if (today.month, today.day) < (month,day):
        age -= 1
    return age

# Main program starts here
print(Fore.RED + "________________________________________________________________________")
name = input("Enter your name : ")
gender = int(input("Enter your gender \n1)Male 2)Female: \n"))
clear_screen()
name = name.title()
print(Fore.RED + "________________________________________________________________________")

# Input validation

if(gender == 1):
    print("Welcome Mr.",name)
elif(gender == 2):
    print("Welcome Miss.",name)
else:
    print("You have entered a wrong value")
    print("Please try again")
    print("Thank you for your time")
    print(Fore.RED + "________________________________________________________________________")
    exit()   

# Input for date of birth

dob = input("Enter your Date of Birth (YYYYMMDD):")

# Input validation for date of birth
if dob.isdigit()== True and len(dob) == 8:
    num = int(dob)
elif len(dob) != 8 or dob.isdigit() == False:
    print("Try writing your date of birth in YYYYMMDD format")
    print(Fore.RED + "________________________________________________________________________")
    exit()    
elif dob[5:6] > 12 or dob[6:8] > 31 or date.year()>dob[0:4] > 1900:
    print("Try writing your date of birth in YYYYMMDD format")
    exit()

# Extracting year, month, and day from the date of birth
    
year = int(dob[:4])
month = int(dob[4:6])
day = int(dob[6:8])
age = calculate_age(dob)
clear_screen()

# Validating the date of birth

if month < 1 or month > 12:
    print("You have entered a wrong date of birth in month")
    print(Fore.RED + "________________________________________________________________________")
    exit()
if day < 1 or day > 31:
    print("You have entered a wrong date of birth in day")
    print(Fore.RED + "________________________________________________________________________")
    exit()      
if month == 2:  
    if day > 29 or (day == 29 and not (year % 4 == 0 and (year % 100 != 0 or year % 400 == 0))):
        print("You have entered a wrong date of birth, February has only 28 days in non-leap years")
        print(Fore.RED + "________________________________________________________________________")
        exit()
if month in [4, 6, 9, 11] and day > 30:
    print("You have entered a wrong date of birth, 04, 06, 09, 11 months have only 30 days")
    print(Fore.RED + "________________________________________________________________________")
    exit()
if year < 1900 or year > date.today().year:
    print("You have entered a wrong date of birth, the year should be between 1900 and the current year")
    print(Fore.RED + "________________________________________________________________________")
    exit()




# Displaying age and eligibility for voting

if age < 0:
    print("You have entered a wrong date of birth")
    exit()
elif age < 18:
    print("Your age is:", age)
if(age >= 18):   
    print(Fore.RED + "________________________________________________________________________")
    print("You are eligible to vote.")
    print(''' D'ye want to apply for vote?''')
    print("1)Yes \n2)No")
    ans = input()
    if(ans == '1'):
        clear_screen()
        Aadhar = input("Enter your Aadhar no. :")
        if(Aadhar.isdigit() == False or len(Aadhar) != 12):
            print("You have entered a wrong Aadhar number")
            exit()
        elif Aadhar[0] == '0':
            print("You have entered a wrong Aadhar number")
            exit()    
        clear_screen()    
        print("You have successfully applied for vote")   
    elif(ans == '2'):
        clear_screen()
        print("You have chosen not to apply for vote")
        print("Thank you for your time")
    else:
        clear_screen()
        print("You entered a wrong answer")
        exit()
else: 
    age_left = 18 - age
    if(age_left == 1):
        print("You are not eligible to vote yet.Thank you for your time.Dont't forget to vote after 1 year.")
    else:    
        print("You are not eligible to vote yet.Thank you for your time.Dont't forget to vote after",age_left,"years.")












'''
print(Fore.CYAN + Style.BRIGHT + "Welcome to the Lucky Fortune Teller!")
print(Style.RESET_ALL)  # Always reset to avoid affecting other text
print(Fore.RED + "This text is red!")
print(Fore.GREEN + "This text is green.")
print(Back.YELLOW + "This text has a yellow background.")
print(Style.BRIGHT + "This is bright style text.")
print(Style.RESET_ALL + "Back to normal text.")
'''