import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
window = tk.Tk()
window.geometry(("500x500"))
window.title("Calculator")
def Calculator():
    number1 = float(num1.get())
    number2 = float(num2.get())
    choice = unit_choices.get()
    if choice == "Addition":
        result_text.set(number1 + number2)
    elif choice == "Subtraction":
        result_text.set(number1 - number2)
    elif choice == "Multplication":
        result_text.set(number1 * number2)
    elif choice == "Division":
        result_text.set(number1 / number2)
    print(choice)
num1_label = tk.Label(text="Enter Number 1:")
num1_label.pack(pady="5",anchor="center")
num1 = tk.Entry()
num1.pack(pady="5",anchor="center")
num2_label = tk.Label(text="Enter Number 2:")
num2_label.pack(pady="5",anchor="center")
num2 = tk.Entry()
num2.pack(pady="5",anchor="center")
unit_choices = tk.StringVar(window)
unit_choices.set("Addition")
unit_options = ["Addition", "Subtraction","Multiplication","Division"]
unit_menu = tk.OptionMenu(window,unit_choices,*unit_options)
unit_menu.pack(pady="5", anchor="center")
result_text = tk.StringVar(window)
outputLabel = tk.Label(window, text="Result: ", textvariable=result_text)
outputLabel.pack(pady="5",anchor="center")
submit_button = tk.Button(text="Convert", command=Calculator)
submit_button.pack(pady="5", anchor="center")
window.mainloop()
