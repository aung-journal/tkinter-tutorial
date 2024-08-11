import tkinter as tk
from tkinter import ttk

window = tk.Tk()
window.geometry('600x400')
window.title('Canvas')

canvas = tk.Canvas(window, bg = 'white')
canvas.pack()

# canvas.create_rectangle(
#     (50, 20, 100, 200),
#     fill = 'red',
#     width = 10,
#     dash = (4, 2, 1, 1),
#     outline = 'green'
# )

# canvas.create_oval(
#     (200, 0, 300, 100),
#     fill = 'green'
# )

# canvas.create_arc(
#     (200, 0, 300, 100),
#     fill = 'red',
#     start = 45,
#     extent = 180,
#     style = tk.CHORD,
#     outline = 'yellow',
#     width = 10)#this is start point
# #start frorm 45 degree and add 180 degrees

# canvas.create_line((0, 0, 100, 150), fill = 'blue')
#canvas.create_polygon((0, 0, 100, 200, 300, 50, 150, - 50), fill = 'gray')#(x1, y1, x2, y2, x3, y3)#this will be a triangle

#canvas.create_text((100, 20), text = 'This is some text.', fill = 'green', width = 10)

# canvas.create_window((50, 100), window = ttk.Label(window, text = 'This is a text in the canvas.'))

#Exercise
#use event binding to create a basic paint app

#my solution

# def on_left_click(event):
#     canvas.create_line((event.x, event.y, event.x + 1, event.y + 1))

# canvas.bind('<B1-Motion>', on_left_click)

#the solution
def draw_on_canvas(event):
    x = event.x
    y = event.y
    canvas.create_oval(x - brush_size / 2, y - brush_size / 2, x + brush_size / 2, y + brush_size / 2, fill='black')

def brush_size_adjust(event):
    global brush_size
    if event.delta > 0:
        brush_size += 4
    else:
        brush_size -= 4

    #because negative will also have the same effect as positive brush size
    brush_size = max(0, min(brush_size, 50))

brush_size = 4
canvas.bind('<Motion>', draw_on_canvas)
canvas.bind('<Button-1>', brush_size_adjust)

window.mainloop()