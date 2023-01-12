from tkinter import *

def button_click(number):
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(number))

def button_clear():
    e.delete(0, END)

def button_add():
    first_number = e.get()
    global f_num
    f_num = int(first_number)
    e.delete(0, END)
    global math
    math = "Adição"

def button_subtract():
    first_number = e.get()
    global f_num
    f_num = int(first_number)
    e.delete(0, END)
    global math
    math = "Subtração"

def button_multiply():
    first_number = e.get()
    global f_num
    f_num = int(first_number)
    e.delete(0, END)
    global math
    math = "Multiplicação"

def button_divide():
    first_number = e.get()
    global f_num
    f_num = int(first_number)
    e.delete(0, END)
    global math
    math = "Divisão"

def button_equal():
    second_number = e.get()
    e.delete(0, END)
    if math == "Adição":
        e.insert(0, f_num + int(second_number))
    elif math == "Subtração":
        e.insert(0, f_num - int(second_number))
    elif math == "Multiplicação":
        e.insert(0, f_num * int(second_number))
    elif math == "Divisão":
        e.insert(0, f_num / int(second_number))

root = Tk()
root.title("Calculadora")

e = Entry(root, width=35, borderwidth=5)
e.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

button_1 = Button(root, text="1", padx=40, pady=20, command=lambda: button_click(1))
button_2 = Button(root, text="2", padx=40, pady=20, command=lambda: button_click(2))
button_3 = Button(root, text="3", padx=40, pady=20, command=lambda: button_click(3))
button_4 = Button(root, text="4", padx=40, pady=20, command=lambda: button_click(4))
button_5 = Button(root, text="5", padx=40, pady=20, command=lambda: button_click(5))
button_6 = Button(root, text="6", padx=40, pady=20, command=lambda: button_click(6))
button_7 = Button(root, text="7", padx=40, pady=20, command=lambda: button_click(7))
button_8 = Button