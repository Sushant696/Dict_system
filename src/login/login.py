import sqlite3
from tkinter import *

def set_background_color(frame, color):
    frame.config(bg=color)

def create_database():
    connection = sqlite3.connect("users.db")
    cursor = connection.cursor()

    # Create a table for users
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

    # Insert user into the table
    cursor.execute('INSERT INTO users (username, password) VALUES (?, ?)', (username, password))

    connection.commit()
    connection.close()

def check_user(username, password):
    connection = sqlite3.connect("users.db")
    cursor = connection.cursor()

    # Check if the entered username and password exist in the table
    cursor.execute('SELECT * FROM users WHERE username=? AND password=?', (username, password))
    user = cursor.fetchone()

    connection.close()

    return user is not None

def create_login_registration_window():
    create_database()  # Create the database if it doesn't exist

    window = Tk()
    window.title("Login and Registration Page")
    window.geometry("600x500")
    window.resizable(0, 0)  # Disable window resizing

    # Create a frame for the left half (green color)
    left_frame = Frame(window, width=300, height=500)
    left_frame.grid(row=0, column=0, sticky="nsew")
    set_background_color(left_frame, "#3D9962")  # Green color
    
    label_team = Label(left_frame, text="Team Ignition", font=("Helvetica", 20), bg="#3D9962", fg="white")
    label_team.place(relx=0.5, rely=0.5, anchor="center")

    # Create a frame for the right half (gray color)
    right_frame = Frame(window, width=300, height=500)
    right_frame.grid(row=0, column=1, sticky="nsew")
    set_background_color(right_frame, "#D9D9D9")  # Gray color

    label_signup = Label(right_frame, text="Sign Up", font=("Helvetica", 20), bg="#D9D9D9", fg="#4C5E8C")
    label_signup.place(relx=0.5, rely=0.1, anchor="center")
    
    # Username label and entry in the same line
    username_label = Label(right_frame, text="Username", font=("Helvetica", 10), bg="#D9D9D9", fg="black")
    username_label.place(relx=0.15, rely=0.30, anchor="center")

    global username_entry
    username_entry = Entry(right_frame, font=("Helvetica", 14), bd=4, relief="flat", justify="center")
    username_entry.place(relx=0.6, rely=0.30, anchor="center", width=200)

    # Password label
    password_label = Label(right_frame, text="Password", font=("Helvetica", 10), bg="#D9D9D9", fg="black")
    password_label.place(relx=0.15, rely=0.40, anchor="center")

    global password_entry
    password_entry = Entry(right_frame, font=("Helvetica", 14), bd=5, relief="flat", justify="center", show="•")
    password_entry.place(relx=0.6, rely=0.40, anchor="center", width=200)

    result_label = Label(right_frame, text="", font=("Helvetica", 12), fg="green", bg="#D9D9D9")
    result_label.place(relx=0.5, rely=0.85, anchor="center")

    def login_action():
        entered_username = username_entry.get()
        entered_password = password_entry.get()

        if entered_username and entered_password:
            # Check if the entered username and password are valid
            if check_user(entered_username, entered_password):
                result_label.config(text="Login successful.", fg="green")
                create_work_completed_window()  # Open the "My work is completed" window
            else:
                result_label.config(text="Invalid username or password.", fg="red")
        else:
            result_label.config(text="Please enter both username and password.", fg="red")

    def register_action():
        # Switch to registration view
        label_signup.config(text="Register", fg="black")
        login_button.config(command=register_user)
        register_button.config(text="R", command=switch_to_login_view)

    def switch_to_login_view():
        # Switch to login view
        label_signup.config(text="Sign Up", fg="#4C5E8C")
        login_button.config(command=login_action)
        register_button.config(text=" Register ", command=register_action)
        clear_entries()

    def clear_entries():
        username_entry.delete(0, 'end')
        password_entry.delete(0, 'end')
        result_label.config(text="")

    def register_user():
        new_username = username_entry.get()
        new_password = password_entry.get()

        if new_username and new_password:
            # Check if username already exists
            if check_user(new_username, new_password):
                result_label.config(text="Username already exists. Please choose another.", fg="red")
            else:
                # Insert the new user into the database
                insert_user(new_username, new_password)
                result_label.config(text="User registered successfully.", fg="green")
                switch_to_login_view()  # Switch back to login view after successful registration
        else:
            result_label.config(text="Please enter both username and password.", fg="red")

    def create_work_completed_window():
        # Create a new window for "My work is completed" message
        work_completed_window = Toplevel(window)
        work_completed_window.title("Work Completed")
        work_completed_window.geometry("300x200")

        # Label in the new window
        work_completed_label = Label(work_completed_window, text="My work is completed.", font=("Helvetica", 16), fg="green")
        work_completed_label.pack(pady=50)

    # Login button
    login_button = Button(right_frame, text=" Login ", font=("Helvetica", 12), bg="#3D9962", fg="white", command=login_action)
    login_button.place(relx=0.3, rely=0.7, anchor="center")
    
    # Register button
    register_button = Button(right_frame, text=" Register ", font=("Helvetica", 12), bg="#3D9962", fg="white", command=register_action)
    register_button.place(relx=0.6, rely=0.7, anchor="center")

    # Make the frames expand to fill the window
    window.grid_rowconfigure(0, weight=1)
    window.grid_columnconfigure(0, weight=1)
    window.grid_columnconfigure(1, weight=1)

    window.mainloop()

# Create and run the window
create_login_registration_window()
