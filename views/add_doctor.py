from ctypes.wintypes import RGB
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from tkinter.ttk import *
import tkinter as tk
from PIL import Image

def add_row():
    value1 = txt1.get()
    value2 = txt2.get()
    value3 = txt3.get()
    value4 = txt4.get()
    tree.insert("", "end", values=(value1, value2,value3,value4))
    txt1.delete(0, tk.END)
    txt2.delete(0, tk.END)
    txt3.delete(0, tk.END) 
    txt4.delete(0, tk.END)



docters = [(1, 'Ali Ahmed', 'Internal Medicine'),
            (2, 'Mona Hossam', 'Surgery '),
            (3, 'Ramy Yasser', 'Pediatrics '),
            (4, 'Kareem Mohamed', 'Psychiatry '),
            (5, 'Mai Alaa', 'Cardiology '),
            (6, 'Tamer Hassan', 'Radiology '),
            (7, 'Moustafa Mahmoud', 'Neurology '),
            (8, 'Moustafa Ahmed', 'Pediatrics '),
            (9, 'Moustafa Mohamed', 'Pediatrics '),                                       
            (10, 'Moustafa Ibrahim', 'Radiology ')
]

win=Tk()
win.iconbitmap("images/icon.jpg")
win.geometry("5000x1200")
win.title('Add doctor')
screen_width = win.winfo_screenwidth()
screen_height = win.winfo_screenheight()
# حساب موقع الإطار (افتراضًا عرض وارتفاع الإطار 300x200)
x = (screen_width/2) - 150
y = (screen_height/2) - 100
frame = tk.Frame(win, width=600, height=400)
frame.place(x=x, y=y)






cols=['id','name','departement','note']
win.geometry("650x500")
basefont = ('Thoma', 12)

lb1=Label(win,text='Doctor Name',font=basefont,background='#37B7C3',foreground='#EBF4F6')
txt1=Entry(win,font=basefont,foreground='#071952')
lb2=Label(win,text='Departement',font=basefont,background='#37B7C3',foreground='#EBF4F6')
txt2=Entry(win,font=basefont,foreground='#071952')
lb3=Label(win,text='Note',font=basefont,background='#37B7C3',foreground='#EBF4F6')
txt3=Entry(win,font=basefont,foreground='#071952')
lb4=Label(win,text='Num_Id',font=basefont,background='#37B7C3',foreground='#EBF4F6')
txt4=Entry(win,font=basefont,foreground='#071952')


tree=Treeview(win,columns=cols,show='headings')
tree.column('id',width=30,anchor='center')
tree.heading('id',text='Num_Id')
tree.heading('name',text='full_name')
tree.heading('departement',text='depertment')
tree.heading('note',text='note')


btn1=Button(win,text='ADD',command=add_row)
for doctor in docters:
    tree.insert('','end',values=doctor,iid=doctor[0])

style = ttk.Style()
style.theme_use('default')
style.configure("Treeview",
                background="#37B7C3",
                foreground="#EBF4F6",
                rowheight=25,
                fieldbackground="#d9d9d9")
style.map('Treeview',
            background=[('selected', '#37B7C3')],
            foreground=[('selected', 'white')])


lb4.place(x=0,y=10)
txt4.place(x=100,y=10)
lb1.place(x=0,y=40)
txt1.place(x=100,y=40)
lb2.place(x=0,y=70)
txt2.place(x=100,y=70)
lb3.place(x=0,y=100)
txt3.place(x=100,y=100)
tree.place(x=10,y=150)
btn1.place(x=260,y=420)
win.mainloop()