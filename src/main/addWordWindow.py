from tkinter import *

def add_word_window():
    add_root = Tk()
    add_root.geometry("500x500")
    add_root.resizable(0,0)

        #function that works when the add button is clicked and checks the boxes wheather they are empty or not
    def submit():
        if word.get()=="" and description.get("1.0", END) == "\n":
            alert_message("Both Word and Description are Empty!")
        elif word.get()=="":
            alert_message("Word is Empty!")
        elif description.get("1.0", END) == "\n":
            alert_message("Description is Empty!")
        else:
            alert.config(text="")
            word.delete(0,END)
            description.delete("1.0",END)



    #this is just a function that displays alert messages!
    def alert_message(message):
        alert.config(text=f"{message}")

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
    alert =Label(text="",bg="red")
    alert.place(x=200,y=460)


    add_root.mainloop()