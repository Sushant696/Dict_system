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
    username_label = Label(right_frame, text="Username", font=("Helvetica", 10), bg="#D9D9D9", fg="black")
    username_label.place(relx=0.15, rely=0.30, anchor="center")

    username_entry = Entry(right_frame, font=("Helvetica", 14), bd=4, relief="flat", justify="center")
    username_entry.place(relx=0.6, rely=0.30, anchor="center", width=200)

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
    window.grid_rowconfigure(0, weight=1)
    window.grid_columnconfigure(0, weight=1)
    window.grid_columnconfigure(1, weight=1)

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
