from tkinter import *
from tkinter import messagebox
import generatepassword
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
import random
def generatepassword():
   
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = []

    for char in range(nr_letters):
        password_list.append(random.choice(letters))

    for char in range(nr_symbols):
        password_list += random.choice(symbols)

    for char in range(nr_numbers):
        password_list += random.choice(numbers)

    random.shuffle(password_list)

    password = ""
    for char in password_list:
        password += char

    password_entry.insert(0, password)
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():

    website = website_entry.get()  
    email = email_entry.get()
    password = password_entry.get()

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Opps", message="Please make sure you haven`t left any fields empty")
    else:
        is_ok = messagebox.askokcancel(title=website,message=f"These are the details entered: \nEmail: {email}"
                            f"\nPassword: {password} \n Is it ok to save ? ")
        if is_ok:
            with open("data.txt","a") as data_file:
                data_file.write(f"{website} | {email} | {password}\n")
                website_entry.delete(0, END)
                password_entry.delete(0, END)
    
    
# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

#Create the Image on the middle of the GUI
canvas = Canvas(height=200, width=200)
logo_img = PhotoImage(file = "logo.png")
canvas.create_image(100, 100,image=logo_img)
canvas.grid(row=0,column=1,columnspan=2)

#Labels 
website_label = Label(text="Website:")
website_label.grid(row=1,column=0)
email_label = Label(text="Email/Username : ")
email_label.grid(row=2,column=0)
passwrod_label = Label(text="Password : ")
passwrod_label.grid(row=3,column=0)

#Entries
website_entry = Entry(window,width=40)
website_entry.grid(row=1,column=1,columnspan=2)
website_entry.focus()
email_entry  = Entry(window,width=40)
email_entry.grid(row=2,column=1,columnspan=2)
email_entry.insert(0,"jrojoao@gmail.com")
password_entry = Entry(window,width=21)
password_entry.grid(row=3,column=1)

#Buttons
generate_password_button = Button(text="Generate Password",command=generatepassword)
generate_password_button.grid(row=3,column=2,columnspan=2)
add_button = Button(text="Add",width=36,command=save)
add_button.grid(row=4,column=1,columnspan=2)


window.mainloop()