from tkinter import *


def miles_to_km():
    miles = miles_entry.get()
    km = float(miles)*1.60934
    km_result_value["text"] = str(km)




window = Tk()
window.title("Converter")
window.config(padx=20, pady=20)

miles_entry = Entry(width=7)
miles_entry.grid(column=1, row=0)


miles_label = Label(text="miles")
miles_label.grid(column=2, row=0)

is_equal_label = Label(text="is equal to")
is_equal_label.grid(column=0, row=1)

km_result_value = Label(text="0")
km_result_value.grid(column=1, row=1)

km_label = Label(text="km")
km_label.grid(column=2, row=1)

calculate_button = Button(text="calculate", command=miles_to_km)
calculate_button.grid(column=1, row=2)







window.mainloop()