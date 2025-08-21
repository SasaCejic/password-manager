from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json

FONT_NAME = "Arial"
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)


    letters_list = [random.choice(letters) for char in range(nr_letters)]


    symbols_list = [random.choice(symbols) for char in range(nr_symbols)]


    numbers_list = [random.choice(numbers) for char in range(nr_numbers)]

    password_list = letters_list + symbols_list + numbers_list

    random.shuffle(password_list)

    password = "".join(password_list)

    password_entry.delete(first=0, last=END)
    password_entry.insert(index=0, string=password)

    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():

    new_data = {
        website_entry.get():
            {
                "email": username_entry.get(),
                "password": password_entry.get()
            }
    }

    if website_entry.get() == "" or username_entry.get() == "" or password_entry.get() == "":
        messagebox.showerror(title="Oops", message="Don't leave any of the entries blank!")
    else:
        try:
            with open("data.json", mode="r") as file:
                data = json.load(file)
        except FileNotFoundError:
            with open("data.json", mode="w") as file:
                json.dump(new_data, file, indent=4)
        else:
            data.update(new_data)
            with open("data.json", mode="w") as file:
                json.dump(data, file, indent=4)
        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)

# ---------------------------- SEARCH ------------------------------- #
def search():
    try:
        with open("data.json", mode="r") as file:
            data = json.load(file)
    except FileNotFoundError:
        messagebox.showerror(title="Oops", message="No Data File Found.")
    else:
        if website_entry.get() in data:
            message_to_show = (f"Email: {data[website_entry.get()]['email']}\n"
                               f"Password: {data[website_entry.get()]['password']}")
            messagebox.showinfo(title=website_entry.get(), message=message_to_show)
        else:
            messagebox.showerror(title="Oops", message="There is no info about this website.")

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(width=500, height=500, padx=50, pady=50)

canvas = Canvas(width=200, height=200)
photo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=photo)
canvas.grid(column=1, row=0)

website_label = Label(text="Website:")
website_label.grid(column=0, row=1, padx=5, pady=5)

website_entry = Entry(width=21)
website_entry.grid(column=1, row = 1, sticky="WE", padx=5, pady=5)
website_entry.focus()

search_button = Button(text="Search", width=13, command=search, border=1)
search_button.grid(row=1, column=2, sticky="WE", padx=5, pady=5)

username_label = Label(text="Email/Username:")
username_label.grid(column=0, row=2, padx=5, pady=5)

username_entry = Entry(width=35)
username_entry.insert(0, "cejicsasa17@gmail.com")
username_entry.grid(column=1, row=2, columnspan=2, sticky="WE", padx=5, pady=5)

password_label = Label(text="Password:")
password_label.grid(column=0, row=3, padx=5, pady=5)

password_entry = Entry(width=21)
password_entry.grid(column=1, row=3, sticky="WE", padx=5, pady=5)

generate_password_button = Button(text="Generate Password", command=generate_password, border=1)
generate_password_button.grid(column=2, row=3, sticky="WE", padx=5, pady=5)

add_button = Button(text="Add", width=36, command=save, border=1)
add_button.grid(column=1, row=4, columnspan=2, sticky="WE", padx=5, pady=5)

window.mainloop()