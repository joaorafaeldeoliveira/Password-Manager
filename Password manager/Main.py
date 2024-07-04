from tkinter import *




# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generatePassword():
    pass

def add():
    pass

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

#Create the Image on the middle of the GUI
canvas = Canvas(height=200, width=200)
logo_img = PhotoImage(file = "logo.png")
canvas.create_image(100,100,image=logo_img)
canvas.grid(row=0,column=0,columnspan=3)

#Create the Entry Zone
#Website Entry 
websiteLabel = Label(window,text="Website: ")
websiteLabel.grid(row=1,column=0)

websiteEntry = Entry(window,width=40)
websiteEntry.grid(row=1,column=1,columnspan=2)

#User Entry 
userLabel = Label(window,text="E-mail/Username : ")
userLabel.grid(row=2,column = 0)

userEntry = Entry(window,width=40)
userEntry.grid(row=2,column=1,columnspan=2)

#Password Entry
passwordLabel = Label(window,text="Password : ")
passwordLabel.grid(row=3,column = 0)

passwordEntry = Entry(window,width=21)
passwordEntry.grid(row=3,column=1)

generatePassword = Button(text="Generate Password",command= generatePassword)
generatePassword.grid(row=3,column=2,columnspan=2)

#Add button

addButton = Button(text="add",width=36,command=add)
addButton.grid(row=4,column= 1,columnspan=2)



window.mainloop()
