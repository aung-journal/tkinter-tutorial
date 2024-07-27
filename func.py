import tkinter as tk
from tkinter import ttk


#two ways to make this work
def button_func(entry_string):
    print('a button was pressed')
    print(entry_string.get())
    #so it still executes for one time
    #this is a void function, but command receives None, so it executes nothing later

def outer_func(param):
    def inner_func():
        print('a button was pressed')
        print(param.get())
    return inner_func

window = tk.Tk()
window.title('buttons, functions and argumnets')

entry_string = tk.StringVar(value = 'test')
entry = ttk.Entry(window, textvariable= entry_string)
entry.pack()

# button = ttk.Button(window, text = 'button', command = lambda: button_func(entry_string))
button = ttk.Button(window, text = 'button', command = outer_func(entry_string))
button.pack()

window.mainloop()