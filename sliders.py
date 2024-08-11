import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext

window = tk.Tk()
window.title('Sliders')

#slider
scale_float = tk.DoubleVar(value = 15)
scale = ttk.Scale(window,
                command = lambda value: progress.stop(),
                from_ = 0,
                to = 25,
                length = 300,
                orient = 'vertical',
                variable =  scale_float)#command in ttk.scale needs a function with 1 parameter
scale.pack()

#progress bar
progress = ttk.Progressbar(
    window,
    variable = scale_float,
    maximum = 25,#this is like to in slidebar
    orient='horizontal',
    mode = 'indeterminate',
    length = 400)#this makes it like slidebar else this is like progress bar
progress.pack()

progress.start()#this makes it start by itself
#progress.stop()#stopping the progressbar
#if you move it, it is going 

#Scrolledtext
# scrolled_text = scrolledtext.ScrolledText(window, width = 100, height= 5)
# scrolled_text.pack()

#exercise
exercise_scale_int = tk.IntVar()
exercise_progress = ttk.Progressbar(
    window,
    variable = exercise_scale_int,
    orient = 'vertical',
)
exercise_progress.pack()
exercise_progress.start()

label = ttk.Label(window, textvariable= exercise_scale_int)
label.pack()

exercise_scale = ttk.Scale(window,
                variable = exercise_scale_int,
                from_ = 0,
                to = 100,)
exercise_scale.pack()

window.mainloop()