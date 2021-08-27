#!/usr/bin/python3

from tkinter import *

root = Tk()
root.title("TheCalculator")

# Make the entry field
e = Entry(root, width=30, borderwidth=4)
e.grid(row=0, column=0, columnspan=4, padx=2, pady=10)

def click(char):
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(char))

def clear():
    e.delete(0, END)

def delete():
    pass

def result():
    result = eval(e.get())
    e.delete(0, END)
    e.insert(0, result)


# Make the buttons
button_clear = Button(root, text="Clear", width=4, height=1, command=clear)
button_left_parenthesis = Button(root, text="(", width=4, height=1, command=lambda: click("("))
button_right_parenthesis = Button(root, text=")", width=4, height=1, command=lambda: click(")"))
button_divide = Button(root, text="%", width=4, height=1, command=lambda: click("/"))

button_7 = Button(root, text="7", width=4, height=1, command=lambda: click(7))
button_8 = Button(root, text="8", width=4, height=1, command=lambda: click(8))
button_9 = Button(root, text="9", width=4, height=1, command=lambda: click(9))
button_multiply = Button(root, text="*", width=4, height=1, command=lambda: click("*"))


button_4 = Button(root, text="4", width=4, height=1, command=lambda: click(4))
button_5 = Button(root, text="5", width=4, height=1, command=lambda: click(5))
button_6 = Button(root, text="6", width=4, height=1, command=lambda: click(6))
button_subtract = Button(root, text="-", width=4, height=1, command=lambda: click("-"))


button_1 = Button(root, text="1", width=4, height=1, command=lambda: click(1))
button_2 = Button(root, text="2", width=4, height=1, command=lambda: click(2))
button_3 = Button(root, text="3", width=4, height=1, command=lambda: click(3))
button_add = Button(root, text="+", width=4, height=1, command=lambda: click("+"))


button_0 = Button(root, text="0", width=4, height=1, command=lambda: click(0))
button_separator = Button(root, text=",", width=4, height=1, command=lambda: click("X"))
button_equal = Button(root, text="=", width=12, height=1, command=result)


# Put the buttons on the screen

button_clear.grid(row=1, column=0)
button_left_parenthesis.grid(row=1, column=1)
button_right_parenthesis.grid(row=1, column=2)
button_divide.grid(row=1, column=3)

button_7.grid(row=2, column=0)
button_8.grid(row=2, column=1)
button_9.grid(row=2, column=2)
button_multiply.grid(row=2, column=3)

button_4.grid(row=3, column=0)
button_5.grid(row=3, column=1)
button_6.grid(row=3, column=2)
button_subtract.grid(row=3, column=3)

button_1.grid(row=4, column=0)
button_2.grid(row=4, column=1)
button_3.grid(row=4, column=2)
button_add.grid(row=4, column=3)

button_0.grid(row=5, column=0)
button_separator.grid(row=5, column=1)
button_equal.grid(row=5, column=2, columnspan=2)


root.mainloop()
