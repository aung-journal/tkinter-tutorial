import tkinter as tk
from tkinter import ttk, font

window = tk.Tk()
window.title('Styling')
window.geometry('400x300')

print(font.families())

#style
style = ttk.Style()
# print(style.theme_names())
# style.theme_use('alt')

style.configure('new.TButton', foreground = 'green', font = ('Cantarell', 20))
style.map('new.TButton',
           foreground = [('pressed', 'red'), ('disabled', 'yellow')],
           background = [('pressed', 'green'), ('active', 'blue')]
)

#widgets
label = ttk.Label(window,
                text = 'A label\nAnd then type on another line',
                background='red',
                foreground = 'white',
                font = ('Cantarell', 20),
                justify='center'
                )
label.pack()

button = ttk.Button(window, text = 'A button', style = 'new.TButton')
button.pack()

#exercise:
#add a frame
style.configure('new.TFrame', background = 'pink')
frame = ttk.Frame(window, height = 200, width = 100, style = 'new.TFrame')
frame.pack()

window.bind('<Escape>', lambda event: window.quit())
window.mainloop()