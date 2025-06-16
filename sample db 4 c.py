
# TK

import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

# messagebox.showinfo('title', 'msg') 
# messagebox.showwarning('title', 'msg')
# result=messagebox.askquestion('title', 'msg', icon='warning') 

root = tk.Tk()
root.title("T")
# root.geometry("600x400") 
# root.destroy()



v1 = tk.StringVar()
v2 = tk.StringVar()
v3 = tk.StringVar()
v4 = tk.StringVar()


import sqlite3

conn = sqlite3.connect('bookdb.db')
cursor = conn.cursor() 
    

cursor.execute("create table if not exists bookT (id integer primary key autoincrement, V1 text, V2 text, V3 text, V4 text)")
# cursor.executemany("Query...", List_of_Tuples)

# list_of_data = cursor.fetchall()
conn.commit()

cursor.close()
conn.close()
        
'''
CURD:

create table if not exists Table_Name (id integer primary key autoincrement, V1 text, V2 integer)
insert into Table_Name (V1 , V2) values(?,?)
select * from Table_Name where V1 like "%{V1.get()}%" 
delete from Table_Name where id={V1}
update Table_Name set V1="{V1}" , V2={V2}, where id={V_id}
'''



def F1(txt='Default'):
    pass
    conn = sqlite3.connect('bookdb.db')
    cursor = conn.cursor() 
        

    cursor.execute("select * from bookT")
    # cursor.executemany("Query...", List_of_Tuples)

    list_of_data = cursor.fetchall()
    T1.delete(*T1.get_children())
    for x in list_of_data:
        T1.insert ('', tk.END, values = x)
    print(list_of_data)
    conn.commit()

    cursor.close()
    conn.close()


def F2(txt='Default'):
    pass
    conn = sqlite3.connect('bookdb.db')
    cursor = conn.cursor() 
        
    
    cursor.execute(f'select * from bookT where V1 LIKE  "%{v1.get()}%" and V2 LIKE  "%{v2.get()}%"')
    # cursor.executemany("Query...", List_of_Tuples)
    
    list_of_data = cursor.fetchall()
    print(list_of_data)
    T1.delete(*T1.get_children())
    for x in list_of_data:
        T1.insert ('', tk.END, values = x)
    conn.commit()
    
    cursor.close()
    conn.close()
            
    '''
    CURD:
    
    create table if not exists Table_Name (id integer primary key autoincrement, V1 text, V2 integer)
    insert into Table_Name (V1 , V2) values(?,?)
    c
    delete from Table_Name where id={V1}
    update Table_Name set V1="{V1}" , V2={V2}, where id={V_id}
    '''



def F3(txt='Default'):
    conn = sqlite3.connect('bookdb.db')
    cursor = conn.cursor() 
        

    cursor.execute("insert into bookT (V1, V2, V3, V4) values(?,?,?,?)",(v1.get(),v2.get(),v3.get(),v4.get()))
    # cursor.executemany("Query...", List_of_Tuples)

    # list_of_data = cursor.fetchall()
    conn.commit()

    cursor.close()
    conn.close()
            
    pass
    F1()



def F4(txt='Default'):
    pass
    conn = sqlite3.connect('bookdb.db')
    cursor = conn.cursor() 
    my_id = T1.item(T1.focus())['values'][0]
    print(my_id)
    
    

    cursor.execute(f"delete from bookT where id={my_id}")
    # cursor.executemany("Query...", List_of_Tuples)

    # list_of_data = cursor.fetchall()
    # T1.delete(*T1.get_children())
    # for x in list_of_data:
    #     T1.insert ('', tk.END, values = x)
    # print(list_of_data)
    conn.commit()

    cursor.close()
    conn.close()
    F1()

def F5(txt='Default'):
    pass
    root.destroy()
    # txt = a.get()
#     print(txt)
#     a.set('ee')

#     T1.insert ('', tk.END, values = ('Micky Mouse', '100'))
#     T1.insert ('', tk.END, values = ('Bugs Bunny', '81'))
    
#     print(T1.selection())
    
    
#     V1 = T1.focus()
#     V2 = T1.item(V1)
#     V3 = V2['values']
#     print(V3)
    
#     T1.delete(V1)


#     T1.delete(*T1.get_children())


L1 = tk.Label(root,text='v1')
E1 = tk.Entry(root,textvariable=v1)


L2 = tk.Label(root,text='v2')
E2 = tk.Entry(root,textvariable=v2)


L3 = tk.Label(root,text='v3')
E3 = tk.Entry(root,textvariable=v3)



L4 = tk.Label(root,text='v4')
E4 = tk.Entry(root,textvariable=v4)



L1.grid(row=0,column=0)
E1.grid(row=0,column=1)


L2.grid(row=1,column=0)
E2.grid(row=1,column=1)


L3.grid(row=2,column=0)
E3.grid(row=2,column=1)


L4.grid(row=3,column=0)
E4.grid(row=3,column=1)



B1 = tk.Button(root,text='see',command=F1)
B2 = tk.Button(root,text='search',command=F2)
B3 = tk.Button(root,text='add',command=F3)
B4 = tk.Button(root,text='remove',command=F4)
B5 = tk.Button(root,text='close',command=F5)

B1.grid(row=4,column=0)
B2.grid(row=4,column=1)
B3.grid(row=4,column=2)
B4.grid(row=4,column=3)
B5.grid(row=4,column=4)





# B1 = tk.Button(root,text='ali',command=F1)

cols = ("ID","H1", "H2", "H3", "H4")
T1 = ttk.Treeview(root, columns = cols, show="headings")
T1.heading ('ID', text='ID')
T1.heading ('H1', text='HT1')
T1.heading ('H2', text="HT2")
T1.heading ('H3', text='HT3')
T1.heading ('H4', text="HT4")

# T1.insert ('', tk.END, values = ('Micky Mouse', '100'))
# T1.insert ('', tk.END, values = ('Bugs Bunny', '81'))
# T1.bind('<<TreeviewSelect>>', F1)

T1.grid(row=5,column=0,columnspan=5)


# L1.pack()
# E1.pack()
# B1.pack()
# T1.pack()








# F1 = tk.Frame(root, bg='pink')
# L2 = tk.Label(F1,text='ali')
# E2 = tk.Entry(F1,textvariable=a)
# B2 = tk.Button(F1,text='ali',command=F1)

# F1.pack()
# L2.pack()
# E2.pack()
# B2.pack()

# L1.pack() 
# L1.grid(row=0,column=0,columnspan=1)
# L1.place(x=10,y=50)



root.mainloop()
