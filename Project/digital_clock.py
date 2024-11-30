import tkinter
from time import strftime

root = tkinter.Tk()
root.title("Digital Clock")


def time():
    string = strftime("%H:%M:%S %p\n%D")
    label.config(text=string)
    label.after(1000, time)


label = tkinter.Label(
    root, font=("calibri", 50, "bold"), background="white", foreground="black"
)
label.pack(anchor="center")

time()

root.mainloop()
