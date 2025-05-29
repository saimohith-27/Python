name = input("Enter your name : ")
gender = int(input("Enter your gender \n1)Male \n2)Female: \n"))
if(gender == 1):
    print("Welcome Mr.",name)
elif(gender == 2):
    print("Welcome Miss.",name)
age = int(input("Enter your age: "))

if(age >= 18):   
    print("You are eligible to vote.")
    print(''' D'ye want to apply for vote?''')
    print("1)Yes \n2)No")
    ans = input()
    
    if(ans == '1'):
        Aadhar = input("Enter your Aadhar no. :")
        print("You have successfully applied for vote")
    elif(ans == '2'):
        print("Thank you for your time")
    else:
        print("You entered a wrong answer, code terminated")
else: 
    age_left = 18 - age
    if(age_left == 1):
        print("You are not eligible to vote yet.Thank you for your time.Dont't forget to vote after 1 year.")
    else:    
        print("You are not eligible to vote yet.Thank you for your time.Dont't forget to vote after",age_left,"years.")