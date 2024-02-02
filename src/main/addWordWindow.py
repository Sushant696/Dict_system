from tkinter import *

def add_word_window():
    add_root = Tk()
    add_root.geometry("500x500")
    add_root.resizable(0,0)

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
    add_button = Button(add_root,text="Add")
    add_button.place(x=210,y=400,height=50,width=100)


    add_root.mainloop()





