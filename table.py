import tkinter as tk
from tkinter import ttk
from random import choice

window = tk.Tk()
window.geometry('600x400')
window.title('Tables')

first_names = ['Bob', 'Maria', 'Alex', 'James', 'Susan', 'Henry', 'Lisa', 'Anna', 'Lisa']
last_names = ['Smith', 'Brown', 'wilson', 'Thomson', 'Cook', 'Taylor', 'Walker', 'Clark']

# treeview
table = ttk.Treeview(window, columns = ('first', 'last', 'email'), show = 'headings')
table.heading('first', text = 'First name')
table.heading('last', text = 'Surname')
table.heading('email', text = 'Email')

table.pack(fill = 'both', expand = True)#this is going to expand entire thing

# table.insert(parent = '', index = 0, values = ('John', 'Doe', 'JohnDoe@email.com'))#this will create one entry

for i in range(100):
    first = choice(first_names)
    last = choice(last_names)
    email = first + last + '@email.com'
    data = (first, last, email)
    table.insert(parent = '', index = 0, values = data)#index here means insert the row in the 0th row, so the last entry will be on top
    #so this will be just like stack(FIFO)
    #what is index: 

table.insert(parent = '', index = tk.END, values = ('XXXXX', 'YYYYY', 'ZZZZZ')) #this will insert in the last row

#events

def item_select(_):
    #print(table.selection())
    #you are just going 
    for i in table.selection():
        print(table.item(i)['values'])
        print()
    #table.item(table.selection())

def delete_items(_):
    print('delete')
    for i in table.selection():
        table.delete(i)

table.bind('<<TreeviewSelect>>', item_select)#everything we are selecting an item in the table
table.bind('<Delete>', delete_items)
#items


window.mainloop()