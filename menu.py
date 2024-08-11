import tkinter as tk
from tkinter import ttk

# window
window =  tk.Tk()
window.geometry('600x400')
window.title('Menu')

#menu
menu = tk.Menu(window)

# sub menu
file_menu = tk.Menu(menu, tearoff = False)#tear off means you can tear away the menu as a new window
file_menu.add_command(label = 'New', command = lambda : print('New file'))
file_menu.add_command(label = 'Open', command = lambda : print('Openfile'))
file_menu.add_separator()
menu.add_cascade(label = 'File', menu = file_menu)#two arguments

#another sub menu
help_menu = tk.Menu(menu, tearoff = False)
help_menu.add_command(label = 'Help entry', command = lambda : print(help_check_string.get()))

help_check_string = tk.StringVar()
help_menu.add_checkbutton(label = 'check', onvalue='on', offvalue='off', variable=help_check_string)

menu.add_cascade(label = 'Help', menu = help_menu)

#add another menu to the main menu
exercise_menu = tk.Menu(menu, tearoff = False)
exercise_menu.add_command(label = 'Exercise 1', command = lambda: print('exercise 1'))
menu.add_cascade(label = 'Exercise', menu = exercise_menu)

exercise_sub_menu = tk.Menu(menu, tearoff = False)
exercise_sub_menu.add_command(label = 'Exercise 2', command = lambda: print('exercise 2'))
exercise_menu.add_cascade(label = 'More', menu = exercise_sub_menu)

window.configure(menu = menu)

#menu button
menu_button = ttk.Menubutton(window, text = 'Menu Button')
menu_button.pack()

button_sub_menu = tk.Menu(menu_button, tearoff=False)
button_sub_menu.add_command(label = 'entry 1', command= lambda: print('test 1'))
button_sub_menu.add_checkbutton(label='check 1')
#menu_button.configure(menu = button_sub_menu)#configure the menu to give it
menu_button['menu'] = button_sub_menu#this is the same

window.mainloop()