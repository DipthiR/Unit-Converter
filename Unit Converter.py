import tkinter as tk
from tkinter import ttk, messagebox

# Units for different categories
unit_data = {
    "Length": {
        "meter": 1,
        "kilometer": 1000,
        "centimeter": 0.01,
        "millimeter": 0.001,
        "mile": 1609.34,
        "yard": 0.9144,
        "foot": 0.3048,
        "inch": 0.0254
    },
    "Weight": {
        "gram": 1,
        "kilogram": 1000,
        "milligram": 0.001,
        "pound": 453.592,
        "ounce": 28.3495
    },
    "Temperature": ["celsius", "fahrenheit", "kelvin"]
}

# Conversion function
def convert_units():
    category = category_var.get()
    from_unit = from_unit_var.get()
    to_unit = to_unit_var.get()
    try:
        value = float(entry_value.get())
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid number.")
        return

    if category == "Temperature":
        result = convert_temperature(value, from_unit, to_unit)
    else:
        base_value = value * unit_data[category][from_unit]
        result = base_value / unit_data[category][to_unit]
    
    label_result.config(text=f"{value} {from_unit} = {round(result, 4)} {to_unit}")

def convert_temperature(value, from_unit, to_unit):
    if from_unit == to_unit:
        return value
    if from_unit == "celsius":
        return (value * 9/5) + 32 if to_unit == "fahrenheit" else value + 273.15
    elif from_unit == "fahrenheit":
        return (value - 32) * 5/9 if to_unit == "celsius" else ((value - 32) * 5/9) + 273.15
    elif from_unit == "kelvin":
        return value - 273.15 if to_unit == "celsius" else ((value - 273.15) * 9/5) + 32

def update_units(*args):
    from_unit_menu['values'] = to_unit_menu['values'] = list(
        unit_data[category_var.get()].keys()
        if category_var.get() != "Temperature"
        else unit_data["Temperature"]
    )
    from_unit_var.set(from_unit_menu['values'][0])
    to_unit_var.set(to_unit_menu['values'][1])

def clear_fields():
    entry_value.delete(0, tk.END)
    label_result.config(text="")

# GUI setup
app = tk.Tk()
app.title("🧮 Smart Unit Converter")
app.geometry("500x400")
app.config(bg="#f5f5f5")
app.resizable(False, False)

style = ttk.Style(app)
style.configure('TLabel', font=('Segoe UI', 12))
style.configure('TButton', font=('Segoe UI', 11, 'bold'), padding=6)
style.configure('TCombobox', font=('Segoe UI', 11), padding=4)

# Widgets
tk.Label(app, text="Unit Converter", font=("Segoe UI", 18, "bold"), bg="#f5f5f5", fg="#333").pack(pady=10)

category_var = tk.StringVar(value="Length")
category_menu = ttk.Combobox(app, textvariable=category_var, values=list(unit_data.keys()), state='readonly')
category_menu.pack(pady=5)
category_menu.bind('<<ComboboxSelected>>', update_units)

entry_value = tk.Entry(app, font=("Segoe UI", 14), justify='center')
entry_value.pack(pady=10)

from_unit_var = tk.StringVar()
to_unit_var = tk.StringVar()

from_unit_menu = ttk.Combobox(app, textvariable=from_unit_var, state='readonly')
to_unit_menu = ttk.Combobox(app, textvariable=to_unit_var, state='readonly')
from_unit_menu.pack(pady=5)
to_unit_menu.pack(pady=5)

frame_buttons = tk.Frame(app, bg="#f5f5f5")
frame_buttons.pack(pady=10)

btn_convert = ttk.Button(frame_buttons, text="Convert", command=convert_units)
btn_clear = ttk.Button(frame_buttons, text="Clear", command=clear_fields)
btn_convert.grid(row=0, column=0, padx=10)
btn_clear.grid(row=0, column=1, padx=10)

label_result = tk.Label(app, text="", font=("Segoe UI", 14, "italic"), fg="#006666", bg="#f5f5f5")
label_result.pack(pady=20)

update_units()  # Initialize default units

app.mainloop()
