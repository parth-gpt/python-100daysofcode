import tkinter


def button_clicked():
    new_text = input.get()
    my_label.config(text=new_text)


window = tkinter.Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)

# Label
my_label = tkinter.Label(text="I am a Label", font=("Arial", 24, "normal"))
my_label["text"] = "new text"
my_label.config(text="new text")
my_label.grid(column=0, row=0)

# Button
button = tkinter.Button(text="click me", command=button_clicked)
button.grid(column=1, row=1)
button.config(padx=10, pady=10)

new_button = tkinter.Button(text="new click me", command=button_clicked)
new_button.grid(column=2, row=0)
# button.pack()

# Entry
input = tkinter.Entry(width=15)
input.grid(column=3, row=2)
# input.pack()




window.mainloop()
