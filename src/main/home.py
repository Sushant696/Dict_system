from tkinter import *
from addWordWindow import add_word_window
from words import display_words_ui, word_list

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

root.mainloop()
