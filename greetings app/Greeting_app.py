import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk


def greet():
    print(f"As-salamu alaykum {user_name.get()}")


root = tk.Tk()

root.geometry("600x400")
root.resizable(False,False)

image = Image.open("grl.jpg").resize((600,400))
photo = ImageTk.PhotoImage(image)
label1 = ttk.Label(root, image = photo)
label1.place(x = 0,y = 0)
root.title("Widget Examples")

user_name = tk.StringVar()
root.title("Greeter")

root.columnconfigure(0, weight=1)
input_fr = ttk.Frame(root, padding=(20, 10, 20, 0))
input_fr.grid(sticky="EW")

name_label = ttk.Label(input_fr, text='Name: ')
name_label.grid(row=0, column=0)
name_entry = ttk.Entry(input_fr, width=35, textvariable=user_name)
name_entry.grid(row=0, column=1)
name_entry.focus()

button_fr = ttk.Frame(root, padding=(20, 10))
button_fr.grid(sticky="EW")
button_fr.columnconfigure(0, weight=1)
button_fr.columnconfigure(1, weight=1)
greet_button = ttk.Button(button_fr, text='Greet', command=greet)
greet_button.grid(row=0, column=0, sticky="EW")

quit_button = ttk.Button(button_fr, text='Quit', command=root.destroy)
quit_button.grid(row=0, column=1, sticky="EW")

root.mainloop()
root.mainloop()