from tkinter import Tk, Label, PhotoImage

# Create the main window
root = Tk()
root.title("Image Example")

# Replace 'path/to/your/image.gif' with the actual path to your image file
# image_path = 'logo.png'
image_path = r'S:\Python\Collage Project\Tkinter_dict\src\main\'


# Create a PhotoImage object
img = PhotoImage(file=image_path)

# Create a label and set the image
label = Label(root, image=img)
label.pack()

# Start the Tkinter event loop
root.mainloop()
