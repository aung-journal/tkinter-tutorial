import tkinter as tk

window = tk.Tk()
window.geometry('600x480')
window.title('Canvas')

canvas = tk.Canvas(window, bg = 'white')
canvas.pack()

#width is just size of border
#tuple or parameter both are fine
canvas.create_rectangle(
    (50, 20, 100, 200),
    fill = 'red',
    width = 10,
    dash = (4, 2, 1, 1),
    outline = 'green')

canvas.create_oval(
    (0, 0, 20),
    fill = 'green')
canvas.create_line((0, 0, 100, 150))
#1 is just how tall, how wide

window.mainloop()