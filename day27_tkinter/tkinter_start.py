from tkinter import *

window = Tk()
window.title("I`m a title")
window.minsize(width=500, height=300)

# Label

my_label = Label(text="I`m a label", font=("Arial", 24, "bold"))
my_label.pack()

my_label["text"] = "New Text!"
my_label.config(text="New Text-2!")

# Entry

input = Entry(width=10)
input.pack()


# Button

def button_clicked():
    value = input.get()
    my_label.config(text=value)


button = Button(text="Click me!", command=button_clicked)
button.pack()





window.mainloop()
