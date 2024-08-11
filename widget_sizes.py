import tkinter as tk
from tkinter import ttk

window = tk.Tk()
window.title('Widget Sizes')
window.geometry('400x300')

#widgets
label1 = ttk.Label(window, text = 'Label1', background = 'green')
label2 = ttk.Label(window, text = 'Label2', background='red', width = 50)
#50 characters size

#90 % of the time, you are going to use the label
# label1.pack()
# label2.pack(fill = 'x')

#grid layout
window.columnconfigure((0, 1), weight = 1, uniform = 'a')
window.rowconfigure((0, 1), weight = 1, uniform = 'a')

label1.grid(row = 0, column=0)
label2.grid(row = 1, column=0)

# grip = ttk.Sizegrip(window)
# grip.pack()
# grip.place(relx = 1.0, rely = 1.0, anchor='se')#this makes the sizing of window flexible
window.bind('<Escape>', lambda event: window.quit())
window.mainloop()