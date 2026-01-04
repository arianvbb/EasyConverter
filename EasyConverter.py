import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Converter")
root.geometry("500x300")

notebook = ttk.Notebook(root)
notebook.pack(pady = 10, expand = True, fill='both')

Temp = ttk.Frame(notebook, width = 500, height = 300)
Mass = ttk.Frame(notebook, width = 500, height = 300)
Power = ttk.Frame(notebook, width = 500, height = 300)
Energy = ttk.Frame(notebook, width = 500, height = 300)

notebook.add(Temp)
notebook.add(Mass)
notebook.add(Power)
notebook.add(Energy)

notebook.add(Temp, text='Temperature')
notebook.add(Mass, text='Mass')
notebook.add(Power, text='Power')
notebook.add(Energy, text='Energy')


#TEMPERATURE
label = tk.Label(Temp, text = "Temperature", font = ('Arial', 20), anchor="center")
label.grid(row = 0, columnspan = 1, column = 1, padx = 0, pady = 20)

TempAmount = tk.Entry(Temp)
TempAmount.grid(row = 1, column = 0, padx = 30, pady = 20, sticky = 'w')

def on_select(event):
    Selected_from_temp = Temp_dropdown.get()

def temp_calculation():
    if Temp_dropdown.get() == "Celcius":
        Fahrenheit = float(TempAmount.get()) * 9/5 + 32
        Kelvin = float(TempAmount.get()) + 273.15
        results = tk.Label(Temp, text = f"You have {Fahrenheit:.1f} Fahrenheit and {Kelvin:.1f} Kelvin", font = ('Arial, 10'))
        results.grid(row = 2, column = 0, columnspan = 4, padx = 0, pady = 0)
    elif Temp_dropdown.get() == "Kelvin":
        Celcius = float(TempAmount.get()) - 273.15
        Fahrenheit = Celcius * 9/5 + 32
        results = tk.Label(Temp, text = f"You have {Celcius:.1f} Celcius and {Fahrenheit:.1f} Fahrenheit", font = ('Arial, 10'))
        results.grid(row = 2, column = 0, columnspan = 4, padx = 0, pady = 0)
    elif Temp_dropdown.get() == "Fahrenheit":
        Celcius = ((float(TempAmount.get())) - 32) * 5/9
        Kelvin = Celcius + 273.15
        results = tk.Label(Temp, text = f"You have {Celcius:.1f} Celcius and {Kelvin:.1f} Kelvin", font = ('Arial, 10'))
        results.grid(row = 2, column = 0, columnspan = 4, padx = 0, pady = 0)
    else: 
        print("You have an error")

Temp_Options = [
    "Kelvin",
    "Celcius",
    "Fahrenheit"
]

Temp_dropdown = ttk.Combobox(Temp, values = Temp_Options, state = "readonly")
Selected_from_temp = Temp_dropdown.get()
Temp_dropdown.grid(row = 1, column = 1, padx = 0, pady = 10, sticky = 'e')
Temp_dropdown.set(Temp_Options[0])
Temp_dropdown.bind("<<ComboboxSelected>>", on_select)

Temp_Convert = tk.Button(Temp, text = "Convert", font = ('Arial', 14), command = temp_calculation)
Temp_Convert.grid(row = 1, column = 3, padx = 50, pady = 0, sticky = "w")


#MASS
label = tk.Label(Mass, text = "Mass", font = ('Arial', 20), anchor="center")
label.grid(row = 0, columnspan = 1, column = 1, padx = 0, pady = 20)

MassAmount = tk.Entry(Mass)
MassAmount.grid(row = 1, column = 0, padx = 30, pady = 20, sticky = 'w')

def on_select(event):
    Selected_from_mass = Mass_dropdown.get()

def mass_calculation():
    if Mass_dropdown.get() == "Kilogram":
        Gram = float(MassAmount.get()) * 10
        Milligram = float(MassAmount.get()) * 100
        Tonne = float(MassAmount.get()) / 1000
        Pound = float(MassAmount.get()) * 2.20462
        Ounce = Pound * 16
        results = tk.Label(Mass, text = f"You have {Gram:.1f} Grams, {Milligram:.1f} Milligrams, {Tonne:.1f} Tonnes, {Pound:.1f} Pounds and {Ounce:.1f} Ounces", font = ('Arial, 10'))
        results.grid(row = 2, column = 0, columnspan = 4, padx = 0, pady = 0)
    elif Mass_dropdown.get() == "Gram":
        Kilogram = float(MassAmount.get()) / 10
        Milligram = float(MassAmount.get()) * 100
        Tonne = float(MassAmount.get()) / 1000
        Pound = float(MassAmount.get()) * 2.20462
        Ounce = Pound * 16
        results = tk.Label(Mass, text = f"You have {Kilogram:.1f} Kilograms, {Milligram:.1f} Milligrams, {Tonne:.1f} Tonnes, {Pound:.1f} Pounds and {Ounce:.1f} Ounces", font = ('Arial, 10'))
        results.grid(row = 2, column = 0, columnspan = 4, padx = 0, pady = 0)
    elif Mass_dropdown.get() == "Milligram":
        Kilogram = float(MassAmount.get()) / 100
        Gram = float(MassAmount.get()) / 10
        Tonne = float(MassAmount.get()) / 1000
        Pound = float(MassAmount.get()) * 2.20462
        Ounce = Pound * 16
        results = tk.Label(Mass, text = f"You have {Gram:.1f} Grams, {Kilogram:.1f} Kilograms, {Tonne:.1f} Tonnes, {Pound:.1f} Pounds and {Ounce:.1f} Ounces", font = ('Arial, 10'))
        results.grid(row = 2, column = 0, columnspan = 4, padx = 0, pady = 0)
    elif Mass_dropdown.get() == "Tonne":
        Kilogram = float(MassAmount.get()) / 100
        Gram = float(MassAmount.get()) / 10
        Tonne = float(MassAmount.get()) / 1000
        Pound = float(MassAmount.get()) * 2.20462
        Ounce = Pound * 16
        results = tk.Label(Mass, text = f"You have {Gram:.1f} Grams, {Milligram:.1f} Milligrams, {Kilogram:.1f} Kilograms, {Pound:.1f} Pounds and {Ounce:.1f} Ounces", font = ('Arial, 10'))
        results.grid(row = 2, column = 0, columnspan = 4, padx = 0, pady = 0)
    elif Mass_dropdown.get() == "Pound":
        Kilogram = float(MassAmount.get()) / 100
        Gram = float(MassAmount.get()) / 10
        Tonne = float(MassAmount.get()) / 1000
        Pound = float(MassAmount.get()) * 2.20462
        Ounce = Pound * 16
        results = tk.Label(Mass, text = f"You have {Gram:.1f} Grams, {Milligram:.1f} Milligrams, {Tonne:.1f} Tonnes, {Kilogram:.1f} Kilograms and {Ounce:.1f} Ounces", font = ('Arial, 10'))
        results.grid(row = 2, column = 0, columnspan = 4, padx = 0, pady = 0)
    elif Mass_dropdown.get() == "Ounce":
        Kilogram = float(MassAmount.get()) / 100
        Gram = float(MassAmount.get()) / 10
        Tonne = float(MassAmount.get()) / 1000
        Pound = float(MassAmount.get()) * 2.20462
        Ounce = Pound * 16
        results = tk.Label(Mass, text = f"You have {Gram:.1f} Grams, {Milligram:.1f} Milligrams, {Tonne:.1f} Tonnes, {Pound:.1f} Pounds and {Kilogram:.1f} Kilograms", font = ('Arial, 10'))
        results.grid(row = 2, column = 0, columnspan = 4, padx = 0, pady = 0)
    else: 
        print("You have an error")

Mass_Options = [
    "Kilogram",
    "Gram",
    "Milligram",
    "Tonne",
    "Pound",
    "Ounce"
]

Mass_dropdown = ttk.Combobox(Mass, values = Mass_Options, state = "readonly")
Selected_from_weight = Mass_dropdown.get()
Mass_dropdown.grid(row = 1, column = 1, padx = 0, pady = 10, sticky = 'e')
Mass_dropdown.set(Mass_Options[0])
Mass_dropdown.bind("<<ComboboxSelected>>", on_select)

Mass_Convert = tk.Button(Mass, text = "Convert", font = ('Arial', 14), command = mass_calculation)
Mass_Convert.grid(row = 1, column = 3, padx = 50, pady = 0, sticky = "w")


#FORCE
label = tk.Label(Power, text = "Power", font = ('Arial', 20), anchor="center")
label.grid(row = 0, columnspan = 1, column = 1, padx = 0, pady = 20)

PowerAmount = tk.Entry(Power)
PowerAmount.grid(row = 1, column = 0, padx = 30, pady = 20, sticky = 'w')

def on_select(event):
    Selected_from_force = Power_dropdown.get()

def power_calculation():
    if Power_dropdown.get() == "Watt":
        kW = float(PowerAmount.get()) / 1000
        MW = kW / 1000
        Hp = float(PowerAmount.get()) / 745.7
        results = tk.Label(Power, text = f"You have {kW:.1f} kW, {MW:.1f} MW and {Hp:.1f} Hp", font = ('Arial, 10'))
        results.grid(row = 2, column = 0, columnspan = 4, padx = 0, pady = 0)
    elif Power_dropdown.get() == "kW":
        Watt = float(PowerAmount.get()) * 1000
        MW = Watt / 1000000
        Hp = Watt / 745.7
        results = tk.Label(Power, text = f"You have {Watt:.1f} Watt, {MW:.1f} MW and {Hp:.1f} Hp", font = ('Arial, 10'))
        results.grid(row = 2, column = 0, columnspan = 4, padx = 0, pady = 0)
    elif Power_dropdown.get() == "MW":
        Watt = float(PowerAmount.get()) * 1000000
        kW = Watt / 1000
        Hp = Watt / 745.7
        results = tk.Label(Power, text = f"You have {Watt:.1f} Watt, {kW:.1f} kW and {Hp:.1f} Hp", font = ('Arial, 10'))
        results.grid(row = 2, column = 0, columnspan = 4, padx = 0, pady = 0)
    elif Power_dropdown.get == "Hp":
        Watt = float(PowerAmount.get()) * 745.7
        kW = Watt  / 1000
        MW = Watt / 1000000
        results = tk.Label(Power, text = f"You have {Watt:.1f} Watt, {kW:.1f} kW and {MW:.1f} MW", font = ('Arial, 10'))
        results.grid(row = 2, column = 0, columnspan = 4, padx = 0, pady = 0)
    else: 
        print("You have an error")

Power_Options = [
    "Watt",
    "kW",
    "MW",
    "Hp"
]

Power_dropdown = ttk.Combobox(Power, values = Power_Options, state = "readonly")
Selected_from_power = Power_dropdown.get()
Power_dropdown.grid(row = 1, column = 1, padx = 0, pady = 10, sticky = 'e')
Power_dropdown.set(Power_Options[0])
Power_dropdown.bind("<<ComboboxSelected>>", on_select)

Power_Convert = tk.Button(Power, text = "Convert", font = ('Arial', 14), command = power_calculation)
Power_Convert.grid(row = 1, column = 3, padx = 50, pady = 0, sticky = "w")

#ENERGY
label = tk.Label(Energy, text = "Energy", font = ('Arial', 20), anchor="center")
label.grid(row = 0, columnspan = 1, column = 1, padx = 0, pady = 20)

EnergyAmount = tk.Entry(Energy)
EnergyAmount.grid(row = 1, column = 0, padx = 30, pady = 20, sticky = 'w')

def on_select(event):
    Selected_from_energy = Energy_dropdown.get()

def energy_calculation():
    if Energy_dropdown.get() == "Joule":
        kWh = float(EnergyAmount.get()) / (3.6 * 10**6)
        eV = float(EnergyAmount.get()) * 1.602176634 * 10**-19
        Cal = float(EnergyAmount.get()) * 4.184

        results = tk.Label(Energy, text = f"You have {kWh:.1f} kWh, {eV:.1f} eV and {Cal:.1f} Cal", font = ('Arial, 10'))
        results.grid(row = 2, column = 0, columnspan = 4, padx = 0, pady = 0)
    elif Energy_dropdown.get() == "kWh":
        Joule = float(EnergyAmount.get()) / (3.6 * 10**6)
        eV = Joule * 1.602176634 * 10**-19
        Cal = Joule * 4.184

        results = tk.Label(Energy, text = f"You have {Joule:.1f} Joule, {eV:.1f} eV and {Cal:.1f} Cal", font = ('Arial, 10'))
        results.grid(row = 2, column = 0, columnspan = 4, padx = 0, pady = 0)
    elif Energy_dropdown.get() == "eV":
        Joule = (float(EnergyAmount.get())) / (1.602176634 * 10**-19)
        kWh = Joule * 3.6 * 10**6
        Cal = Joule * 4.184

        results = tk.Label(Energy, text = f"You have {Joule:.1f} Joule, {kWh:.1f} kWh and {Cal:.1f} Cal", font = ('Arial, 10'))
        results.grid(row = 2, column = 0, columnspan = 4, padx = 0, pady = 0)
    elif Energy_dropdown.get() == "Cal":
        Joule = float(EnergyAmount.get()) / 4.184
        kWh = Joule * 3.6 * 10**6
        eV = Joule * 1.602176634 * 10**-19

        results = tk.Label(Energy, text = f"You have {Joule:.1f} Joule, {kWh:.1f} kWh and {eV:.1f} eV", font = ('Arial, 10'))
        results.grid(row = 2, column = 0, columnspan = 4, padx = 0, pady = 0)
    else: 
        print("You have an error")

Energy_Options = [
    "Joule",
    "kWh",
    "eV",
    "Cal"
]

Energy_dropdown = ttk.Combobox(Energy, values = Energy_Options, state = "readonly")
Selected_from_energy = Energy_dropdown.get()
Energy_dropdown.grid(row = 1, column = 1, padx = 0, pady = 10, sticky = 'e')
Energy_dropdown.set(Energy_Options[0])
Energy_dropdown.bind("<<ComboboxSelected>>", on_select)

Energy_Convert = tk.Button(Energy, text = "Convert", font = ('Arial', 14), command = energy_calculation)
Energy_Convert.grid(row = 1, column = 3, padx = 50, pady = 0, sticky = "w")



root.mainloop()