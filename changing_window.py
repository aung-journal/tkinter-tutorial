import tkinter as tk
from tkinter import ttk

window = tk.Tk()
window.title('More on the window')
#window.geometry('600x400')#left+top(x, y)
# window.iconbitmap('')
#changing the icon of the window

#exercise:
#start window in the middle of the screen

window_width = 1024
window_height = 576
display_width = window.winfo_screenwidth()
display_height = window.winfo_screenheight()

left = (display_width - window_width) / 2
top = (display_height - window_height) / 2

window.geometry(f"{window_width}x{window_height}+{int(left)}+{int(top)}")
#window attribute
window.minsize(200, 100)#the minimum size of window
window.maxsize(800, 700)#the maximum size of window
window.resizable(True, False)#can only scale horizontally now

#screen attribute(window sizes)
print(window.winfo_screenwidth())
print(window.winfo_screenheight())

#window attribute
window.attributes('-alpha', 0.1)#for transparency
window.attributes('-topmost', True)#making the screen on top of everything

#security event
window.bind('<Escape>', lambda event: window.quit())

#some atttributets can make window impossible to quit

#window.attributes('-disable', True)#not working for now
#window.attributes('-fullscreen', True)

#title bar
#window.overrideredirect(True)#you can't resize in this position and it make window title bar gone
grip = ttk.Sizegrip(window)
grip.pack()

grip.place(relx = 1.0, rely = 1.0, anchor='se')#this makes the sizing of window flexible

window.mainloop()