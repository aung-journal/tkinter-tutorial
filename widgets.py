import tkinter as tk
from tkinter import ttk

window = tk.Tk()
window.title('Getting and setting widgets')

def button_func():
    #get method only work with entry now, not label and button
    # update the label
    #label.configure(text = 'some other text')
    label['text'] = entry.get()
    entry['state'] = 'disabled'

def exercise_button_func():
    label['text'] = 'some text'
    entry['state'] = 'enabled'

#widgets
label = ttk.Label(master = window, text = 'widgets')
label.pack()

entry = ttk.Entry(master = window)
entry.pack()

button = ttk.Button(master = window, text = 'Button', command = button_func)
button.pack()

#exercise button
exercise_button = ttk.Button(master = window, text = 'Exercise Button', command = exercise_button_func)
exercise_button.pack()

window.mainloop()