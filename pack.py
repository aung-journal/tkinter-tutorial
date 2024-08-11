import tkinter as tk
from tkinter import ttk

window = tk.Tk()
window.title('Pack')
window.geometry('400x600')

#widgets
label1 = ttk.Label(window, text = 'Label1', background = 'red')
label2 = ttk.Label(window, text = 'Label2', background='blue')
label3 = ttk.Label(window, text = 'Label3', background='green')
button = ttk.Button(window, text = 'Button')

#layouts
# label1.pack(side = 'top', expand = True, fill = 'both')
# label2.pack(side = 'top', fill = 'x')
# label3.pack(side = 'top')
# button.pack(side = 'top', expand = True, fill = 'y')

#exercise 1(this)
#you are really just going to only use padx or pady
# label1.pack(side = 'right', expand = True, fill = 'both')
# label2.pack(side = 'top', expand = True, fill = 'both')
# label3.pack(side = 'top', expand = True, fill = 'both')
# button.pack(side = 'top', expand = True, fill = 'both')

#exercise 2(mixed side)
label1.pack(side = 'top', expand = True, fill = 'both', padx = 10, pady = 10)
label2.pack(side = 'left', expand = True, fill = 'both')
label3.pack(side = 'top', expand = True, fill = 'both')
button.pack(side = 'top', expand = True, fill = 'both')

window.bind('<Escape>', lambda event: window.quit())
window.mainloop()
