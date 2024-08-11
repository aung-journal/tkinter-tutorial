import tkinter as tk
from tkinter import ttk

window = tk.Tk()
# window.geometry('600x400')
window.title('Frames and parenting')

frame = ttk.Frame(window, width = 200, height = 200, borderwidth = 10, relief = tk.GROOVE)
frame.pack_propagate(False)#This will make the size of the frame not to be set with of its children
frame.pack(side = 'left')

# parenting(master setting)
label = ttk.Label(frame, text = 'Label in  frame')
label.pack()

button = ttk.Button(frame, text = 'button in a frame')
button.pack()

#exercise
frame2 = ttk.Frame(window, width = 200, height = 200, borderwidth = 10, relief = tk.GROOVE)
frame2.pack_propagate(False)#This will make the size of the frame not to be set with of its children
ttk.Label(frame2, text = 'Label in frame2').pack()
ttk.Button(frame2, text = 'button in frame2').pack()
ttk.Entry(frame2).pack()
frame2.pack(side = 'left')

#example
label2 = ttk.Label(window, text = 'Label outside frame')
label2.pack(side= 'left')

window.mainloop()