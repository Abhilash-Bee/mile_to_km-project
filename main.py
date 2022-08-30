from tkinter import *

window = Tk()
window.title("Mile to Km conversion")
window.minsize(width=200, height=200)
window.config(padx=50, pady=50)

mile_input = Entry(width=7)
mile_input.grid(column=1, row=0)

mile_label = Label()
mile_label.config(text="Miles", font=("Courier", 20))
mile_label.grid(column=2, row=0)

is_equal_to_label = Label()
is_equal_to_label.config(text="is equal to", font=("Courier", 20))
is_equal_to_label.grid(column=0, row=1)

km_result_label = Label()
km_result_label.config(font=("Courier", 20))
km_result_label.grid(column=1, row=1)

km_label = Label()
km_label.config(text="Km", font=("Courier", 20))
km_label.grid(column=2, row=1)


def button_clicked():
    mile = float(mile_input.get())
    km = round(mile * 1.60934, 2)
    km_result_label.config(text=str(km))


my_button = Button(text="Calculate", command=button_clicked)
my_button.grid(column=1, row=2)

window.mainloop()
