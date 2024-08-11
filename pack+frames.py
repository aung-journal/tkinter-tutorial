import tkinter as tk
from tkinter import ttk

window = tk.Tk()
window.title('Pack parenting')
window.geometry('400x600')

#widgets
#Top frame
top_frame = ttk.Frame(window)
label1 = ttk.Label(top_frame, text = 'Label1', background = 'red')
label2 = ttk.Label(top_frame, text = 'Label2', background='blue')

#middle widget
label3 = ttk.Label(window, text = 'Label3', background='green')

#bottom frame
bottom_frame = ttk.Frame(window)
label4 = ttk.Label(bottom_frame, text = 'Label4', background='orange')
button = ttk.Button(bottom_frame, text = 'Button')
button2 = ttk.Button(bottom_frame, text = 'Another Button')
#top layout
label1.pack(side = 'top', fill = 'both', expand = True)
label2.pack(side = 'top', fill = 'both', expand = True)
top_frame.pack(fill = 'both', expand = True)

#middle layout
label3.pack(expand = True)

#bottom layout
button.pack(side = 'left', expand = True, fill = 'both')
label4.pack(side = 'left', expand = True, fill = 'both')
button2.pack(side = 'left', expand = True, fill = 'both')
bottom_frame.pack(expand = True, fill = 'both', padx = 20, pady = 20)

#exercise
exercise_frame = ttk.Frame(bottom_frame)
button3 = ttk.Button(bottom_frame, text = 'Button3')
button4 = ttk.Button(bottom_frame, text = 'Button4')
button5 = ttk.Button(bottom_frame, text = 'Button5')

#exercise layout
button3.pack(expand = True, fill = 'both')
button4.pack(expand = True, fill = 'both')
button5.pack(expand = True, fill = 'both')
exercise_frame.pack(side = 'left', expand = True)

window.bind('<Escape>', lambda event: window.quit())
window.mainloop()