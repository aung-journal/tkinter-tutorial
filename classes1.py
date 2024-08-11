import tkinter as tk
from tkinter import ttk

def create_segment(parent, label_text, button_text):
    frame = ttk.Frame(parent)

    frame.rowconfigure(0, weight = 1)
    frame.columnconfigure((0, 1, 2), weight = 1, uniform='a')

    #widgets
    ttk.Label(frame, text = label_text).grid(row = 0, column=0 , sticky = 'nsew')
    ttk.Button(frame, text = button_text).grid(row = 0, column = 1, sticky = 'nsew')

    return frame

class Segment(ttk.Frame):
    def __init__(self, parent, label_text, button_text, entry_button_text):
        super().__init__(parent)

        #grid layout
        self.rowconfigure(0, weight = 1)
        self.columnconfigure((0, 1, 2), weight = 1, uniform='a')
        ttk.Label(self, text = label_text).grid(row = 0, column=0 , sticky = 'nsew')
        ttk.Button(self, text = button_text).grid(row = 0, column = 1, sticky = 'nsew')

        #entry layout
        self.create_entry(self, entry_button_text).grid(row = 0, column = 2, sticky = 'nsew', padx = 10, pady = 10)

        #place method
        self.pack(expand = True, fill = 'both', padx = 10, pady = 10)

    def create_entry(self, parent, button_text):
        frame = ttk.Frame(parent)
        
        ttk.Entry(frame).pack(expand = True, fill = 'both')
        ttk.Button(frame, text = button_text).pack(expand = True, fill = 'both')

        return frame

window = tk.Tk()
window.title('Widget and Return')
window.geometry('400x600')

#widgets

#functional 
# create_segment(window, 'label', 'button').pack(expand = True, fill = 'both', padx = 10, pady = 10)
# create_segment(window, 'test', 'click').pack(expand = True, fill = 'both', padx = 10, pady = 10)
# create_segment(window, 'hello', 'test').pack(expand = True, fill = 'both', padx = 10, pady = 10)
# create_segment(window, 'bye', 'launch').pack(expand = True, fill = 'both', padx = 10, pady = 10)
# create_segment(window, 'last one', 'exit').pack(expand = True, fill = 'both', padx = 10, pady = 10)

#classes
Segment(window, 'label', 'button', 'Exercise')
Segment(window, 'test', 'click', 'Exercise'),
Segment(window, 'hello', 'test', 'Exercise'),
Segment(window, 'bye', 'launch', 'Exercise')
Segment(window, 'last one', 'exit', 'Exercise')

#exercise


window.bind('<Escape>', lambda event: window.quit())
window.mainloop()