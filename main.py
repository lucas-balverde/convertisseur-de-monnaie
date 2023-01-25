
from tkinter import *
from tkinter import ttk
import tkinter as tk

########################################
                  #GUI
########################################

#def fenetre
window = tk.Tk()
window.title("convertisseur")
window.geometry("500x500")

#def Label
amoutLabel = tk.Label(window, text="Quantité :", bg="lightgrey", font = ("Arial", 20), width=20)
amoutLabel.pack(pady=20)

#def entry
Entryvalue = tk.Entry(window, width=20)
Entryvalue.pack(pady=20)

#label 
lbl = tk.Label(window,text = "Monnaie a convertir:")
lbl.pack(pady=10)

#faire un menu déroulant de la monnaie a convertir 
fromCurrency=["USD","EUR","GBP","JPY"]
fromMenu = ttk.Combobox(window, values=fromCurrency)
fromMenu.current(0)
fromMenu.pack(pady=20)

#label
lbl2 = Label(window,text = "Monnaie convertie:") 
lbl2.pack(pady=5)

#faire une deuxieme liste de la monnaie que l'on souhaite 
toCurrency=["USD","EUR","GBP","JPY"]
toMenu = ttk.Combobox(window, values=toCurrency)
toMenu.current(0)
toMenu.pack(pady=20)

# Création d'une zone de texte pour afficher le résultat de la conversion
printResult = Listbox(window, width=40, height=4)
printResult.pack(pady=20)

# Taux de change fixes pour effectuer les conversions
USD_TO_EUR = 0.92
USD_TO_JPY = 128.74
EUR_TO_JPY = 139.37
USD_TO_GBP = 0.80
EUR_TO_GBP = 0.87
JPY_TO_GBP = 0.0016

# Fonction qui vérifie si les devises selectionnées sont différente
#a la place de cette fonction je pourrais faire en sorte que le résultat soit le meme que le montant saisi a la base en faisant montant*1
def check_diff_currencies(fromCurrency, toCurrency):
    if fromCurrency == toCurrency:
        print("conversion impossible")
        return False
    return True

# Fonction qui calcule la conversion
def calculate_conversion(amount, fromCurrency, toCurrency):
    if fromCurrency == 'USD':
        if toCurrency == 'EUR':
            return amount * USD_TO_EUR
        elif toCurrency == 'JPY':
            return amount * USD_TO_JPY
        elif toCurrency == "GBP":
            return amount * USD_TO_GBP
    elif fromCurrency == 'EUR':
        if toCurrency == 'USD':
            return amount / USD_TO_EUR
        elif toCurrency == 'JPY':
            return amount * EUR_TO_JPY
        elif toCurrency == 'GBP':
            return amount * EUR_TO_GBP
    elif fromCurrency == 'JPY':
        if toCurrency == 'USD':
            return amount / USD_TO_JPY
        elif toCurrency == 'EUR':
            return amount / EUR_TO_JPY
        elif toCurrency == 'GBP':
            return amount * JPY_TO_GBP
    elif fromCurrency == 'GBP':
        if toCurrency == 'EUR':
            return amount / EUR_TO_GBP
        elif toCurrency == 'JPY':
            return amount / JPY_TO_GBP
        elif toCurrency == "USD":
            return amount / USD_TO_GBP

# Fonction appelée quand "Convertir" est cliqué
def on_convert_clicked():
    amount = float(Entryvalue.get())
    fromCurrency = fromMenu.get()
    toCurrency = toMenu.get()
    if check_diff_currencies(fromCurrency, toCurrency):
        result = str(calculate_conversion(amount, fromCurrency, toCurrency))
        printResult.delete(0, END)
        printResult.insert(0, result)

#enregistrement de l'historique
        fichier =open("historique.txt", "a")
        fichier.writelines([str(amount), " ", fromCurrency, " ", '->', " ", result, " ", toCurrency, '\n'])

#def Button
Convertir = tk.Button(window, text =("Convertir"), bg ="lightgrey", fg ="darkblue", font=("Arial", 20), width=20, command=on_convert_clicked)
Convertir.pack()

window.mainloop()