
# TK

import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

# messagebox.showinfo('title', 'msg') 
# messagebox.showwarning('title', 'msg')
# result=messagebox.askquestion('title', 'msg', icon='warning') 

root = tk.Tk()
root.title("T")
root.geometry("600x400") 




a = tk.StringVar()


def F1(txt='Default'):

    txt = a.get()
    print(txt)
    a.set('ee')

    T1.insert ('', tk.END, values = ('Micky Mouse', '100'))
    T1.insert ('', tk.END, values = ('Bugs Bunny', '81'))
    
    print(T1.selection())
    
    
    V1 = T1.focus()
    V2 = T1.item(V1)
    V3 = V2['values']
    print(V3)
    
    T1.delete(V1)



L1 = tk.Label(root,text='ali')
E1 = tk.Entry(root,textvariable=a)
B1 = tk.Button(root,text='ali',command=F1)

cols = ("H1", "H2")
T1 = ttk.Treeview(root, columns = cols, show="headings")
T1.heading ('H1', text='HT1')
T1.heading ('H2', text="HT2")

T1.insert ('', tk.END, values = ('Micky Mouse', '100'))
T1.insert ('', tk.END, values = ('Bugs Bunny', '81'))
# T1.bind('<<TreeviewSelect>>', F1)




L1.pack()
E1.pack()
B1.pack()
T1.pack()








F1 = tk.Frame(root, bg='pink')
L2 = tk.Label(F1,text='ali')
E2 = tk.Entry(F1,textvariable=a)
B2 = tk.Button(F1,text='ali',command=F1)

F1.pack()
L2.pack()
E2.pack()
B2.pack()

# L1.pack() 
# L1.grid(row=0,column=0,columnspan=1)
# L1.place(x=10,y=50)



root.mainloop()
