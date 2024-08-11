import tkinter as tk
from tkinter import ttk

class App(tk.Tk):
    def __init__(self, start_size):
        super().__init__()
        self.title('Responsive layout')
        self.geometry(f'{start_size[0]}x{start_size[1]}')

        self.frame = ttk.Frame(self)
        self.frame.pack(expand=True, fill='both')

        self.size_notifier = SizeNotifier(self, {
            1200: self.create_large_layout,
            600: self.create_medium_layout,
            300: self.create_small_layout
            })

        self.bind('<Escape>', lambda event: self.quit())
        self.mainloop()

    def create_small_layout(self):
        self.frame.pack_forget()
        #this makes the previous frame to be gone
        self.frame = ttk.Frame(self)
        self.frame.pack(expand=True, fill='both')

        ttk.Label(self.frame, text='Label1', background='red').pack(expand=True, fill='both', padx=10, pady=5)
        ttk.Label(self.frame, text='Label2', background='blue').pack(expand=True, fill='both', padx=10, pady=5)
        ttk.Label(self.frame, text='Label3', background='green').pack(expand=True, fill='both', padx=10, pady=5)
        ttk.Label(self.frame, text='Label4', background='orange').pack(expand=True, fill='both', padx=10, pady=5)

    def create_medium_layout(self):
        self.frame.pack_forget()
        self.frame = ttk.Frame(self)
        self.frame.pack(expand=True, fill='both')

        self.frame.columnconfigure((0, 1), weight=1, uniform='a')
        self.frame.rowconfigure((0, 1), weight=1, uniform='a')

        ttk.Label(self.frame, text='Label1', background='red').grid(row=0, column=0, sticky='nsew')
        ttk.Label(self.frame, text='Label2', background='blue').grid(row=0, column=1, sticky='nsew')
        ttk.Label(self.frame, text='Label3', background='green').grid(row=1, column=0, sticky='nsew')
        ttk.Label(self.frame, text='Label4', background='orange').grid(row=1, column=1, sticky='nsew')

    #exercise: create third layout, where all of the widgets are next to each other
    def create_large_layout(self):
        self.frame.pack_forget()
        self.frame = ttk.Frame(self)
        self.frame.pack(expand = True, fill = 'both')
        ttk.Label(self.frame, text='Label1', background='red').pack(side = 'left',expand=True, fill='both', padx=10, pady=5)
        ttk.Label(self.frame, text='Label2', background='blue').pack(side = 'left',expand=True, fill='both', padx=10, pady=5)
        ttk.Label(self.frame, text='Label3', background='green').pack(side = 'left',expand=True, fill='both', padx=10, pady=5)
        ttk.Label(self.frame, text='Label4', background='orange').pack(side = 'left',expand=True, fill='both', padx=10, pady=5)

class SizeNotifier:
    def __init__(self, window: tk.Tk, size_dict: dict):
        self.window = window
        self.size_dict = {key: value for key, value in sorted(size_dict.items())}
        self.current_min_size = None

        self.window.update()  # Ensure the window size is updated before setting min size

        min_height = self.window.winfo_height()
        min_width = min(self.size_dict.keys())
        self.window.minsize(min_width, min_height)

        self.window.bind('<Configure>', self.check_size)
        self.initial_layout()#set up the initial layout

    def initial_layout(self):
        w = self.window.winfo_width()
        for min_size in self.size_dict:
            if w >= min_size:
                self.size_dict[min_size]()

    def check_size(self, event):
        #don't do check_size configure for widgets such as label, etc. Only for self.window
        if event.widget == self.window:
            w = event.width
            checked_size = None

            for min_size in self.size_dict:
                if w >= min_size:
                    checked_size = min_size

            if checked_size != self.current_min_size:
                self.current_min_size = checked_size
                print(self.current_min_size)
                self.size_dict[self.current_min_size]()

app = App((400, 300))
