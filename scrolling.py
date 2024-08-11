import tkinter as tk
from tkinter import ttk

from random import randint, choice

window = tk.Tk()
window.geometry('600x400')
window.title('Scrolling')

#canvas
#canvas is larger than window, so scrolling
# canvas = tk.Canvas(window, bg = 'white', scrollregion=(0, 0, 2000, 5000))
# canvas.create_line(0, 0, 2000, 5000, fill = 'green', width = 10)

# for i in range(100):
#     l = randint(0, 2000)
#     t = randint(0, 5000)
#     r = l + randint(10, 500)
#     b = t + randint(10, 500)
#     color = choice(('red', 'green', 'blue', 'yellow', 'orange'))
#     canvas.create_rectangle(
#         (l, t, r, b),
#         fill = color
#     )
# canvas.pack(expand = True, fill = 'both')

# #mousewheel scrolling
# canvas.bind('<MouseWheel>', lambda event: canvas.yview_scroll(int(event.delta / 60), 'units'))#units is always default don't change
# #tkinter always want integer for scrolling unit

# #scrollbar
# scrollbar = ttk.Scrollbar(window, orient = 'vertical', command = canvas.yview)#this will make scrollilng possible
# canvas.configure(yscrollcommand= scrollbar.set)#this is making scrollbar to scroll
# scrollbar.place(relx = 1, rely = 0, relheight = 1, anchor = 'ne')#this is basically what you are going to use all the timefor scrollbar

# #exercise(horizontal scrollbar)
# scrollbar1 = ttk.Scrollbar(window, orient = 'horizontal', command = canvas.xview)
# canvas.configure(xscrollcommand=scrollbar1.set)
# scrollbar1.place(relx = 0, rely = 1, relwidth = 1, anchor = 'sw')

# #bind event
# canvas.bind('<Control MouseWheel>', lambda event: canvas.xview_scroll(int(event.delta / 60), 'units'))

#Text
# text = tk.Text(window)

# for i in range(1, 200):
#     text.insert(f'{i}.0', f'text: {i} \n')

# text.pack(expand = True, fill = 'both')

# scrollbar_text = ttk.Scrollbar(window, orient = 'vertical', command = text.yview)#this will make scrollilng possible
# text.configure(yscrollcommand= scrollbar_text.set)#this is making scrollbar to scroll
# scrollbar_text.place(relx = 1, rely = 0, relheight = 1, anchor = 'ne')#this is basically what you are going to use all the timefor scrollbar

#Treeview
first_names = ['Bob', 'Maria', 'Alex', 'James', 'Susan', 'Henry', 'Lisa', 'Anna', 'Lisa']
last_names = ['Smith', 'Brown', 'wilson', 'Thomson', 'Cook', 'Taylor', 'Walker', 'Clark']

# treeview
table = ttk.Treeview(window, columns = (1, 2), show = 'headings')
table.heading(1, text = 'First name')
table.heading(2, text = 'Surname')

for i in range(100):
    table.insert(parent = '', index = tk.END, values = (choice(first_names), choice(last_names)))
table.pack(expand = True, fill = 'both')

scrollbar_table = ttk.Scrollbar(window, orient = 'vertical', command = table.yview)#this will make scrollilng possible
table.configure(yscrollcommand= scrollbar_table.set)#this is making scrollbar to scroll
scrollbar_table.place(relx = 1, rely = 0, relheight = 1, anchor = 'ne')#this is basically what you are going to use all the timefor scrollbar

window.bind('<Escape>', lambda event: window.quit())
window.mainloop()