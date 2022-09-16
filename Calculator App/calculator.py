import tkinter as tk
from PIL import Image, ImageTk
from tkinter import ttk


root = tk.Tk()
root.title("CASIO Calculator")
root.geometry("370x480")
root.resizable(False,False)
image = Image.open("background2.jpg").resize((600,400))
photo = ImageTk.PhotoImage(image)
label = ttk.Label(root, image = photo, padding =5)
label.pack()


def InputNumer(x):
    if entry_box.get() == "O":
        entry_box.delete(0,'end')
        entry_box.insert(0,str(x))
    else:
        length = len(entry_box.get())
        entry_box.insert(length,str(x))


def InputOperator(x):
    if entry_box.get() != "O":
        length = len(entry_box.get())
        entry_box.insert(length,btn_operator[x]['text'])

def FuncClear():
    entry_box.delete(0,tk.END)
    entry_box.insert(0,"O")
result = 0
result_list = []


def FuncOperator():
    content = entry_box.get()
    result = eval(content)
    print(result)
    entry_box.delete(0,tk.END)
    entry_box.insert(0,str(result))

    result_list.append(content)
    result_list.reverse()
    statusBar.configure(text='History :'+'|'.join(result_list[:5]),font='verdana 10 bold')

def FuncDelete():
    length=len(entry_box.get())
    entry_box.delete(length-1,'end')
    if length == 1:
        entry_box.insert(0,"O")

#   Entry Box
entry_box = tk.Entry(font='verdana 14 bold',width=22,bd=10,justify=tk.RIGHT,bg='#e6e6fa')
entry_box.insert(0,"O")
entry_box.place(x=20,y=10)

#   Number Buttons
btn_numbers=[]
for i in range(10):
    btn_numbers.append(tk.Button(width=4,text=str(i),font='times 15 bold',bd=5,
                              command= lambda x=i:InputNumer(x)))

btn_text=1
for i in range(0,3):
    for j in range(0,3):
        btn_numbers[btn_text].place(x=25+j*90, y=70+i*70)
        btn_text +=1

#   Operator Buttons
btn_operator=[]
for i in range(4):
    btn_operator.append(tk.Button(width=4,font='times 15 bold',bd=5,command=lambda x=i:InputOperator(x)))

btn_operator[0]['text'] = "+"
btn_operator[1]['text'] = "-"
btn_operator[2]['text'] = "*"
btn_operator[3]['text'] = "/"

for i in range(4):
    btn_operator[i].place(x=290,y=70+i*70)

#   other buttons
btn_zero = tk.Button(width=19, text='0', font='times 15 bold',bd=5, command= lambda  x=0:InputNumer(x))
btn_clear= tk.Button(width=4, text='C', font='times 15 bold',bd=5, command=FuncClear)
btn_clear.place(x=25,y=340)
btn_zero.place(x=25, y=280)
btn_dot= tk.Button(width=4,text='.',font='times 15 bold',bd=5,command=lambda x=".":InputNumer(x))
btn_dot.place(x=110,y=340)
btn_equal = tk.Button(width=4, text='=', font='times 15 bold',bd=5, command=FuncOperator)
btn_equal.place(x=200,y=340)

icon= tk.PhotoImage(file='back.png')
btn_delete = tk.Button(width=50,height=35, font='times 15 bold',bd=5, command=FuncDelete,image=icon)
btn_delete.place(x=290,y=340)

statusBar = tk.Label(root,text='History : ',relief= tk.SUNKEN,height=3,anchor= tk.W,font='verdana 9 bold')
statusBar.pack(side=tk.BOTTOM,fill=tk.X)

root.mainloop()