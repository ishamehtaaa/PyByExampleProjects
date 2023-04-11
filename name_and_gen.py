from tkinter import *
import csv

#131:

def add_info():
    name = name_box.get()
    age = age_box.get()
    file = open("Person.csv", "a")
    newRec = name + "," + str(age) + "," + "\n"
    file.write(str(newRec))
    file.close()
    name_box.delete(0, END)
    age_box.delete(0, END)
    name_box.focus()
    enterfollow.destroy()
    success = Label(text = "Info successfully added!", font = ("Arial, 18"))
    success.place(x = 135, y = 50, height = 35, width = 450)
    success["fg"] = "#f28b8b"
    success["bg"] = "#f2d8d8"


def create_csv():
    #enterfollow = Label(text = "Please enter the following: ", font = ("Arial, 15"))
    enterfollow.place(x = 145, y = 50, height = 35, width = 450)
    enterfollow["bg"] = "#f2d8d8"
    pressent = Label(text = "Press Enter when you're done. ", font = ("Arial, 10"))
    pressent.place(x = 215, y = 290, height = 35, width = 300)
    pressent["bg"] = "#f2d8d8"
    enter_butt = Button(text = "Enter", command = add_info, font = ("Arial, 12"))
    enter_butt.place(x = 270, y = 330, height = 45, width = 180)
    enter_butt["bg"] = "#f2b4b4"

    
    name_box.place(x = 360, y = 120, height = 35, width = 170)
    name_label = Label(text = "Name:", font = ("Arial, 11"))
    name_label.place(x = 170, y = 120, height = 35, width = 130)
   
    age_box.place(x = 360, y = 220, height = 35, width = 170)
    age_label = Label(text = "Age:", font = ("Arial, 11"))
    age_label.place(x = 170, y = 220, height = 35, width = 130)

    create_yes.destroy()
    yes_butt.destroy()

window = Tk()
window.title("Person")
window.geometry("700x400")
window["bg"] = "#f2d8d8"


create_yes = Label(text = "Would you like to create a csv?", font = ("Arial", 18))
create_yes.place(x = 125, y = 50, height = 35, width = 450)
create_yes["bg"] = "#f2d8d8"


yes_butt = Button(text = "Yes", command = create_csv, font = ("Arial, 16"))
yes_butt.place(x = 250, y = 160, height = 100, width = 200)
yes_butt["bg"] = "#f28b8b"


name_box = Entry(text = "")
age_box = Entry(text = "")

enterfollow = Label(text = "Please enter the following: ", font = ("Arial, 15"))

window.mainloop()