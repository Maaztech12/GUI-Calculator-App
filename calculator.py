#step 1 : importing
from tkinter import *

#step 2 : creating window
window = Tk()
window.title("calculator app")
img= PhotoImage(file='C:\\Users\\User\\Desktop\\cal1.png')
window.iconphoto(False,img)
window.geometry('384x348')
window.config(bg = 'beige')
def click(num):
    result = entry.get()
    entry.delete(0,END)
    entry.insert(0, str(result) + str(num))
entry = Entry(window, width=62 , borderwidth=5)
button9 = Button(window , text='9',padx=40 , pady=20, command=lambda: click(9),bg='black',fg='white')
button8 = Button(window , text='8',padx=40 , pady=20, command=lambda: click(8),bg='black',fg='white')
button7 = Button(window , text='7',padx=40 , pady=20, command=lambda: click(7),bg='black',fg='white')
button6 = Button(window , text='6',padx=40 , pady=20, command=lambda: click(6),bg='black',fg='white')
button5 = Button(window , text='5',padx=40 , pady=20, command=lambda: click(5),bg='black',fg='white')
button4 = Button(window , text='4',padx=40 , pady=20, command=lambda: click(4),bg='black',fg='white')
button3 = Button(window , text='3',padx=40 , pady=20, command=lambda: click(3),bg='black',fg='white')
button2 = Button(window , text='2',padx=40 , pady=20, command=lambda: click(2),bg='black',fg='white')
button1 = Button(window , text='1',padx=40 , pady=20, command=lambda: click(1),bg='black',fg='white')
button0 = Button(window , text='0',padx=40 , pady=20, command=lambda: click(0),bg='black',fg='white')
#addtion:
def add():
    n1=entry.get()
    global math
    math = "addition"
    global i
    i = int(n1)
    entry.delete(0,END)
button_add = Button(window , text='+',padx=39 , pady=20, command=add,bg='wheat1',fg='black')
#equal:
def equal():
    n2=entry.get()
    entry.delete(0,END)
    if math == "addition":
        entry.insert(0,i + int(n2))
    elif math == "subraction":
        entry.insert(0, i - int(n2))
    elif math == "multiplication":
        entry.insert(0, i * int(n2))
    elif math == "division":
        entry.insert(0, i / int(n2))
button_equal = Button(window , text='=',padx=86.5 , pady=20,command=equal,bg='violet',fg='black')
#CLear:
def clear():
    entry.delete(0, END)
button_clear = Button(window , text='Clear',padx=173 , pady=20,command=clear,bg='whitesmoke',fg='black')
#subraction:
def minus():
    n1=entry.get()
    global math
    math = "subraction"
    global i
    i = int(n1)
    entry.delete(0,END)
button_sub = Button(window , text='-',padx=40 , pady=20,command=minus,bg='wheat1',fg='black')
#multiplication:
def multi():
    n1=entry.get()
    global math
    math = "multiplication"
    global i
    i = int(n1)
    entry.delete(0,END)
button_mul = Button(window , text='*',padx=40 , pady=20,command=multi,bg='wheat1',fg='black')
#division:
def div():
    n1=entry.get()
    global math 
    math ="division"
    global i
    i = int(n1)
    entry.delete(0,END)
button_div = Button(window , text='/',padx=40 , pady=20,command=div,bg='wheat1',fg='black')

button9.grid(row=1 ,column=0)
button8.grid(row=1 ,column=1)
button7.grid(row=1 ,column=2)
button6.grid(row=2 ,column=0)
button5.grid(row=2 ,column=1)
button4.grid(row=2 ,column=2)
button3.grid(row=3 ,column=0)
button2.grid(row=3 ,column=1)
button1.grid(row=3 ,column=2)
button0.grid(row=4 ,column=0)
button_add.grid(row=1 ,column=3)
button_clear.grid(row=5 ,column=0,columnspan=4)
button_equal.grid(row=4 ,column=1,columnspan=2)
button_sub.grid(row=2 ,column=3)
button_mul.grid(row=3 ,column=3)
button_div.grid(row=4 ,column=3)
entry.grid(row=0 , column=0,columnspan=4)
mainloop()