from tkinter import *
import time

root = Tk()
root.title('Digital Clock')
root.geometry("420x150")

label = Label(root, font=("Boulder", 68, 'bold'), bg="#f2e750", fg="#363529", bd=25)
label.grid(row=0, column=1)


def digital_clock():
    time_live = time.strftime("%H:%M:%S")
    label.config(text=time_live)
    label.after(200, digital_clock)


digital_clock()
root.mainloop()
