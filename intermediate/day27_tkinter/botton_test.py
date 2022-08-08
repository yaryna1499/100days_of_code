from tkinter import Button, Label, Tk

window = Tk()

my_label = Label(text="default")
my_label.pack()




def button_clicked():
    n = int()
    my_label["text"] = str(n+1)
    print(my_label["text"])


button = Button(text="I`m a button!", command=button_clicked)
button.pack()

window.mainloop()
