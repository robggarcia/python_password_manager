# Password Manager

from tkinter import *
from tkinter import messagebox

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #


def add_password():
    website = web_entry.get()
    user = user_entry.get()
    password = pass_entry.get()

    # create a message box for the user
    is_ok = messagebox.askokcancel(
        title=website, message=f"These are the details entered:\n{user}\n{password}\nIs it OK to save?")

    if is_ok:
        with open("data.txt", "a") as my_file:
            my_file.write(f"{website} | {user} | {password}\n")
        website = web_entry.delete(0, END)
        password = pass_entry.delete(0, END)

# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
lock_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=lock_img)
canvas.grid(row=0, column=1)

# website
web_label = Label(text="Website:").grid(row=1, column=0)
web_entry = Entry(width=35)
web_entry.focus()
web_entry.grid(row=1, column=1, columnspan=2)

# email/username
user_label = Label(text="Email/Username:").grid(row=2, column=0)
user_entry = Entry(width=35)
user_entry.insert(0, "robgordongarcia@gmail.com")
user_entry.grid(row=2, column=1, columnspan=2)
# password
pass_label = Label(text="Password:").grid(row=3, column=0)
pass_entry = Entry(width=18)
pass_entry.grid(row=3, column=1)
pass_button = Button(text="Generate Password").grid(
    row=3, column=2)
# add
add_button = Button(text="Add", width=33, command=add_password).grid(
    row=4, column=1, columnspan=2)

window.mainloop()
