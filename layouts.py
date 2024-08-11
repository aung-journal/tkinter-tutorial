import tkinter as tk
from tkinter import ttk

window = tk.Tk()
window.title('Layout intro')
window.geometry('600x400')

#widgets
label1 = ttk.Label(window, text = 'Label1', background='red')
label2 = ttk.Label(window, text = 'Label2', background='blue')

#pack
# label1.pack(side = 'left')
# label2.pack(side = 'right')

# label1.pack(side = 'left')
# label2.pack(side = 'left')

# label1.pack(side = 'left', expand = True, fill = 'y')#true is going to make the label to take up the entire screen
# #both means whether you are going to fill in the entire available space
# label2.pack(side = 'left', expand = True, fill='both')

#grid
# window.columnconfigure(0, weight=1)#creates a column
# window.columnconfigure(1, weight=1)#creates a column
# window.columnconfigure(2, weight=2)#creates a column
# window.rowconfigure(1, weight = 1)

# label1.grid(row = 0, column = 1, sticky='nsew')#label only takes up the minimum amount of space
# label2.grid(row = 1, column = 1, columnspan=2, sticky='nsew')#label only takes up the minimum amount of space
# #column span
# #this is going to make widget stick in north

#place
label1.place(x = 100, y = 200, width = 200, height = 100)
#anchor is like where you will set (0, 0), default is ne(north east aka top left corner)
label2.place(relx=0.5, rely = 0.5, relwidth= 1, anchor = 'se')#relx is just relative x (this makes x axis from 0 to 1 and y axis from 0 to 1)#so the top left corner is (0, 0)
#when you are using place, you normally uses relative x
window.bind('<Escape>', lambda event: window.quit())
window.mainloop()