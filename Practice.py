import tkinter as tk
from tkinter import messagebox
from datetime import date

# Initialize global variables
name = gender = dob = Aadhar = PAN = ""
year = month = day = age = 0
eligible = False

def reset_fields():
    name_entry.delete(0, tk.END)
    gender_var.set("")
    dob_entry.delete(0, tk.END)
    aadhar_entry.delete(0, tk.END)
    pan_entry.delete(0, tk.END)

def validate_and_extract_dob(dob_input):
    global year, month, day
    if len(dob_input) != 8 or not dob_input.isdigit():
        messagebox.showerror("Invalid DOB", "Enter DOB in YYYYMMDD format.")
        return False
    try:
        year = int(dob_input[:4])
        month = int(dob_input[4:6])
        day = int(dob_input[6:8])
        date(year, month, day)
    except ValueError:
        messagebox.showerror("Invalid DOB", "Invalid date. Please check month and day.")
        return False
    if year < 1900 or year > date.today().year:
        messagebox.showerror("Invalid DOB", "Year should be between 1900 and current year.")
        return False
    return True

def calculate_age():
    global age
    today = date.today()
    age = today.year - year
    if (today.month, today.day) < (month, day):
        age -= 1
    return age

def check_eligibility():
    global name, gender, dob, Aadhar, PAN, eligible
    name = name_entry.get().strip().title()
    gender = gender_var.get()
    dob = dob_entry.get().strip()
    Aadhar = aadhar_entry.get().strip()
    PAN = pan_entry.get().strip().upper()

    if not name or not dob or not Aadhar or not PAN:
        messagebox.showwarning("Input Error", "All fields are required.")
        return
    if not gender:
        messagebox.showwarning("Input Error", "Select any one option")
        return
    if not validate_and_extract_dob(dob):
        return

    calculate_age()

    if age < 18:
        eligible = False
        age_left = 18 - age
        msg = "You are NOT eligible to vote.\nTry after {} year(s).".format(age_left)
        messagebox.showinfo("Result", msg)
        return
    else:
        eligible = True

    if not (Aadhar.isdigit() and len(Aadhar) == 12 and Aadhar[0] != '0'):
        messagebox.showerror("Invalid Aadhar", "Aadhar must be a 12-digit number not starting with 0.")
        return

    if not (len(PAN) == 10 and PAN[:5].isalpha() and PAN[5:9].isdigit() and PAN[9].isalpha()):
        messagebox.showerror("Invalid PAN", "PAN format should be: 5 letters, 4 digits, 1 letter (e.g., ABCDE1234F).")
        return

    confirm_vote_application()

def confirm_vote_application():
    response = messagebox.askyesno("Apply to Vote", "You are eligible to vote.\nDo you want to apply?")
    if response:
        show_summary()
    else:
        messagebox.showinfo("Exit", "You chose not to apply. Thank you!")

def show_summary():
    summary = f"""
    Name   : {name.upper()}
    Age    : {age}
    Aadhar : {Aadhar}
    PAN    : {PAN}
    Applied: ( ͡° ͜ʖ ͡°)

    You may check your application status on official government sites.
    """
    messagebox.showinfo("Application Submitted", summary)
    reset_fields()

# GUI setup
window = tk.Tk()
window.title("Voting Eligibility Checker")
window.geometry("400x450")

tk.Label(window, text="Enter your name:").pack()
name_entry = tk.Entry(window)
name_entry.pack()

tk.Label(window, text="Select your gender:").pack()
gender_var = tk.StringVar()
tk.Radiobutton(window, text="Male", variable=gender_var, value="Male").pack()
tk.Radiobutton(window, text="Female", variable=gender_var, value="Female").pack()

tk.Label(window, text="Enter your DOB (YYYYMMDD):").pack()
dob_entry = tk.Entry(window)
dob_entry.pack()

tk.Label(window, text="Enter your Aadhar number:").pack()
aadhar_entry = tk.Entry(window)
aadhar_entry.pack()

tk.Label(window, text="Enter your PAN number:").pack()
pan_entry = tk.Entry(window)
pan_entry.pack()

tk.Button(window, text="Check Eligibility", command=check_eligibility).pack(pady=10)

window.mainloop()
