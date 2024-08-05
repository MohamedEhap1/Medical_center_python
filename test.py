import tkinter
from tkinter import ttk

root = tkinter.Tk()
root.configure(background='black')
# style configuration
style = ttk.Style(root)
style.configure('TLabel', background='black', foreground='white')
style.configure('TFrame', background='black')

frame = ttk.Frame(root)
frame.grid(column=0, row=0)

ttk.Button(frame, text="Open file", command=None).grid(column=0, row=1)
lab = ttk.Label(frame, text="test test test test test test ")
lab.grid(column=0, row=2)


root.mainloop()