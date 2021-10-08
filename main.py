from tkinter import *

window = Tk()
window.title("Feet to Meters")

frame = Frame(window, padx=3, pady=12)
frame.grid(column=0, row=0)

feet = StringVar()
feet_input = Entry(frame, width=7, textvariable=feet)
feet_input.grid(column=1, row=0)

meters = StringVar()
Label(frame, textvariable=meters)