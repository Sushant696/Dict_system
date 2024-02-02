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
    {"word": "Esoteric", "description": "intended for or likely to be understood by only a small number of people with special knowledge"}
]

# words.py


# container frame == bodyFrame the main place to render the UI
def display_words_ui(container_frame):

    # counter = 0
    for i, word_dict in enumerate(word_list):

        word_frame = Frame(container_frame, bg='blue')
        word_frame.grid(row=i,column=0,padx=4,pady=4)

        word_label = Label(
            word_frame, text=f"{i+1}. {word_dict['word']}", font=("Helvetica", 12), justify="left")
        word_label.pack(pady=5 , padx=4)

        word_des_label = Label(
            word_frame, text=f"{i+1}. {word_dict['description']}", font=("Helvetica", 14), justify="left")

        # word_des_label.grid(column=1+i, row=8+i)
        word_des_label.pack(pady=5 , padx=4)

        # print(i, word_dict)
