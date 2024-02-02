import sqlite3
from tkinter import *

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

def create_login_window():
    create_database()

    window = Tk()
    window.title("Login Page")
    window.geometry("600x500")
    window.resizable(0, 0)

    left_frame = Frame(window, width=300, height=500)
    left_frame.grid(row=0, column=0, sticky="nsew")
    set_background_color(left_frame, "#3D9962")

    label_team = Label(left_frame, text="Team Ignition", font=("Helvetica", 20), bg="#3D9962", fg="white")
    label_team.place(relx=0.5, rely=0.5, anchor="center")

    right_frame = Frame(window, width=300, height=500)
    right_frame.grid(row=0, column=1, sticky="nsew")
    set_background_color(right_frame, "#D9D9D9")

    label_signup = Label(right_frame, text="Login", font=("Helvetica", 20), bg="#D9D9D9", fg="#4C5E8C")
    label_signup.place(relx=0.5, rely=0.1, anchor="center")

    username_label = Label(right_frame, text="Username", font=("Helvetica", 10), bg="#D9D9D9", fg="black")
    username_label.place(relx=0.15, rely=0.30, anchor="center")

    username_entry = Entry(right_frame, font=("Helvetica", 14), bd=4, relief="flat", justify="center")
    username_entry.place(relx=0.6, rely=0.30, anchor="center", width=200)

    password_label = Label(right_frame, text="Password", font=("Helvetica", 10), bg="#D9D9D9", fg="black")
    password_label.place(relx=0.15, rely=0.40, anchor="center")

    password_entry = Entry(right_frame, font=("Helvetica", 14), bd=5, relief="flat", justify="center", show="•")
    password_entry.place(relx=0.6, rely=0.40, anchor="center", width=200)

    result_label = Label(right_frame, text="", font=("Helvetica", 12), fg="green", bg="#D9D9D9")
    result_label.place(relx=0.5, rely=0.85, anchor="center")

    def login_action():
        entered_username = username_entry.get()
        entered_password = password_entry.get()

        if entered_username and entered_password:
            if check_user(entered_username, entered_password):
                result_label.config(text="Login successful.", fg="green")
                create_work_completed_window()
                window.destroy()
            else:
                result_label.config(text="Invalid username or password.", fg="red")
        else:
            result_label.config(text="Please enter both username and password.", fg="red")

    def register_action():
        create_registration_window()
        window.destroy()

    login_button = Button(right_frame, text=" Login ", font=("Helvetica", 12), bg="#3D9962", fg="white", command=login_action)
    login_button.place(relx=0.3, rely=0.7, anchor="center")

    register_button = Button(right_frame, text="Register ", font=("Helvetica", 12), bg="#3D9962", fg="white", command=register_action)
    register_button.place(relx=0.7, rely=0.7, anchor="center")

    window.grid_rowconfigure(0, weight=1)
    window.grid_columnconfigure(0, weight=1)
    window.grid_columnconfigure(1, weight=1)

    window.mainloop()

# Function for opening a new window after successful login
def create_work_completed_window():
    work_completed_window = Tk()
    work_completed_window.title("Work Completed Page")
    work_completed_window.geometry("400x300")

    label_work_completed = Label(work_completed_window, text="Congratulations! Your work is completed.", font=("Helvetica", 16))
    label_work_completed.pack(pady=50)

    work_completed_window.mainloop()

# Function to create registration window
def create_registration_window():
    # Include your registration window creation code here
    pass

# Run the login window
create_login_window()
