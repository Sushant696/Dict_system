from tkinter import *
import sqlite3
import json


def retrieve_data(id=None):
    try:
        # Connect to the SQLite database
        conn = sqlite3.connect('words.db')
        cursor = conn.cursor()

        if id is not None:
            # Execute the SQL query to retrieve data for the given id
            cursor.execute('''SELECT * FROM description WHERE id = ?''', (id,))
            data = cursor.fetchone()
            if data:
                result = {"id": data[0], "word": data[1],
                          "description": data[2]}
                print("Data for ID", id, ":")
                print(result)
            else:
                result = None
        else:
            # Execute the SQL query to retrieve all data
            cursor.execute('''SELECT * FROM description''')
            data = cursor.fetchall()
            result = [{"id": row[0], "word": row[1].lower(), "description": row[2]}
                      for row in data]

        # Close the database connection
        conn.close()

        # Convert the result to JSON format
        return json.dumps(result) if result is not None else "[]"
    except sqlite3.Error as e:
        print("SQLite error:", e)
        return "[]"


word_list = json.loads(retrieve_data())
print(word_list)


def update_word(word_id, new_word, new_description):
    try:
        # Connect to the SQLite database
        conn = sqlite3.connect('words.db')
        cursor = conn.cursor()

        # Update word and description in the database
        cursor.execute('''UPDATE description SET word=?, description=? WHERE id=?''',
                       (new_word, new_description, word_id))
        conn.commit()

        print(f"Word with ID {word_id} updated successfully.")

        # Close database connection
        conn.close()

    except sqlite3.Error as e:
        print("SQLite error:", e)


root = Tk()
root.geometry('1200x750')
root.title('Dictionary System')
root.resizable(False, False)

# top header container
top_frame = Frame(root, borderwidth=6, bg='green')
top_frame.place(x=20, y=1, width=1160, height=80)

# Main Body Container
body_frame = Frame(root, borderwidth=6)
body_frame.place(x=80, y=80, width=1160, height=660)

words = []


def add_word_window():
    global word, description, alert
    add_root = Tk()
    add_root.title("Add Word in Dictionary")
    add_root.geometry("500x500")
    add_root.resizable(0, 0)

    word_label = Label(add_root, text="Word", font=16)
    word_label.place(x=80, y=20)

    description_label = Label(add_root, text="Description", font=16)
    description_label.place(x=200, y=120)

    # Entry Boxes
    word = Entry(add_root, font=16)
    word.place(x=160, y=20, height=30)

    description = Text(add_root)
    description.place(x=50, y=150, height=200, width=400)

    # This is the button to submit / add word to the dictionary
    add_button = Button(add_root, text="Add",background="#3D9962",fg="white", command=submit)
    add_button.place(x=210, y=380, height=50, width=100)

    # This is label for alert message output
    alert = Label(add_root, text="", foreground="red")
    alert.place(x=150, y=460)

    add_root.mainloop()


# add_root.mainloop()


# here is the update logic each word has unique id so that is being passed here the wordid des and current word and the update button is being displayed from iteration which is done in display_words_ui

def update_word_window(word_id, current_word, current_description):
    update_root = Tk()
    update_root.title(f"Update Word - {current_word}")
    update_root.geometry("400x200")
    update_root.resizable(0, 0)

    def update_word_in_database(new_word, new_description):
        try:
            # Connect to the SQLite database
            conn = sqlite3.connect('words.db')
            cursor = conn.cursor()

            # Update word and description in the database
            cursor.execute('''UPDATE description SET word=?, description=? WHERE id=?''',
                           (new_word, new_description, word_id))
            conn.commit()

            print(f"Word with ID {word_id} updated successfully.")

            # Close database connection
            conn.close()

            # Update the word_list and refresh the UI
            global word_list
            word_list = []  # clearing the list so that the word will not overwrite the previous word
            word_list = json.loads(retrieve_data())

            # Close the update window
            display_words_ui(body_frame)
            display_words()

            update_root.destroy()

        except sqlite3.Error as e:
            print("SQLite error:", e)

    # Entry widgets
    new_word_entry = Entry(update_root)
    new_word_entry.insert(0, current_word)
    new_word_entry.pack(pady=10)

    new_description_entry = Text(update_root, width=40, height=1)
    new_description_entry.insert('1.0', current_description)
    new_description_entry.pack(pady=10)

    # Update button
    update_button = Button(update_root, text="Update", command=lambda: update_word_in_database(
        new_word_entry.get(),
        new_description_entry.get('1.0', END)), bg="#276640", fg="white")
    update_button.pack(pady=10)

    # Center the window on the screen
    update_root.eval('tk::PlaceWindow . center')

    update_root.mainloop()


'''
    Function that handles delete button actions!!
'''


def delete_button():
    del_root = Tk()
    del_root.resizable(False, False)
    del_root.geometry("400x400")

    def delete_action():
        password = password_entry.get().strip().lower()  # getting password
        if (password != "1234"):
            del_root.destroy()
            not_admin_root = Tk()
            not_admin_root.geometry("300x300")
            not_admin_root.resizable(False, False)
            alert = Label(
                not_admin_root, text="Sorry, Unauthorized access denied.", font=30, fg="red")
            alert.place(x=10, y=120)
            not_admin_root.mainloop()
        else:
            del_root.destroy()
            yes_admin = Tk()
            yes_admin.geometry("400x400")
            yes_admin.resizable(False, False)
            word_error_msg = Label(yes_admin, text="", fg="red", font=20)
            word_error_msg.place(x=80, y=330)

            # function that handles delete button
            def delete_word():
                by_user_word_to_delete = word_to_delete_entry.get().strip().lower()
                word_des_inside = json.loads(retrieve_data())

                def check_word_existis_or_not(): 
                    for entry in word_des_inside:
                        if entry["word"] == by_user_word_to_delete:
                            return True
                    return False

                if by_user_word_to_delete == "":
                    word_error_msg.config(
                        text="Word must be entered to proceed.")

                elif not check_word_existis_or_not():
                    word_error_msg.config(
                        text="Word not found. Deletion failed")

                else:
                    word_error_msg.destroy()
                    delete_word_inside.destroy()
                    # print(f"test xxxxxxxxxxxxxx        :{word_des_inside}")

                    def result_(msg):
                        result_msg.config(text=f"ALERT: {msg}")

                    def no_pressed():
                        confirm_label.destroy()
                        yes_button.destroy()
                        no_button.destroy()
                        word_to_delete_label.destroy()
                        word_to_delete_entry.destroy()
                        result_("Word deletion canceled.")
                        result_msg.config(fg="red")

                    def yes_pressed():

                        def get_index_of_dict(word):
                            for index, entry in enumerate(word_des_inside):
                                if entry["word"] == word:
                                    return index
                            return None

                        word_to_delete_dict_index = get_index_of_dict(
                            by_user_word_to_delete)
                        word_des_inside.pop(word_to_delete_dict_index)
                        # after poping now update the data to db and update the ui

                        # update the db with new word_list
                        conn = sqlite3.connect('words.db')
                        cursor = conn.cursor()

                        # clear existing data
                        cursor.execute('''DELETE FROM description''')

                        # inserting the updated word list into the data base
                        for word_entry in word_des_inside:
                            cursor.execute('''INSERT INTO description(word, description) VALUES(?, ?)''', (
                                word_entry['word'], word_entry['description']))

                        conn.commit()
                        conn.close()

                        global word_list
                        word_list = word_des_inside

                        display_words_ui(body_frame)

                        confirm_label.destroy()
                        yes_button.destroy()
                        no_button.destroy()
                        word_to_delete_label.destroy()
                        word_to_delete_entry.destroy()
                        result_("Word Deleted Sucessfully")
                    


                    confirm_label = Label(
                        yes_admin, text="Are you sure?", fg="red", font=20)
                    confirm_label.place(x=160, y=250,)
                    yes_button = Button(
                        yes_admin, text="Yes",background="#3D9962",fg="white", command=yes_pressed)
                    yes_button.place(x=120, y=280, width=80, height=40)
                    no_button = Button(yes_admin, text="No",background="red",fg="white",
                                       command=no_pressed)
                    no_button.place(x=200, y=280, width=80, height=40)
                    result_msg = Label(yes_admin, text="", fg="green")
                    result_msg.place(x=110, y=330)

            # labels, entries and buttons.
            word_to_delete_label = Label(
                yes_admin, text="Enter the word to delete", font=18)
            word_to_delete_label.place(x=120, y=50)
            word_to_delete_entry = Entry(yes_admin, font=18)
            word_to_delete_entry.place(x=100, y=80, width=200, height=30)
            delete_word_inside = Button(
                yes_admin, text="Delete",background="#3D9962",fg="white", command=delete_word)
            delete_word_inside.place(x=150, y=150, height=50, width=100)

            yes_admin.mainloop()

    password_label = Label(del_root, text="Enter Authorization Code", font=18)
    password_label.place(x=110, y=80)
    password_entry = Entry(del_root, font=20)
    password_entry.place(x=110, y=100, width=180, height=30)
    cont_button = Button(del_root, text="Continue =>",
                         font=20,background="#3D9962",fg="white", command=delete_action)
    cont_button.place(x=150, y=180, height=50, width=100)

    del_root.mainloop()


# function to check user word exists or not
def check_user_word(word_by_user):
    load_words = json.loads(retrieve_data())
    words = [d["word"] for d in load_words]
    if word_by_user in words:
        alert_message(" Word already exits!")
        alert.config(fg="red")

    else:
        get_data()
        alert.config(fg="green")
        alert_message(" Word Added Sucessfully!")


# Function that works when the add button is clicked and checks the boxes wheather they are empty or not
def submit():
    global word_list
    word_list = []
    # print(f"check{word_list}")
    display_words_ui(body_frame)
    if word.get() == "" and description.get("1.0", END) == "\n":
        alert_message("Both Word and Description are Empty!")
    elif word.get() == "":
        alert_message("     Word is Empty!")
    elif description.get("1.0", END) == "\n":
        alert_message("     Description is Empty!")
    else:
        check_user_word(word.get().lower())
        word_list = json.loads(retrieve_data())
        # print(f"check two :  {word_list}")
        display_words_ui(body_frame)
        display_words()


# Function to get word and description by user
def get_data():
    word_des = {
        'word': word.get(), "description": description.get(1.0, END).strip()}
    word.delete(0, END)
    description.delete("1.0", END)
    # print(word_des)

    # Connect to the SQLite database
    conn = sqlite3.connect('words.db')
    cursor = conn.cursor()

    # Create table if not exists
    cursor.execute('''CREATE TABLE IF NOT EXISTS description (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    word TEXT,
                    description TEXT
                )''')
    conn.commit()

    # Insert word and description into the database
    cursor.execute('''INSERT INTO description (word, description) VALUES (?, ?)''',
                   (word_des['word'], word_des['description']))
    conn.commit()

    # Convert data to JSON format
    word_json = json.dumps(word_des)
    print(word_json)
    # Close database connection
    conn.close()

# This is just a function that displays alert messages!


def alert_message(message):
    alert.config(text=f"ALERT! {message}")


# loop that appends the "all the words that are comming" to the varible named words.
for i in word_list:
    words.append(i["word"].lower())


# top header container
top_frame = Frame(root, borderwidth=6, bg='green')
top_frame.place(x=20, y=1, width=1160, height=80)

# Main Body Container
body_frame = Frame(root, borderwidth=6)
body_frame.place(x=10, y=100, width=1160, height=660)

words = []

# Iterate over Word list and render the word


def display_words_ui(container_frame):
    # Get the list of existing widgets
    widgets = container_frame.winfo_children()

    # Skip the first two widgets (assuming they are the Add New Word and Delete Word buttons)
    existing_widgets = widgets[2:]

    # Destroy existing word frames
    for widget in existing_widgets:
        widget.destroy()
    # above here destroyed the exising widget except the add word and delete word button

    for i, word_dict in enumerate(word_list):
        word_frame = Frame(container_frame, relief="solid")
        word_frame.grid(row=(i // 3), column=i %
                        3, padx=45, pady=55, sticky="w")

        word_label = Label(word_frame, text=f"{word_dict['word']}", font=(
            "Helvetica", 14), justify="left", wraplength=300)
        word_label.grid(row=0, column=0, sticky="w")

        word_des_label = Label(word_frame, text=f"{word_dict['description']}", font=(
            "Helvetica", 10), justify="left", wraplength=300)
        word_des_label.grid(row=1, column=0, sticky="w")

        update_button = Button(word_frame, text="Update", command=lambda id=word_dict['id'], word=word_dict[
                               'word'], description=word_dict['description']: update_word_window(id, word, description))
        # Set sticky to "w" (west/left)
        update_button.grid(row=2, column=0, pady=5, sticky="w")


def display_words():
    display_words_ui(body_frame)


def main():
    add_word_button = Button(
        body_frame, text='Add New Word',background="#3D9962",fg="white", command=add_word_window)
    add_word_button.grid(row=0, column=0, padx=20, pady=5, sticky="e")

    delete_word_button = Button(
        body_frame, text='Delete word',background="#3D9962",fg="white", command=delete_button)
    delete_word_button.grid(row=0, column=1, padx=20, pady=5, sticky="e")

    # Place the Add and Delete buttons at the top right
    add_word_button.place(x=960, y=1)
    delete_word_button.place(x=1080, y=1)

    display_words()


def search_bar():
    # search bar section
    global search_entry
    search_entry = Entry(top_frame,font=18)
    search_entry.place(x=460, y=5, width=620, height=40)

    logo_label = Label(top_frame, text='Dictionary App')
    logo_label.place(x=20, y=5, width=80, height=50)

    search_button = Button(top_frame, text='Search', command=search_word)
    search_button.place(x=1050, y=5, width=80, height=41)


def search_word():
    user_search_input = search_entry.get().lower()

    if not user_search_input:
        # If the search input is empty, simply return without opening a window
        return

    search_root = Tk()
    search_root.resizable(False, False)
    search_root.geometry("500x500")

    # First filter the word list
    def filter_items(word_dict):
        return user_search_input in word_dict['word'].lower()

    filteredWordList = list(filter(filter_items, word_list))

    if filteredWordList:
        display_filtered_words(search_root, filteredWordList)
    else:
        no_result_label = Label(search_root, text="No matching words found.")
        no_result_label.pack()

    search_root.mainloop()



def display_filtered_words(search_root, filteredWordList):
    for i, word_dict in enumerate(filteredWordList):
        word_frame = Frame(search_root, relief="solid")
        word_frame.grid(row=i, column=0, padx=20, pady=40, sticky="w")

        word_label = Label(word_frame, text=f"{word_dict['word']}", font=(
            "Helvetica", 14), justify="left", wraplength=320)
        word_label.grid(row=0, column=0, sticky="w")

        word_des_label = Label(word_frame, text=f"{word_dict['description']}", font=(
            "Helvetica", 10), justify="left", wraplength=320)
        word_des_label.grid(row=1, column=0, sticky="w")

        update_button = Button(word_frame, text="Update", command=lambda id=word_dict['id'], word=word_dict[
            'word'], description=word_dict['description']: update_word_window(id, word, description))

        # Set sticky to "w" (west/left)
        update_button.grid(row=2, column=0, pady=5, sticky="w")


# search function
search_bar()
main()
root.mainloop()
