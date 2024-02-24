<<<<<<< HEAD
from tkinter import *

def set_background_color(frame, color):
    frame.config(bg=color)

def create_window():
    window = Tk()
    window.title("Green and Gray Window")
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

    label_signup = Label(right_frame, text="Sign Up", font=("Helvetica", 20), bg="#D9D9D9", fg="black")
    label_signup.place(relx=0.5, rely=0.1, anchor="center")
    
    # Username label and entry in the same line
=======
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
            username TEXT NOT NULL,
            password TEXT NOT NULL
        )
    ''')

    connection.commit()
    connection.close()

# Function to insert a new user into the 'users' table
def insert_user(username, password):
    connection = sqlite3.connect("users.db")
    cursor = connection.cursor()

    cursor.execute('INSERT INTO users (username, password) VALUES (?, ?)', (username, password))

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
                create_work_completed_window()
                window.destroy()
            else:
                result_label.config(text="Invalid username or password.", fg="red")
        else:
            result_label.config(text="Please enter both username and password.", fg="red")

    # Creating the main login window
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

>>>>>>> f59557e60a1926577ec6be0f68fa1e0d60fc7fda
    username_label = Label(right_frame, text="Username", font=("Helvetica", 10), bg="#D9D9D9", fg="black")
    username_label.place(relx=0.15, rely=0.30, anchor="center")

    username_entry = Entry(right_frame, font=("Helvetica", 14), bd=4, relief="flat", justify="center")
    username_entry.place(relx=0.6, rely=0.30, anchor="center", width=200)

<<<<<<< HEAD
    # Password label
    password_label = Label(right_frame, text="Password", font=("Helvetica", 10), bg="#D9D9D9", fg="black")
    password_label.place(relx=0.15, rely=0.40, anchor="center")

    # Password entry
    password_entry = Entry(right_frame, font=("Helvetica", 14), bd=5, relief="flat", justify="center", show="•")
    password_entry.place(relx=0.6, rely=0.40, anchor="center", width=200)

    # Login button
    login_button = Button(right_frame, text=" Login ", font=("Helvetica", 12), bg="#3D9962", fg="white", command=login_action)
    login_button.place(relx=0.3, rely=0.7, anchor="center")
    
    # Register button
    register_button = Button(right_frame, text=" Register ", font=("Helvetica", 12), bg="#3D9962", fg="white", command=register_action)
    register_button.place(relx=0.6, rely=0.7, anchor="center")

    # Make the frames expand to fill the window
=======
    password_label = Label(right_frame, text="Password", font=("Helvetica", 10), bg="#D9D9D9", fg="black")
    password_label.place(relx=0.15, rely=0.40, anchor="center")

    password_entry = Entry(right_frame, font=("Helvetica", 14), bd=5, relief="flat", justify="center", show="•")
    password_entry.place(relx=0.6, rely=0.40, anchor="center", width=200)

    result_label = Label(right_frame, text="", font=("Helvetica", 12), fg="green", bg="#D9D9D9")
    result_label.place(relx=0.5, rely=0.85, anchor="center")

    # Function to switch to the registration view
    def switch_to_registration_view():
        registration_window.deiconify()
        window.withdraw()

    registration_button = Button(right_frame, text=" Register ", font=("Helvetica", 12), bg="#3D9962", fg="white", command=switch_to_registration_view)
    registration_button.place(relx=0.5, rely=0.7, anchor="center")

    login_button = Button(right_frame, text=" Login ", font=("Helvetica", 12), bg="#3D9962", fg="white", command=login_action)
    login_button.place(relx=0.5, rely=0.8, anchor="center")

>>>>>>> f59557e60a1926577ec6be0f68fa1e0d60fc7fda
    window.grid_rowconfigure(0, weight=1)
    window.grid_columnconfigure(0, weight=1)
    window.grid_columnconfigure(1, weight=1)

<<<<<<< HEAD
    window.mainloop()

# Function to handle the login action
def login_action():
    # Add your login logic here
    print("Login button clicked")

# Function to handle the register action
def register_action():
    # Add your register logic here
    print("Register button clicked")

# Create and run the window
create_window()
=======
    # Creating the registration window
    registration_window = Tk()
    registration_window.title("Registration Page")
    registration_window.geometry("600x500")
    registration_window.resizable(0, 0)
    registration_window.withdraw()

    registration_left_frame = Frame(registration_window, width=300, height=500)
    registration_left_frame.grid(row=0, column=0, sticky="nsew")
    set_background_color(registration_left_frame, "#3D9962")

    registration_label_team = Label(registration_left_frame, text="Team Ignition", font=("Helvetica", 20), bg="#3D9962", fg="white")
    registration_label_team.place(relx=0.5, rely=0.5, anchor="center")

    registration_right_frame = Frame(registration_window, width=300, height=500)
    registration_right_frame.grid(row=0, column=1, sticky="nsew")
    set_background_color(registration_right_frame, "#D9D9D9")

    registration_label_signup = Label(registration_right_frame, text="Registration", font=("Helvetica", 20), bg="#D9D9D9", fg="#4C5E8C")
    registration_label_signup.place(relx=0.5, rely=0.1, anchor="center")

    registration_name_label = Label(registration_right_frame, text="Name", font=("Helvetica", 10), bg="#D9D9D9", fg="black")
    registration_name_label.place(relx=0.15, rely=0.25, anchor="center")

    registration_name_entry = Entry(registration_right_frame, font=("Helvetica", 14), bd=4, relief="flat", justify="center")
    registration_name_entry.place(relx=0.6, rely=0.25, anchor="center", width=200)

    registration_email_label = Label(registration_right_frame, text="Email", font=("Helvetica", 10), bg="#D9D9D9", fg="black")
    registration_email_label.place(relx=0.15, rely=0.35, anchor="center")

    registration_email_entry = Entry(registration_right_frame, font=("Helvetica", 14), bd=5, relief="flat", justify="center")
    registration_email_entry.place(relx=0.6, rely=0.35, anchor="center", width=200)

    registration_username_label = Label(registration_right_frame, text="Username", font=("Helvetica", 10), bg="#D9D9D9", fg="black")
    registration_username_label.place(relx=0.15, rely=0.45, anchor="center")

    registration_username_entry = Entry(registration_right_frame, font=("Helvetica", 14), bd=5, relief="flat", justify="center")
    registration_username_entry.place(relx=0.6, rely=0.45, anchor="center", width=200)

    registration_password_label = Label(registration_right_frame, text="Password", font=("Helvetica", 10), bg="#D9D9D9", fg="black")
    registration_password_label.place(relx=0.15, rely=0.55, anchor="center")

    registration_password_entry = Entry(registration_right_frame, font=("Helvetica", 14), bd=5, relief="flat", justify="center", show="•")
    registration_password_entry.place(relx=0.6, rely=0.55, anchor="center", width=200)

    registration_result_label = Label(registration_right_frame, text="", font=("Helvetica", 12), fg="green", bg="#D9D9D9")
    registration_result_label.place(relx=0.5, rely=0.85, anchor="center")

    # Function to switch to the login view
    def switch_to_login_view():
        window.deiconify()
        registration_window.withdraw()

    registration_back_to_login_button = Button(registration_right_frame, text=" Back to Login ", font=("Helvetica", 12), bg="#3D9962", fg="white", command=switch_to_login_view)
    registration_back_to_login_button.place(relx=0.5, rely=0.8, anchor="center")

    # Function to handle registration button click
    def registration_action():
        # Implement your registration logic here
        pass

    registration_register_button = Button(registration_right_frame, text=" Register ", font=("Helvetica", 12), bg="#3D9962", fg="white", command=registration_action)
    registration_register_button.place(relx=0.5, rely=0.7, anchor="center")

    registration_window.grid_rowconfigure(0, weight=1)
    registration_window.grid_columnconfigure(0, weight=1)
    registration_window.grid_columnconfigure(1, weight=1)

    window.mainloop()

# Function for opening a new window after successful login
def create_work_completed_window():
    work_completed_window = Tk()
    work_completed_window.title("Work Completed Page")
    work_completed_window.geometry("400x300")

    label_work_completed = Label(work_completed_window, text="Congratulations! Your work is completed.", font=("Helvetica", 16))
    label_work_completed.pack(pady=50)

    work_completed_window.mainloop()

# Run the login window
create_login_window()
>>>>>>> f59557e60a1926577ec6be0f68fa1e0d60fc7fda
