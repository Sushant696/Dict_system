# import sqlite3
# from tkinter import *
# import json

# words =[]






# def add_word_window():
#     add_root = Tk()
#     add_root.title("Add Word in Dictionary")
#     add_root.geometry("500x500")
#     add_root.resizable(0,0)


    


# # This checks weather the word entered by user is in dictionary list or not
#     def check_user_word(word_by_user):
#         if word_by_user in words:
#             alert_message("Word already exits!")
#         else:
#             get_data()
#             alert_message("Word Added Sucessfully!")
            


# # Function that works when the add button is clicked and checks the boxes wheather they are empty or not
#     def submit():
#         if word.get()=="" and description.get("1.0", END) == "\n":
#             alert_message("Both Word and Description are Empty!")
#         elif word.get()=="":
#             alert_message("     Word is Empty!")
#         elif description.get("1.0", END) == "\n":
#             alert_message("     Description is Empty!")
#         else:
#             check_user_word(word.get().lower())
            
# # Function to get word and description by user
#     def get_data():
#         word_des = {'word':word.get(),"description":description.get(1.0,END).strip()}
#         word.delete(0,END)
#         description.delete("1.0",END)
#         # print(word_des)


#         # Connect to the SQLite database
#         conn = sqlite3.connect('words.db')
#         cursor = conn.cursor()

#         # Create table if not exists
#         cursor.execute('''CREATE TABLE IF NOT EXISTS description (
#                     id INTEGER PRIMARY KEY AUTOINCREMENT,
#                     word TEXT,
#                     description TEXT
#                 )''')
#         conn.commit()

#         # Insert word and description into the database
#         cursor.execute('''INSERT INTO description (word, description) VALUES (?, ?)''',
#                    (word_des['word'], word_des['description']))
#         conn.commit()

#         # Convert data to JSON format
#         word_json = json.dumps(word_des)
#         print(word_json)

#         # Close database connection
#         conn.close()


# # This is just a function that displays alert messages!
#     def alert_message(message):
#         alert.config(text=f"INFO : {message}")

#     # labels
#     word_label = Label(add_root,text="Word",font=16)
#     word_label.place(x=80,y=20)

#     description_label = Label(add_root,text="Description",font=16)
#     description_label.place(x=200,y=120)


#     # Entry Boxes
#     word = Entry(add_root,font=16)
#     word.place(x=160,y=20,height=30)

#     description = Text(add_root)
#     description.place(x=50,y=150,height=200,width=400)


# # This is the button to submit / add word to the dictionary
#     add_button = Button(add_root,text="Add",command=submit)
#     add_button.place(x=210,y=380,height=50,width=100)


# # This is label for alert message output
#     alert =Label(add_root,text="",foreground="red")
#     alert.place(x=150,y=460)


#     add_root.mainloop()






# def retrieve_data(id=None):
#     try:
#         # Connect to the SQLite database
#         conn = sqlite3.connect('words.db')
#         cursor = conn.cursor()

#         if id is not None:
#             # Execute the SQL query to retrieve data for the given id
#             cursor.execute('''SELECT * FROM description WHERE id = ?''', (id,))
#             data = cursor.fetchone()
#             if data:
#                 result = {"id": data[0], "word": data[1], "description": data[2]}
#                 print("Data for ID", id, ":")
#                 print(result)
#             else:
#                 result = None
#         else:
#             # Execute the SQL query to retrieve all data
#             cursor.execute('''SELECT * FROM description''')
#             data = cursor.fetchall()
#             result = [{"id": row[0], "word": row[1], "description": row[2]} for row in data]

#         # Close the database connection
#         conn.close()

#         # Convert the result to JSON format
#         return json.dumps(result)
#     except sqlite3.Error as e:
#         print("SQLite error:", e)
#         return None
    

# word_list = json.loads(retrieve_data())
# # word_list = retrieve_data()
# # loop that appends the "all the words that are comming" to the varible named words.
# for i in word_list:
#     words.append(i["word"].lower())
# print(word_list)




# ###################################################################################################################################
# def display_words_ui(container_frame):
#     for i, word_dict in enumerate(word_list):
#         word_frame = Frame(container_frame)
#         word_frame.grid(row=(i // 2) + 1, column=i %
#                         2, padx=70, pady=20, sticky="w")

#         word_label = Label(word_frame, text=f"{i + 1}. {word_dict['word']}", font=(
#             "Helvetica", 12), justify="left", wraplength=400)
#         word_label.grid(row=0, column=0, sticky="w")

#         word_des_label = Label(word_frame, text=f"{word_dict['description']}", font=(
#             "Helvetica", 14), justify="left", wraplength=400)
#         word_des_label.grid(row=1, column=0, sticky="w")


