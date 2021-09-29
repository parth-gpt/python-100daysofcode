from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate():
    pass_entry.delete(0, END)
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for char in range(randint(8, 10))]
    password_symbols = [choice(symbols) for char in range(randint(2, 4))]
    password_numbers = [choice(numbers) for char in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)
    pass_entry.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website_data = website_entry.get()
    email_data = email_entry.get()
    password_data = pass_entry.get()

    if website_data == "" or email_data == "" or password_data == "":
        messagebox.showwarning(title="Empty Fields!", message="Empty Fields!\n Please enter required fields.")
    else:
        is_ok = messagebox.askokcancel(title=website_data,
                                       message=f"Have a look at the details entered:\n\n Website: {website_data}\n Email: {email_data}\n Password: {password_data}\n\n Is it Ok to save?")

        if is_ok:
            with open("data.txt", "a") as data:
                data.write(f"{website_data} | {email_data} | {password_data}\n")
                website_entry.delete(0, END)
                pass_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
logo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo)
canvas.grid(column=1, row=0)

website = Label(text="Website:", font=("Arial", 15, "normal"))
website.grid(column=0, row=1)
website.config(padx=50)

website_entry = Entry(width=35)
website_entry.grid(column=1, row=1, columnspan=2)
website_entry.focus()

email = Label(text="Email/Username:", font=("Arial", 15, "normal"))
email.grid(column=0, row=2)

email_entry = Entry(width=35)
email_entry.grid(column=1, row=2, columnspan=2)
email_entry.insert(0, "parth@gmail.com")

password = Label(text="Password:", font=("Arial", 15, "normal"))
password.grid(column=0, row=3)
password.config(padx=30)

pass_entry = Entry(width=21)
pass_entry.grid(column=1, row=3)

button = Button(text="Generate Password", command=generate)
button.grid(column=2, row=3)

button = Button(text="Add", width=36, command=save)
button.grid(column=1, row=4, columnspan=2)

window.mainloop()
