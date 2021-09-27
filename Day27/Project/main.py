import tkinter


def calc():
    input_num = entry.get()
    to_km = int(input_num) * 1.609
    km.config(text=to_km)


window = tkinter.Tk()
window.title("Mile to Km Converter")
window.minsize(width=300, height=120)
window.config(padx=20, pady=20)

my_label = tkinter.Label(text="is equal to", font=("Arial", 15, "normal"))
my_label.grid(column=0, row=2)

entry = tkinter.Entry(width=10)
entry.grid(column=1, row=1)

miles_unit = tkinter.Label(text="Miles", font=("Arial", 15, "normal"))
miles_unit.grid(column=2, row=1)

km = tkinter.Label(text="0", font=("Arial", 15, "normal"))
km.grid(column=1, row=2)

km_unit = tkinter.Label(text="Km", font=("Arial", 15, "normal"))
km_unit.grid(column=2, row=2)

new_button = tkinter.Button(text="Calculate", command=calc)
new_button.grid(column=1, row=3)

window.mainloop()
