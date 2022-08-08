from tkinter import *

window = Tk()
window.title("Converter")
window.config(padx=20, pady=20)

miles_entry = Entry(width=7)
miles_entry.grid(column=1, row=0)
miles_entry_value = miles_entry.get()

print(type(miles_entry_value))