import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
window = tk.Tk()
window.geometry(("500x500"))
window.title("Weight Conversion")
def WeightThing():
    weights = float(weight.get())
    choice = unit_choices.get()
    if choice == "Kilograms to Pounds":
        result_text.set(weights * 2.2)
    elif choice == "Pounds to Kilograms":
        result_text.set(weights / 2.2)
    elif choice == "Kilograms to Ounces":
        result_text.set(weights * 35.2)
    elif choice == "Ounces to Kilograms":
        result_text.set(weights / 35.2)
    elif choice == "Pounds to Ounces":
        result_text.set(weights * 16)
    elif choice == "Ounces to Pounds":
        result_text.set(weights / 16)
    print(choice)
weight_label = tk.Label(text="weight:")
weight_label.pack(pady="5",anchor="center")
weight = tk.Entry()
weight.pack(pady="5",anchor="center")
unit_choices = tk.StringVar(window)
unit_choices.set("Kilograms to Pounds")
unit_options = ["Kilograms to Pounds", "Pounds to Kilograms", "Kilograms to Ounces", "Ounces to Kilograms", "Pounds to Ounces", "Ounces to Pounds"]
unit_menu = tk.OptionMenu(window,unit_choices,*unit_options)
unit_menu.pack(pady="5", anchor="center")
submit_button = tk.Button(text="Convert", command=WeightThing)
submit_button.pack(pady="5", anchor="center")
result_text = tk.StringVar(window)
outputLabel = tk.Label(window, text="Result: ", textvariable=result_text)
outputLabel.pack(pady="5",anchor="center")
window.mainloop()
