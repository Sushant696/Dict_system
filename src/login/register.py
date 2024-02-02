import sqlite3
from tkinter import *


def set_background_color(frame, color):
    frame.config(bg=color)

def create_registration_database():
    connection = sqlite3.connect("users.db")
    cursor = connection.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT NOT NULL,
            username TEXT NOT NULL,
            password TEXT NOT NULL
        )
    ''')

    connection.commit()
    connection.close()

def insert_registration_user(name, email, username, password):
    connection = sqlite3.connect("users.db")
    cursor = connection.cursor()

    cursor.execute('INSERT INTO users (name, email, username, password) VALUES (?, ?, ?, ?)', (name, email, username, password))

    connection.commit()
    connection.close()

def check_username_availability(username):
    connection = sqlite3.connect("users.db")
    cursor = connection.cursor()

    cursor.execute('SELECT * FROM users WHERE username=?', (username,))
    existing_user = cursor.fetchone()

    connection.close()

    return existing_user is None

def create_registration_window():
    create_registration_database()

    registration_window = Tk()
    registration_window.title("Registration Page")
    registration_window.geometry("600x500")
    registration_window.resizable(0, 0)

    left_frame = Frame(registration_window, width=300, height=500)
    left_frame.grid(row=0, column=0, sticky="nsew")
    set_background_color(left_frame, "#3D9962")

    label_team = Label(left_frame, text="Team Ignition", font=("Helvetica", 20), bg="#3D9962", fg="white")
    label_team.place(relx=0.5, rely=0.5, anchor="center")

    right_frame = Frame(registration_window, width=300, height=500)
    right_frame.grid(row=0, column=1, sticky="nsew")
    set_background_color(right_frame, "#D9D9D9")

    label_signup = Label(right_frame, text="Registration", font=("Helvetica", 20), bg="#D9D9D9", fg="#4C5E8C")
    label_signup.place(relx=0.5, rely=0.1, anchor="center")

    name_label = Label(right_frame, text="Name", font=("Helvetica", 10), bg="#D9D9D9", fg="black")
    name_label.place(relx=0.15, rely=0.25, anchor="center")

    name_entry = Entry(right_frame, font=("Helvetica", 14), bd=4, relief="flat", justify="center")
    name_entry.place(relx=0.6, rely=0.25, anchor="center", width=200)

    email_label = Label(right_frame, text="Email", font=("Helvetica", 10), bg="#D9D9D9", fg="black")
    email_label.place(relx=0.15, rely=0.35, anchor="center")

    email_entry = Entry(right_frame, font=("Helvetica", 14), bd=5, relief="flat", justify="center")
    email_entry.place(relx=0.6, rely=0.35, anchor="center", width=200)

    username_label = Label(right_frame, text="Username", font=("Helvetica", 10), bg="#D9D9D9", fg="black")
    username_label.place(relx=0.15, rely=0.45, anchor="center")

    username_entry = Entry(right_frame, font=("Helvetica", 14), bd=5, relief="flat", justify="center")
    username_entry.place(relx=0.6, rely=0.45, anchor="center", width=200)

    password_label = Label(right_frame, text="Password", font=("Helvetica", 10), bg="#D9D9D9", fg="black")
    password_label.place(relx=0.15, rely=0.55, anchor="center")

    password_entry = Entry(right_frame, font=("Helvetica", 14), bd=5, relief="flat", justify="center", show="•")
    password_entry.place(relx=0.6, rely=0.55, anchor="center", width=200)

    result_label = Label(right_frame, text="", font=("Helvetica", 12), fg="green", bg="#D9D9D9")
    result_label.place(relx=0.5, rely=0.85, anchor="center")

    def registration_action():
        entered_name = name_entry.get()
        entered_email = email_entry.get()
        entered_username = username_entry.get()
        entered_password = password_entry.get()

        if entered_name and entered_email and entered_username and entered_password:
            if not check_username_availability(entered_username):
                result_label.config(text="Username is not available.", fg="red")
            else:
                insert_registration_user(entered_name, entered_email, entered_username, entered_password)
                result_label.config(text="Registration successful.", fg="green")
        else:
            result_label.config(text="Please enter all registration details.", fg="red")

    def switch_to_login_view():
        registration_window.destroy()

    register_button = Button(right_frame, text=" Register ", font=("Helvetica", 12), bg="#3D9962", fg="white", command=registration_action)
    register_button.place(relx=0.5, rely=0.7, anchor="center")

    back_to_login_button = Button(right_frame, text=" Back to Login ", font=("Helvetica", 12), bg="#3D9962", fg="white", command=switch_to_login_view)
    back_to_login_button.place(relx=0.5, rely=0.8, anchor="center")

    registration_window.grid_rowconfigure(0, weight=1)
    registration_window.grid_columnconfigure(0, weight=1)
    registration_window.grid_columnconfigure(1, weight=1)

    registration_window.mainloop()
