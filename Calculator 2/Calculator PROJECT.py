import tkinter as tk
import tkinter.font as font

def add():
    Ans.delete(0,50)
    Num11 = float(Num1.get())
    Num12 = float(Num2.get())
    sumvalue = Num11 + Num12
    Num1.delete(0,50)
    Num2.delete(0,50)
    Ans.insert(0, sumvalue)

def difference():
    Ans.delete(0,50)
    Num21 = float(Num1.get())
    Num22 = float(Num2.get())
    differencevalue = Num21 - Num22
    Num1.delete(0,50)
    Num2.delete(0,50)
    Ans.insert(0, differencevalue)

def product():
    Ans.delete(0,50)
    Num31 = float(Num1.get())
    Num32 = float(Num2.get())
    productvalue = Num31 * Num32
    Num1.delete(0,50)
    Num2.delete(0,50)
    Ans.insert(0, productvalue)

def quotient():
    Ans.delete(0,50)
    Num41 = float(Num1.get())
    Num42 = float(Num2.get())
    quotientvalue = Num41 / Num42
    Num1.delete(0,50)
    Num2.delete(0,50)
    Ans.insert(0, quotientvalue)

window = tk.Tk()
window.title('Calculator')
buttonfont = font.Font(size=25)


label = tk.Label(
    text="Calculator by Hamza Naveed",
    fg="white",
    bg="black",
    width=27,
    height=5
    
)
label.pack()



Num1 = tk.Entry(fg="black", bg="white", width=27,)



Num2 = tk.Entry(fg="black", bg="white", width=27,)


Ans = tk.Entry(fg="black", bg="white", width=27,)
Num1.pack()
Num2.pack()
Ans.pack()


Add = tk.Button(
    text=" + ",
    width=5,
    height=1,
    bg="black",
    fg="white",
    command = add
)

Minus = tk.Button(
    text=" - ",
    width=5,
    height=1,
    bg="black",
    fg="white",
    command = difference
)

Times = tk.Button(
    text=" * ",
    width=5,
    height=1,
    bg="black",
    fg="white",
    command = product
)

Divide = tk.Button(
    text=" / ",
    width=5,
    height=1,
    bg="black",
    fg="white",
    command = quotient
)



Add.pack()
Minus.pack()
Times.pack()
Divide.pack()



Add['font'] = buttonfont
Minus['font'] = buttonfont
Times['font'] = buttonfont
Divide['font'] = buttonfont



window.mainloop()
