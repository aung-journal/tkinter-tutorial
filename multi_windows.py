import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

class Extra(tk.Toplevel):
    def __init__(self, title, size):
        super().__init__()
        self.title(title)
        self.geometry(f'{size[0]}x{size[1]}')

        self.create_widgets()

    def create_widgets(self):
        ttk.Label(extra_window, text = 'A label').pack()
        ttk.Button(extra_window, text = 'A button').pack()
        ttk.Label(extra_window, text = 'Another label').pack(expand = True)

    def close_window(self):
        self.destroy()
#
def ask_yes_no():
    # answer = messagebox.askquestion("Title", 'Do you accept it?')
    # print(answer)
    messagebox.showinfo('Info title', "Here 's some information.")

def create_window():
    global extra_window
    extra_window = tk.Toplevel()
    extra_window.title('extra window')
    extra_window.geometry('300x400')
    ttk.Label(extra_window, text = 'A label').pack()
    ttk.Button(extra_window, text = 'A button').pack()
    ttk.Label(extra_window, text = 'Another label').pack(expand = True)

def close_window():
    extra_window.destroy()

window = tk.Tk()
window.geometry('600x400')
window.title('Multiple windows')

button1 =  ttk.Button(window, text = 'open main window', command = create_window)
button1.pack(expand = True)

button2 = ttk.Button(window, text = 'close main window', command = close_window)
button2.pack(expand = True)

button3 = ttk.Button(window, text = 'create yes no window', command = ask_yes_no)
button3.pack(expand = True)

window.bind('<Escape>', lambda event: window.quit())
window.mainloop()