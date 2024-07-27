import tkinter as tk
from tkinter import ttk

def button_func():
    print('a basic button')
    print(radio_var.get())

window = tk.Tk()
window.title('buttons')
window.geometry('600x400')

#button
button_string = tk.StringVar(value = 'A simple button with string var')
# button = ttk.Button(window, text = 'A simple button', command = button_func)
button = ttk.Button(window, text = 'A simple button', command = lambda: button_func, textvariable = button_string)
button.pack()

# checkbutton
check_var = tk.IntVar()
#not variable because this doesn't set the text of the checkbox, it stores the state with 0 being close and 1 being open
check = ttk.Checkbutton(
    window,
    text = 'A simple checkbox',
    command = lambda: print(check_var.get()),
    variable= check_var,
    onvalue = 10,
    offvalue= 5)
#state is now open is 10, off is 5
check.pack()

check2 = ttk.Checkbutton(
    window,
    text = 'Checkbox 2',
    command = lambda: print('test')
)
check2.pack()

#radio buttons
#the radio button will automatically tick all radio buttons with the same value of it and default value is 0. so value has to be changed(or different) to fix that issue.
radio_var = tk.StringVar()
radio1 = ttk.Radiobutton(window,
                        text = 'Radiobutton 1',
                        value = 'radio 1',
                        variable = radio_var,
                        command = lambda: print(radio_var.get()))
radio1.pack()
radio2 = ttk.Radiobutton(window, text = 'Radiobutton 2', value = 2, variable = radio_var)
radio2.pack()

#exercise
#radio button
def exercise_radio_func():
    print(exercise_check_var.get())
    exercise_check_var.set(False)

exercise_radio_var = tk.StringVar()
exercise_radio1 = ttk.Radiobutton(
    window,
    text = 'Exercise radio button 1',
    value = 'A',
    variable = exercise_radio_var,
    command = exercise_radio_func())
)
exercise_radio1.pack()

exercise_radio2 = ttk.Radiobutton(
    window,
    text = 'Exercise radio button 2',
    value = 'B',
    variable = exercise_radio_var,
    command = exercise_radio_func())
)
exercise_radio2.pack()

#check button
exercise_check_var = tk.BooleanVar()
exercise_check = tk.Checkbutton(
    window,
    text = 'Exercise checkbutton',
    variable = exercise_check_var,
    command = lambda: print(exercise_radio_var.get())
)
exercise_check.pack()

window.mainloop()