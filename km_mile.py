from tkinter import *

#128:

def mile():
    mile_conv = input_box.get()
    input_box.delete(0, END)
    float_mile = float(mile_conv)
    converted_mile = (float_mile / 0.6214)
    answer["text"] = str(converted_mile) + " miles."
    input_box.focus()

def kilo():
    kilo_conv = input_box.get()
    input_box.delete(0, END)
    float_kilo = float(kilo_conv)
    converted_kilo = (float_kilo * 1.6093)
    answer["text"] = str(converted_kilo) + " kilometers."
    input_box.focus()


window = Tk()
window.title("Conversion.")
window.geometry("600x300")

kilo_button = Button(text = "Convert to km. ", command = kilo)
kilo_button.place(x = 350, y = 15, height = 35, width = 175)

mile_button = Button(text = "Convert to miles. ", command = mile)
mile_button.place(x = 350, y = 70, height = 35, width = 175)

input_box = Entry(text ="")
input_box.place(x = 160, y = 30, height = 55, width = 175)
input_box["justify"] = "center"
input_box.focus()

answer = Message(text = "")
answer.place(x = 200, y = 175, height = 55, width = 225)
answer["bg"] = "blue"
answer["fg"] = "white"
window.mainloop()