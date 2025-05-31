import os
from datetime import date
from colorama import Fore, Style, init, Back

init(autoreset=True)
clear_screen = lambda: os.system('cls' if os.name == 'nt' else 'clear')

'''
print(Fore.CYAN + Style.BRIGHT + "Welcome to the Lucky Fortune Teller!")
print(Style.RESET_ALL)  # Always reset to avoid affecting other text
print(Fore.RED + "This text is red!")
print(Fore.GREEN + "This text is green.")
print(Back.YELLOW + "This text has a yellow background.")
print(Style.BRIGHT + "This is bright style text.")
print(Style.RESET_ALL + "Back to normal text.")
'''
name = input("Enter your name : ")
gender = int(input("Enter your gender \n1)Male \n2)Female: \n"))
clear_screen()
name = name.title()
if(gender == 1):
    print("Welcome Mr.",name)
elif(gender == 2):
    print("Welcome Miss.",name)
from datetime import date
dob = input("Enter your Date of Birth (YYYYMMDD):")
if dob.isdigit()== True and len(dob) == 8:
    num = int(dob)
elif len(dob) != 8 or dob.isdigit() == False:
    print("Try writing your date of birth in YYYYMMDD format")
    exit()    
elif dob[5:6] > 12 or dob[6:8] > 31 or date.year()>dob[0:4] > 1900:
    print("Try writing your date of birth in YYYYMMDD format")
    exit()
year = int(dob[:4])
month = int(dob[4:6])
day = int(dob[6:8])
def calculate_age(dob):
    today = date.today()
    age = today.year - year
    if (today.month, today.day) < (month,day):
        age -= 1
    return age
age = calculate_age(dob)
clear_screen()
if age < 0:
    print("You have entered a wrong date of birth")
    exit()
elif age < 18:
    print("Your age is:", age)
if(age >= 18):   
    print("You are eligible to vote.")
    print(''' D'ye want to apply for vote?''')
    print("1)Yes \n2)No")
    ans = input()
    if(ans == '1'):
        Aadhar = input("Enter your Aadhar no. :")
        if(Aadhar.isdigit() == False or len(Aadhar) != 12):
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