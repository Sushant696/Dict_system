import sqlite3
from tkinter import *

word_list = [
    {"word": "Serendipity", "description": "the occurrence and development of events by chance in a happy or beneficial way"},
    {"word": "Ephemeral", "description": "lasting for a very short time"},
    {"word": "Ubiquitous", "description": "present, appearing, or found everywhere"},
    {"word": "Quixotic", "description": "exceedingly idealistic; unrealistic and impractical"},
    {"word": "Mellifluous", "description": "having a smooth, flowing sound"},
    {"word": "Sycophant", "description": "a person who acts obsequiously towards someone important in order to gain advantage"},
    {"word": "Nefarious", "description": "wicked, villainous, or criminal"},
    {"word": "Pernicious",
        "description": "having a harmful effect, especially in a gradual or subtle way"},
    {"word": "Ineffable",
        "description": "too great or extreme to be expressed or described in words"},
    {"word": "Esoteric", "description": "intended for or likely to be understood by only a small number of people with special knowledge"},
    {"word": "Halcyon", "description": "denoting a period of time in the past that was idyllically happy and peaceful"},
    {"word": "Sanguine", "description": "optimistic or positive, especially in an apparently difficult or challenging situation"},
    {"word": "Quotidian", "description": "of or occurring every day; daily"},
    {"word": "Cacophony", "description": "a harsh, discordant mixture of sounds"},
    {"word": "Benevolent",
        "description": "well-meaning and kindly; expressing goodwill or kindly feelings"}

]


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


if __name__ == "__main__":
    root = Tk()
    root.geometry('400x400')
    root.title('Dictionary System')
    root.resizable(False, False)

    left_frame = Frame(root, bg='green')
    left_frame.pack(side="left", fill="both", expand=True)

    display_words_ui(left_frame)

    root.mainloop()
