import tkinter as tk
from tkinter import ttk

def get_pos(event):
    print(f'x: {event.x}, y: {event.y}')

window = tk.Tk()
window.geometry('600x500')
window.title('Event Binding')

text = tk.Text(window)
text.pack()

entry = ttk.Entry(window)
entry.pack()

button = ttk.Button(window, text = 'A button')
button.pack()

#Events
# button.bind('<Alt-KeyPress-a>', lambda event: print(event))
# #function of bind always have to take a param about event
# window.bind('<Motion>', get_pos)#once I am in the text only works

# window.bind('<KeyPress>', lambda event: print('a button was pressed.'))

#this is just selected once(not same as KeyPress)
entry.bind('<FocusIn>', lambda event: print('entry field was selected.'))
#this is just deselected once
entry.bind('<FocusOut>', lambda event: print('entry field was deselected.'))

#exercise
text.bind('<Shift-MouseWheel>', lambda event: print('Mousewheel'))

window.mainloop()