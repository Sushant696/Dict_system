import sqlite3
from tkinter import *


# Function to set background color of a frame
def set_background_color(frame, color):
    frame.config(bg=color)

# Function to create the database (users.db) and the 'users' table
def create_database():
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

# Function to insert a new user into the 'users' table
def insert_user(name, email, username, password):
    connection = sqlite3.connect("users.db")
    cursor = connection.cursor()

    cursor.execute('INSERT INTO users (name, email, username, password) VALUES (?, ?, ?, ?)', (name, email, username, password))

    connection.commit()
    connection.close()

# Function to check if a user with the provided username and password exists in the 'users' table
def check_user(username, password):
    connection = sqlite3.connect("users.db")
    cursor = connection.cursor()

    cursor.execute('SELECT * FROM users WHERE username=? AND password=?', (username, password))
    user = cursor.fetchone()

    connection.close()

    return user is not None

# Function to fetch all users from the 'users' table
def fetch_all_users():
    connection = sqlite3.connect("users.db")
    cursor = connection.cursor()

    cursor.execute('SELECT * FROM users')
    users = cursor.fetchall()

    connection.close()

    return users

# Function to create the login window
def create_login_window():
    create_database()

    # Function to handle login button click
    def login_action():
        entered_username = username_entry.get()
        entered_password = password_entry.get()

        if entered_username and entered_password:
            if check_user(entered_username, entered_password):
                result_label.config(text="Login successful.", fg="green")
                # Fetch and display all users
                users = fetch_all_users()
                for user in users:
                    print(user)  # Displaying in console
                create_work_completed_window()
                window.destroy()
            else:
                result_label.config(text="Invalid username or password.", fg="red")
        else:
            result_label.config(text="Please enter both username and password.", fg="red")

    # Function to show or hide password
    def toggle_password_visibility():
        if show_password_var.get():
            password_entry.config(show="")
        else:
            password_entry.config(show="•")

    # Creating the main login window
    window = Tk()
    window.title("Login Page")
    window.geometry("600x500")
    window.resizable(0, 0)

    left_frame = Frame(window, width=300, height=500)
    left_frame.grid(row=0, column=0, sticky="nsew")
    set_background_color(left_frame, "#3D9962")

    label_team = Label(left_frame, text="Project Ignition", font=("Helvetica", 20), bg="#3D9962", fg="white")
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

    show_password_var = BooleanVar()
    show_password_var.set(False)
    show_password_checkbutton = Checkbutton(right_frame, text="Show Password", variable=show_password_var, onvalue=True, offvalue=False, font=("Helvetica", 10), bg="#D9D9D9", fg="#4C5E8C", command=toggle_password_visibility)
    show_password_checkbutton.place(relx=0.5, rely=0.5, anchor="center")

    result_label = Label(right_frame, text="", font=("Helvetica", 12), fg="green", bg="#D9D9D9")
    result_label.place(relx=0.5, rely=0.85, anchor="center")

    login_button = Button(right_frame, text=" Login ", font=("Helvetica", 12), bg="#3D9962", fg="white", command=login_action)
    login_button.place(relx=0.5, rely=0.6, anchor="center")

    window.mainloop()

# Function for opening a new window after successful login
def create_work_completed_window():
    work_completed_window = Toplevel()
    work_completed_window.title("Work Completed Page")
    work_completed_window.geometry("400x300")

    label_work_completed = Label(work_completed_window, text="Congratulations! Your work is completed.", font=("Helvetica", 16))
    label_work_completed.pack(pady=50)

    work_completed_window.mainloop()

# Run the login window
create_login_window()
