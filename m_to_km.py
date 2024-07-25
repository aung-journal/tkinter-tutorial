import tkinter as tk
#from tkinter import ttk
import ttkbootstrap as ttk # type: ignore

window = ttk.Window(themename = 'darkly')
window.title('Demo')
window.geometry('300x150')

def convert():
    mile_input = entry_int.get()
    km_output = mile_input * 1.61
    output_string.set(km_output)

#title
title_label = ttk.Label(master = window, text = 'Miles to kilometres', font = ' Calibri 24 underline')#master is literally parent
title_label.pack()#put this in window

#input field
input_frame = ttk.Frame(master = window)
entry_int = tk.IntVar()#seperate variable that store input of entry
entry = ttk.Entry(master = input_frame, textvariable=entry_int)
button = ttk.Button(master = input_frame, text = 'Convert', command = convert)#we only want to pass function, not calling the function with ()
entry.pack(side = 'left', padx = 10)#put those in input frame
#padx is x axis padding
#pady is y axis padding
button.pack(side = 'left')#put those in input frame
input_frame.pack(pady = 10)#put input_frame in window

#output
output_string = tk.StringVar()#it is going to store a string
output_label = ttk.Label(master = window, text = 'Output', font = 'Calibri 24', textvariable= output_string)
#text variable overwrites whatever inside the label, so we can't see Output anymore
output_label.pack(pady = 5)

window.mainloop()