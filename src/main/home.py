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
            result = [{"id": row[0], "word": row[1], "description": row[2]}
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
body_frame.place(x=20, y=80, width=1160, height=660)

# @@@@@

words = []


def add_word_window():
    # declare word, description, and alert as global variables
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
    add_button = Button(add_root, text="Add", command=submit)
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
            word_list = [] # clearing the list so that the word will not overwride the previous word
            word_list = json.loads(retrieve_data())
            display_words_ui(body_frame)

            # Close the update window
            display_words_ui(body_frame)
            display_words()

            update_root.destroy()

        except sqlite3.Error as e:
            print("SQLite error:", e)

    # Entry widgets
    new_word_entry = Entry(update_root)
    new_word_entry.grid(row=0, column=1, pady=10)
    new_word_entry.insert(0, current_word)

    new_description_entry = Entry(update_root)
    new_description_entry.grid(row=1, column=1, pady=10)
    new_description_entry.insert(0, current_description)

    # Update button
    update_button = Button(update_root, text="Update", command=lambda: update_word_in_database(
        new_word_entry.get(), new_description_entry.get()))
    update_button.grid(row=2, column=0, columnspan=2, pady=10)


def check_user_word(word_by_user):
    load_words=json.loads(retrieve_data())
    words=[d["word"] for d in load_words ]
    if word_by_user in words:
        alert_message("Word already exits!")
    else:
        get_data()
        alert_message("Word Added Sucessfully!")


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
    alert.config(text=f"INFO : {message}")


# loop that appends the "all the words that are comming" to the varible named words.
for i in word_list:
    words.append(i["word"].lower())


###################################################################################################################################
def display_words_ui(container_frame):
    for i, word_dict in enumerate(word_list):
        word_frame = Frame(container_frame)
        word_frame.grid(row=(i // 2) + 1, column=i %
                        2, padx=70, pady=20, sticky="w")

        word_label = Label(word_frame, text=f"{i + 1}. {word_dict['word']}", font=(
            "Helvetica", 12), justify="left", wraplength=400)
        word_label.grid(row=0, column=0, sticky="w")

        word_des_label = Label(word_frame, text=f"{word_dict['description']}", font=(
            "Helvetica", 14), justify="left", wraplength=400)
        word_des_label.grid(row=1, column=0, sticky="w")

        update_button = Button(word_frame, text="Update", command=lambda id=word_dict['id'], word=word_dict[
                               'word'], description=word_dict['description']: update_word_window(id, word, description))
        update_button.grid(row=2, column=0, pady=5)


# @@@@@


def search_word():
    pass
    # word_label = Label(root, text='text')
    # word_label.place(x=20, y=50, width=80, height=50)


def search_bar():

    # search bar section
    search_entry = Entry(top_frame)
    search_entry.place(x=460, y=5, width=620, height=40)

    logo_label = Label(top_frame, text='Dictionary App')
    logo_label.place(x=20, y=5, width=80, height=50)

    search_button = Button(top_frame, text='Search', command=search_word)
    search_button.place(x=1050, y=5, width=80, height=41)


def display_words():
    display_words_ui(body_frame)


def main():
    add_word_button = Button(
        body_frame, text='Add New Word', command=add_word_window)
    add_word_button.grid(row=0, column=0, padx=10, pady=10, sticky="e")


# search function
search_bar()
main()
display_words()

# @@@@@@@@@@@@@@@@@@@@@@@@@@


root.mainloop()
