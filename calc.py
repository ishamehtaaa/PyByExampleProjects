# Import the necessary libraries
from tkinter import *

# Create the calculator window
calculator = Tk()
calculator.title("Simple Calculator")

# Create the input field
input_field = Entry(calculator, width=35, borderwidth=5)
input_field.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

# Define the button click functions
def button_click(number):
    current = input_field.get()
    input_field.delete(0, END)
    input_field.insert(0, str(current) + str(number))

def button_clear():
    input_field.delete(0, END)

def button_add():
    first_number = input_field.get()
    global f_num
    global math_operation
    math_operation = "addition"
    f_num = int(first_number)
    input_field.delete(0, END)

def button_subtract():
    first_number = input_field.get()
    global f_num
    global math_operation
    math_operation = "subtraction"
    f_num = int(first_number)
    input_field.delete(0, END)

def button_multiply():
    first_number = input_field.get()
    global f_num
    global math_operation
    math_operation = "multiplication"
    f_num = int(first_number)
    input_field.delete(0, END)

def button_divide():
    first_number = input_field.get()
    global f_num
    global math_operation
    math_operation = "division"
    f_num = int(first_number)
    input_field.delete(0, END)

def button_equal():
    second_number = input_field.get()
    input_field.delete(0, END)
    if math_operation == "addition":
        input_field.insert(0, f_num + int(second_number))
    elif math_operation == "subtraction":
        input_field.insert(0, f_num - int(second_number))
    elif math_operation == "multiplication":
        input_field.insert(0, f_num * int(second_number))
    elif math_operation == "division":
        input_field.insert(0, f_num / int(second_number))

# Define the calculator buttons
button_1 = Button(calculator, text="1", padx=40, pady=20, command=lambda: button_click(1))
button_2 = Button(calculator, text="2", padx=40, pady=20, command=lambda: button_click(2))
button_3 = Button(calculator, text="3", padx=40, pady=20, command=lambda: button_click(3))
button_4 = Button(calculator, text="4", padx=40, pady=20, command=lambda: button_click(4))
button_5 = Button(calculator, text="5", padx=40, pady=20, command=lambda: button_click(5))
button_6 = Button(calculator, text="6", padx=40, pady=20, command=lambda: button_click(6))
button_7 = Button(calculator, text="7", padx=40, pady=20, command=lambda: button_click(7))
button_8 = Button(calculator, text="8", padx=40, pady=20, command=lambda: button_click(8))
button_9 = Button(calculator, text="9", padx=40, pady=20, command=lambda: button_click(9))
button_0 = Button(calculator, text="0", padx=40, pady=20, command=lambda: button_click(0))
button_add
