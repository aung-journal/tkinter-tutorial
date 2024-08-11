import tkinter as tk
from tkinter import ttk

window = tk.Tk()
window.title('tkinter variables')

#tkinter variables
string_var = tk.StringVar()

#widgets

label = ttk.Label(master = window, text = 'label', textvariable= string_var)
label.pack()

entry = ttk.Entry(master = window, textvariable = string_var)
entry.pack()

window.mainloop()