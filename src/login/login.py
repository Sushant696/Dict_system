import re
import tkinter as tk
from tkinter import messagebox
import sqlite3

def set_background_color(frame, color):
    frame.config(bg=color)

def create_database():
    connection = sqlite3.connect("users.db")
    cursor = connection.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL,
            password TEXT NOT NULL
        )
    ''')

    connection.commit()
    connection.close()

def insert_user(username, password):
    connection = sqlite3.connect("users.db")
    cursor = connection.cursor()

    cursor.execute('INSERT INTO users (username, password) VALUES (?, ?)', (username, password))

    connection.commit()
    connection.close()

def check_user(username, password):
    connection = sqlite3.connect("users.db")
    cursor = connection.cursor()

    cursor.execute('SELECT * FROM users WHERE username=? AND password=?', (username, password))
    user = cursor.fetchone()

    connection.close()

    return user is not None

def fetch_all_users():
    connection = sqlite3.connect("users.db")
    cursor = connection.cursor()

    cursor.execute('SELECT * FROM users')
    users = cursor.fetchall()

    connection.close()

    return users

def toggle_password_visibility(entry_widget, visibility_var):
    if visibility_var.get():
        entry_widget.config(show="")
    else:
        entry_widget.config(show="•")

def create_login_window():
    create_database()

    def login_action():
        entered_username = username_entry.get()
        entered_password = password_entry.get()
        if entered_username and entered_password:
            if check_user(entered_username, entered_password):
                result_label.config(text="Login successful.", fg="green")
                users = fetch_all_users()
                for user in users:
                    print(user)
                create_work_completed_window()
                window.destroy()
            else:
                result_label.config(text="Invalid username or password.", fg="red")
        else:
            result_label.config(text="Please enter both username and password.", fg="red")
    window = tk.Tk()
    window.title("Login Page")
    window.geometry("600x500")
    window.resizable(0, 0)

    left_frame = tk.Frame(window, width=300, height=500)
    left_frame.grid(row=0, column=0, sticky="nsew")
    set_background_color(left_frame, "#3D9962")

    label_team = tk.Label(left_frame, text="Project Ignition", font=("Helvetica", 20), bg="#3D9962", fg="white")
    label_team.place(relx=0.5, rely=0.5, anchor="center")

    right_frame = tk.Frame(window, width=300, height=500)
    right_frame.grid(row=0, column=1, sticky="nsew")
    set_background_color(right_frame, "#D9D9D9")

    label_signup = tk.Label(right_frame, text="Login", font=("Helvetica", 20), bg="#D9D9D9", fg="#4C5E8C")
    label_signup.place(relx=0.5, rely=0.1, anchor="center")

    username_label = tk.Label(right_frame, text="Username", font=("Helvetica", 10), bg="#D9D9D9", fg="black")
    username_label.place(relx=0.15, rely=0.30, anchor="center")

    username_entry = tk.Entry(right_frame, font=("Helvetica", 14), bd=4, relief="flat", justify="center")
    username_entry.place(relx=0.6, rely=0.30, anchor="center", width=200)

    password_label = tk.Label(right_frame, text="Password", font=("Helvetica", 10), bg="#D9D9D9", fg="black")
    password_label.place(relx=0.15, rely=0.40, anchor="center")

    password_entry = tk.Entry(right_frame, font=("Helvetica", 14), bd=5, relief="flat", justify="center", show="•")
    password_entry.place(relx=0.6, rely=0.40, anchor="center", width=200)

    password_visibility_var = tk.BooleanVar()
    password_visibility_check = tk.Checkbutton(right_frame, text="Show Password", variable=password_visibility_var,
                                                command=lambda: toggle_password_visibility(password_entry, password_visibility_var),
                                                bg="#D9D9D9", fg="black", selectcolor="#D9D9D9")
    password_visibility_check.place(relx=0.5, rely=0.5, anchor="center")

    result_label = tk.Label(right_frame, text="", font=("Helvetica", 12), fg="green", bg="#D9D9D9")
    result_label.place(relx=0.5, rely=0.85, anchor="center")

    def switch_to_registration_view():
        registration_window.deiconify()
        window.withdraw()

    registration_button = tk.Button(right_frame, text=" Register ", font=("Helvetica", 12), bg="#3D9962", fg="white", command=switch_to_registration_view)
    registration_button.place(relx=0.5, rely=0.7, anchor="center")

    login_button = tk.Button(right_frame, text=" Login ", font=("Helvetica", 12), bg="#3D9962", fg="white", command=login_action)
    login_button.place(relx=0.5, rely=0.8, anchor="center")

    window.grid_rowconfigure(0, weight=1)
    window.grid_columnconfigure(0, weight=1)
    window.grid_columnconfigure(1, weight=1)

def switch_to_login_view():
    global window
    registration_window.withdraw()
    window.deiconify()

    registration_back_to_login_button = tk.Button(registration_right_frame, text=" Back to Login ", font=("Helvetica", 12), bg="#3D9962", fg="white", command=switch_to_login_view)
    registration_back_to_login_button.place(relx=0.5, rely=0.8, anchor="center")

    def registration_action():
        name = registration_name_entry.get()
        email = registration_email_entry.get()
        username = registration_username_entry.get()
        password = registration_password_entry.get()
        retyped_password = registration_retype_password_entry.get()

        if name and email and username and password and retyped_password:
            if password == retyped_password:
                insert_user(username, password)
                registration_result_label.config(text="User has been registered successfully.", fg="green")
            else:
                registration_result_label.config(text="Passwords do not match. Please retype the password.", fg="red")
        else:
            registration_result_label.config(text="Please fill in all fields.", fg="red")

    registration_register_button = tk.Button(registration_right_frame, text=" Register ", font=("Helvetica", 12), bg="#3D9962", fg="white", command=registration_action)
    registration_register_button.place(relx=0.5, rely=0.9, anchor="center")

    registration_window.grid_rowconfigure(0, weight=1)
    registration_window.grid_columnconfigure(0, weight=1)
    registration_window.grid_columnconfigure(1, weight=1)

registration_window = tk.Tk()
registration_window.title("Registration Page")
registration_window.geometry("600x500")
registration_window.resizable(0, 0)
registration_window.withdraw()

registration_left_frame = tk.Frame(registration_window, width=300, height=500)
registration_left_frame.grid(row=0, column=0, sticky="nsew")

registration_label_team = tk.Label(registration_left_frame, text="Project Ignition", font=("Helvetica", 20), bg="#3D9962", fg="white")
registration_label_team.place(relx=0.5, rely=0.5, anchor="center")

registration_right_frame = tk.Frame(registration_window, width=300, height=500)
registration_right_frame.grid(row=0, column=1, sticky="nsew")

registration_label_signup = tk.Label(registration_right_frame, text="Registration", font=("Helvetica", 20), bg="#D9D9D9", fg="#4C5E8C")
registration_label_signup.place(relx=0.5, rely=0.1, anchor="center")

registration_name_label = tk.Label(registration_right_frame, text="Name", font=("Helvetica", 10), bg="#D9D9D9", fg="black")
registration_name_label.place(relx=0.15, rely=0.25, anchor="center")

registration_name_entry = tk.Entry(registration_right_frame, font=("Helvetica", 14), bd=4, relief="flat", justify="center")
registration_name_entry.place(relx=0.6, rely=0.25, anchor="center", width=200)

registration_email_label = tk.Label(registration_right_frame, text="Email", font=("Helvetica", 10), bg="#D9D9D9", fg="black")
registration_email_label.place(relx=0.15, rely=0.35, anchor="center")

validate_email_command = registration_window.register(validate_email)
registration_email_entry = tk.Entry(registration_right_frame, font=("Helvetica", 14), bd=5, relief="flat", justify="center", validate="focusout", validatecommand=(validate_email_command, '%P'))
registration_email_entry.place(relx=0.6, rely=0.35, anchor="center", width=200)

registration_username_label = tk.Label(registration_right_frame, text="Username", font=("Helvetica", 10), bg="#D9D9D9", fg="black")
registration_username_label.place(relx=0.15, rely=0.45, anchor="center")

registration_username_entry = tk.Entry(registration_right_frame, font=("Helvetica", 14), bd=5, relief="flat", justify="center")
registration_username_entry.place(relx=0.6, rely=0.45, anchor="center", width=200)

registration_password_label = tk.Label(registration_right_frame, text="Password", font=("Helvetica", 10), bg="#D9D9D9", fg="black")
registration_password_label.place(relx=0.15, rely=0.55, anchor="center")

registration_password_entry = tk.Entry(registration_right_frame, font=("Helvetica", 14), bd=5, relief="flat", justify="center", show="•")
registration_password_entry.place(relx=0.6, rely=0.55, anchor="center", width=200)

registration_retype_password_label = tk.Label(registration_right_frame, text="Retype-Pass", font=("Helvetica", 9), bg="#D9D9D9", fg="black")
registration_retype_password_label.place(relx=0.15, rely=0.65, anchor="center")

registration_retype_password_entry = tk.Entry(registration_right_frame, font=("Helvetica", 14), bd=5, relief="flat", justify="center", show="•")
registration_retype_password_entry.place(relx=0.6, rely=0.65, anchor="center", width=200)

registration_result_label = tk.Label(registration_right_frame, text="", font=("Helvetica", 12), fg="green", bg="#D9D9D9")
registration_result_label.place(relx=0.5, rely=0.85, anchor="center")

create_login_window()
registration_window.mainloop()
