import tkinter as tk
from tkinter import ttk

window = tk.Tk()
window.title('Hide widgets')
window.geometry('600x400')

#place method
# def toggle_label_place():
#     global label_visible

#     if label_visible:
#         label.place_forget()
#         label_visible = False
#     else:
#         label_visible = True
#         label.place(relx = 0.5, rely = 0.5, anchor = 'center')

# button = ttk.Button(window, text = 'toggle Label', command = toggle_label_place)
# button.place(x = 10, y = 10)

# label_visible = True
# label = ttk.Label(window, text = 'A label')
# label.place(relx = 0.5, rely = 0.5, anchor = 'center')

#grid method

# def toggle_label_grid():
#     global label_visible
    
#     if label_visible:
#         label.grid_forget()
#         label_visible = False
#     else:
#         label_visible = True
#         label.grid(column = 1, row = 0)

# window.columnconfigure((0, 1), weight = 1, uniform = 'a')
# window.rowconfigure(0, weight = 1, uniform = 'a')

# button = ttk.Button(window, text = 'toggle Label', command = toggle_label_grid)
# button.grid(column = 0, row = 0)

# label_visible = True
# label = ttk.Label(window, text = 'A label')
# label.grid(column = 1, row = 0)

#pack method

#for toggling, you should use either grid or place
def toggle_label_pack():
    global label_visible

    if label_visible:
        label.pack_forget()
        label_visible = False
        frame.pack(expand = True, before = button)#we can pack frame before button using this param before
    else:
        frame.pack_forget() 
        label.pack(expand = True, before = button)
        label_visible = True
    # #exercise: so the button stays on the bottom(my sol)
    # button.pack(side = 'bottom')

label_visible = True
label = ttk.Label(window, text = 'A label')
label.pack(expand = True)

button = ttk.Button(window, text = 'toggle Label', command = toggle_label_pack)
button.pack()

frame = ttk.Frame(window)

window.bind('<Escape>', lambda event: window.quit())
window.mainloop()