#129

from tkinter import *

def onclick():
    input = entry_box.get()
    if input.isdigit():
        number_list.insert(END, input)
        entry_box.delete(0, END)

    else:
        entry_box.delete(0, END)

def clear():
    number_list.delete(0, END)

def save_list():
    file = open("WholeNUmmms.csv", "w")
    tmp_list = number_list.get(0, END)
    item = 0
    for x in tmp_list:
        newRec = tmp_list[item] + "\n"
        file.write(str(newRec))
        item = item + 1
    file.close()


window = Tk()
window.title("Whole Number.")
window.geometry("600x400")

entry_box = Entry(text = "")
entry_box.place(x = 120, y = 80, height = 35, width = 150)

click = Button(text = "Check if whole number. ", command = onclick)
click.place(x = 110, y = 150, height = 35, width = 170)

label = Label(text = "Whole Numbers:")
label.place(x = 440, y = 30, height = 30, width = 100)

number_list = Listbox()
number_list.place(x = 440, y = 70, height = 130, width = 100)

clear_button = Button(text = "Clear", command = clear)
clear_button.place(x = 400, y = 250, height = 25, width = 180)

save_button = Button(text = "Save", command = save_list)
save_button.place(x = 400, y = 300, height = 35, width = 180)




window.mainloop()
