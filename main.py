from tkinter import *

window = Tk()
window.title("Feet to Meters")

def calcular(*args):
    try:
        value = float(feet.get())
        met = int(0.3048 * value * 10000 + 0.5) / 10000
        meters.set(met)
    except ValueError:
        meters.set("ERROR")


frame = Frame(window, padx=3, pady=12)
frame.grid(column=0, row=0)

feet = StringVar()
feet_input = Entry(frame, width=7, textvariable=feet)
feet_input.grid(column=1, row=0)

meters = StringVar()
meters.set("0")
Label(frame, textvariable=meters).grid(column=1, row=1)

Button(frame, text="Calcular", command=calcular).grid(column=2, row=2)

Label(frame, text="Pies").grid(column=0, row=0)
Label(frame, text="Es igual a").grid(column=0, row=1)
Label(frame, text="Metros").grid(column=2, row=1)

feet_input.focus()

window.bind("<Return>", calcular)

window.mainloop()
