
from tkinter import *
from math import *


root = Tk()
root.title("Standard Calculator")
root.configure(bg = 'Pink')
root.geometry('320x310')

values = Entry(root, text = '0', width = 30, borderwidth = 5)
values.grid(row = 0, column = 0, columnspan = 4, padx = 33, pady = 10)


def enter(number):
    existing = values.get()
    values.delete(0, END)
    values.insert(0, str(existing) + str(number))

def clear():
    values.delete(0, END)

def addition() :
    global num1
    global operation
    operation = 'Addition'
    num1 = values.get()
    values.delete(0, END)

def substract():
    global num1
    global operation
    operation = 'Substraction'
    num1 = values.get()
    values.delete(0, END)

def multipy() :
    global num1
    global operation
    operation = 'Multiplication'
    num1 = values.get()
    values.delete(0, END)

def divide() :
    global num1
    global operation
    operation = 'Division'
    num1 = values.get()
    values.delete(0, END)

def squaring():
    global num1
    num1 = values.get()
    values.delete(0, END)
    values.insert(0, int(num1) * int(num1))

def sqroot():
    global num1
    num1 = values.get()
    values.delete(0, END)
    values.insert(0, sqrt(int(num1)) )

def pie():
    values.delete(0, END)
    values.insert(0, pi)

def sine():
    global num1
    num1 = values.get()
    values.delete(0, END)
    radian_convert = radians(int(num1))
    values.insert(0, sin(radian_convert))

def cosine():
    global num1
    num1 = values.get()
    values.delete(0, END)
    radian_convert = radians(int(num1))
    values.insert(0, cos(radian_convert) )

def tangent():
    global num1
    num1 = values.get()
    values.delete(0, END)
    radian_convert = radians(int(num1))
    values.insert(0, tan(radian_convert))

def fact():
    global num1
    num1 = values.get()
    values.delete(0, END)
    values.insert(0, factorial(int(num1)))

def equals():
    num2 = values.get()
    values.delete(0, END)

    if operation == 'Addition' :
        values.insert(0, float(num1) + float(num2))
    elif operation ==  'Substraction' :
        values.insert(0, float(num1)- float(num2))
    elif operation == 'Multiplication':
        values.insert(0, float(num1) * float(num2))
    elif operation == 'Division':
        values.insert(0, float(num1) / float(num2))



button_0 = Button(root, text='0', padx = 33, pady = 10, bg = 'Cyan', command = lambda : enter(0))
button_1 = Button(root, text='1', padx = 33, pady = 10, bg = 'Cyan', command = lambda : enter(1))
button_2 = Button(root, text='2', padx = 33, pady = 10, bg = 'Cyan', command = lambda : enter(2))
button_3 = Button(root, text='3', padx = 33, pady = 10, bg = 'Cyan', command = lambda : enter(3))
button_4 = Button(root, text='4', padx = 33, pady = 10, bg = 'Cyan', command = lambda : enter(4))
button_5 = Button(root, text='5', padx = 33, pady = 10, bg = 'Cyan', command = lambda : enter(5))
button_6 = Button(root, text='6', padx = 33, pady = 10, bg = 'Cyan', command = lambda : enter(6))
button_7 = Button(root, text='7', padx = 33, pady = 10, bg = 'Cyan', command = lambda : enter(7))
button_8 = Button(root, text='8', padx = 33, pady = 10, bg = 'Cyan', command = lambda : enter(8))
button_9 = Button(root, text='9', padx = 33, pady = 10, bg = 'Cyan', command = lambda : enter(9))

button_0.grid(row = 5, column = 1)

button_1.grid(row = 4, column =0 )
button_2.grid(row = 4, column = 1)
button_3.grid(row = 4, column = 2)

button_4.grid(row = 3 , column = 0 )
button_5.grid(row = 3, column =  1)
button_6.grid(row = 3, column =  2)

button_7.grid(row = 2, column = 0)
button_8.grid(row = 2, column = 1)
button_9.grid(row = 2, column = 2)

# button_clear = Button(root, text = 'C',padx= 31, pady= 10)
# button_clear.grid(row = 1, column = 0)

button_backspace = Button(root, text = 'AC', padx = 69, pady = 10, command = clear)
button_backspace.grid(row = 1, column = 0, columnspan = 2)

button_equals = Button(root, text = '=', padx= 31, pady = 10, command = equals)
button_equals.grid(row = 1, column = 2)

button_add = Button(root, text= '+', padx = 28, pady = 10, bg = 'light Green', command = addition)
button_add.grid(row = 1, column = 3)

button_sub = Button(root, text= '-', padx = 28, pady = 10, bg = 'light Green',command = substract)
button_sub.grid(row = 2, column = 3)

button_mul = Button(root, text= 'X', padx = 28, pady = 10, bg = 'light Green',command = multipy)
button_mul.grid(row = 3, column = 3)

button_div = Button(root, text= '/', padx = 28, pady = 10, bg = 'light Green',command = divide)
button_div.grid(row = 4, column = 3)

button_square = Button(root, text = 'Square', padx = 19, pady = 10, bg = 'Light Green', command = squaring)
button_square.grid(row = 5, column = 2)

button_squareroot = Button(root, text = 'Squareroot', padx = 7, pady = 10, bg = 'Light Green', command = sqroot)
button_squareroot.grid(row = 5, column = 0)

button_sin = Button(root, text = 'sin', padx = 28, pady = 10, bg = 'Light Green', command = sine)
button_sin.grid(row = 6, column = 0)

button_cos = Button(root, text = 'cos', padx = 28, pady = 10, bg = 'Light Green', command = cosine)
button_cos.grid(row = 6, column = 1)

button_tan = Button(root, text = 'tan', padx = 28, pady = 10, bg = 'Light Green', command = tangent)
button_tan.grid(row = 6, column = 2)

button_fact = Button(root, text = 'n!', padx = 26, pady = 10, bg = 'Light Green', command = fact)
button_fact.grid(row = 6, column = 3)

button_pie = Button(root, text = 'pie', padx = 23, pady = 10, bg = 'Light Green', command = pie)
button_pie.grid(row = 5, column = 3)




root.mainloop()



















































