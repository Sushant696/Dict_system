from tkinter import *
from words import word_list

words =[]

# loop that appends the "all the words that are comming" to the varible named words.
for i in word_list:
    words.append(i["word"].lower())


def add_word_window():
    add_root = Tk()
    add_root.title("Add Word in Dictionary")
    add_root.geometry("500x500")
    add_root.resizable(0,0)


    


# This checks weather the word entered by user is in dictionary list or not
    def check_user_word(word_by_user):
        if word_by_user in words:
            alert_message("Word already exits!")
        else:
            get_data()
            alert_message("Word Added Sucessfully!")
            word.delete(0,END)
            description.delete("1.0",END)


# Function that works when the add button is clicked and checks the boxes wheather they are empty or not
    def submit():
        if word.get()=="" and description.get("1.0", END) == "\n":
            alert_message("Both Word and Description are Empty!")
        elif word.get()=="":
            alert_message("     Word is Empty!")
        elif description.get("1.0", END) == "\n":
            alert_message("     Description is Empty!")
        else:
            check_user_word(word.get().lower())
            
# Function to get word and description by user
    def get_data():
        new_word = word.get()
        new_des = description.get(1.0,END)
        print(new_word)
        print(new_des)

# This is just a function that displays alert messages!
    def alert_message(message):
        alert.config(text=f"INFO : {message}")

    # labels
    word_label = Label(add_root,text="Word",font=16)
    word_label.place(x=80,y=20)

    description_label = Label(add_root,text="Description",font=16)
    description_label.place(x=200,y=120)


    # Entry Boxes
    word = Entry(add_root,font=16)
    word.place(x=160,y=20,height=30)

    description = Text(add_root)
    description.place(x=50,y=150,height=200,width=400)


# This is the button to submit / add word to the dictionary
    add_button = Button(add_root,text="Add",command=submit)
    add_button.place(x=210,y=380,height=50,width=100)


# This is label for alert message output
    alert =Label(add_root,text="",foreground="red")
    alert.place(x=150,y=460)


    add_root.mainloop()

# add_word_window()