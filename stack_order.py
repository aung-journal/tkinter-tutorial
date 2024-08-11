import tkinter as tk
from tkinter import ttk

window = tk.Tk()
window.title('Stacking order')
window.geometry('400x400')

#exercise: add a third label and button

#widgets
label1 = ttk.Label(window, text = 'Label1', background = 'green')
label2 = ttk.Label(window, text = 'Label2', background='red')
label3 = ttk.Label(window, text = 'Label3', background = 'blue')

# label1.lift()#this makes the label1 top of all of the widgets
# label2.lower()#opposite function

#label1.tkraise()#does the same as lift() method

#aboveThis param, allows only to be above specific widget
#lift and tkraise is just the same also have the same params
button1 = ttk.Button(window, text = 'raise label 1', command = lambda: label1.tkraise(aboveThis=label2))
button2 = ttk.Button(window, text = 'raise label 2', command = lambda: label2.tkraise())
button3 = ttk.Button(window, text = 'raise label 3', command = lambda: label3.tkraise())

label1.place(x = 50, y = 100, width = 200, height = 150)
label2.place( x = 150, y = 60, width = 140, height = 100)
label3.place(x = 20, y = 80, width = 180, height = 100)

button1.place(rely = 1, relx  = 0.75, anchor = 'se')
button2.place(rely = 1, relx  = 1, anchor = 'se')
button3.place(rely = 1, relx = 0.5, anchor = 'se')

window.bind('<Escape>', lambda event: window.quit())
window.mainloop()