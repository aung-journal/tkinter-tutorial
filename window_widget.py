import tkinter as tk
from tkinter import ttk

def button_func():
    print('A button was pressed.')

def button1_func():
    print('hello')

window = tk.Tk()
window.title('Window and Widgets')
window.geometry('800x500')

# ttk label
label = ttk.Label(master = window, text = 'This is a test')
label.pack()

# tk.Text
text = tk.Text(master = window)#multiline text entry
text.pack()

#ttk entry
entry = ttk.Entry(master = window)
entry.pack()# singleline text entry

#ttk Label
label = ttk.Label(master = window, text = 'my label')
label.pack()

#ttk button
button = ttk.Button(master = window, text = 'Button', command = button_func)
button.pack()

#ttk button
# button1 = ttk.Button(master = window, text = 'Button 1', command = button1_func)
button1 = ttk.Button(master = window, text = 'Button 1', command = lambda: print('hello'))
button1.pack()

#run
window.mainloop()
print('hello')
