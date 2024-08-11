import tkinter as tk
from tkinter import ttk

class ListFrame(ttk.Frame):
    def __init__(self, parent, text_data, item_height):
        super().__init__(parent)
        self.pack(expand = True, fill ='both')

        #widget data
        self.text_data = text_data
        self.item_number = len(text_data)
        self.list_height = self.item_number * item_height

        #canvas
        self.canvas = tk.Canvas(self, background='white', scrollregion = (0, 0, self.winfo_width(), self.list_height))
        self.canvas.pack(expand=True, fill ='both')

        #display frame
        self.frame = ttk.Frame(self)

        for index, item in enumerate(self.text_data):
            self.create_item(index, item).pack(expand = True, fill = 'both', pady = 4, padx = 10)

        # self.canvas.create_window((0, 0),
        #                         window = self.frame,
        #                         anchor = 'nw',
        #                         width = self.winfo_width(),
        #                         height = self.list_height
        #                         )
        
        #events
        # self.canvas.bind_all('<Mousewheel>', lambda event: self.canvas.yview_scroll(-int(event.delta / 60), 'units'))
        # self.bind('<Configure>', self.update_size)

    def update_size(self, event):
        self.canvas.create_window(
            (0, 0),
            window = self.frame,
            anchor = 'nw',
            width = self.winfo_width(),
            height = self.list_height
        )
        
    def create_item(self, index, item):
        frame = ttk.Frame(self.frame)

        #grid layout
        frame.rowconfigure(0, weight = 1)
        frame.columnconfigure((0, 1, 2), weight = 1, uniform = 'a')

        #widgers
        ttk.Label(frame, text = f'#{index}').grid(row = 0, column = 0)
        ttk.Label(frame, text = f'#{item[0]}').grid(row = 0, column = 1)        
        ttk.Button(frame, text = f'#{item[1]}').grid(row = 0, column = 2, columnspan = 3, sticky = 'nsew')

        return frame        


window = tk.Tk()
window.geometry('500x400')
window.title('Scrolling')

#canvas
# canvas = tk.Canvas(window, background = 'white')
# canvas.create_window((20, 50), window = ttk.Label(canvas, text = 'A label'))
# canvas.pack(expand = True, fill ='both')

text_list = [('label', 'button'), ('label1', 'button1'), ('label2', 'button2'), ('label3', 'button3')]
list_frame = ListFrame(window, text_list, 100)

window.bind('<Escape>', lambda event: window.quit())
window.mainloop()