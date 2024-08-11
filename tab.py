import tkinter as tk
from tkinter import ttk

window = tk.Tk()
window.geometry('600x400')
window.title("Tab Widget")

#notebook widget
notebook =ttk.Notebook(window)

tab1 = ttk.Frame(notebook)
label1 = ttk.Label(tab1, text = 'Text in tab 1')
label1.pack()
button1 = ttk.Button(tab1, text = 'Button in tab 1')
button1.pack()

tab2 = ttk.Frame(notebook)
label2 = ttk.Label(tab2, text = 'Text in tab 2')
label2.pack()
entry2 = ttk.Entry(tab2)
entry2.pack()

#exercise
tab3 = ttk.Frame(notebook)

button3a = ttk.Button(tab3, text = 'Button a in tab 3')
button3a.pack()

button3b = ttk.Button(tab3, text = 'Button b in tab 3')
button3b.pack()

label3 = ttk.Label(tab3, text = 'Label in tab 3')
label3.pack()

notebook.add(tab1, text = 'Tab 1')
notebook.add(tab2, text = 'Tab 2')
notebook.add(tab3, text = 'Tab 3')

notebook.pack()

window.mainloop()