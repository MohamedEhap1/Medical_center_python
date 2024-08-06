from tkinter import *
from tkinter.ttk import *
from PIL import Image, ImageTk
from tkinter import messagebox
import sqlite3
root = Tk()
root.config(background="#EBF4F6") # frame background color
root.title("Patient Info")


#connect to the database
conn=sqlite3.connect('Medical_Center.db') 
# get a cursur 
cur=conn.cursor()
# get the data of all patients
cur.execute('SELECT * From patient')
# fetsh the result of the query
results=cur.fetchall()

#Styling properties
style = Style()
style.theme_use("clam") # To make Style modern 

#Buttons Styling
style.configure("TButton", 
                background = "#071952",
                foreground = "white",
                font = ("Tahoma" , 13),
                borderwidth = 0,
                ) 
style.map("TButton", # Style On Hovering Buttons
        background=[('active', '#088395')],
        foreground=[('active', 'white')])



# Table and Scroll bar Frame
table_frame = Frame(root)
#Table Columns
cols = ("id" , "name"  , "age" , 
        "phone","blood_type" ,"gender" , "status","nameDoc","datee")

#Create Table
table = Treeview(table_frame , columns=cols , show="headings" ,
                style="Treeview")


# back button
def backBtn():
        root.destroy()
        import dashboard
back_img = Image.open("images/BackBtn.png")
back_tk = ImageTk.PhotoImage(back_img)
back_button = Button(root, image=back_tk,command=backBtn)
back_button.pack(anchor="w" , pady=10 , padx=5)



# Search Frame
search_frame = Frame(root)
search_frame.pack(anchor="center")

search_entry = Entry(search_frame , style="TEntry",) # create search input
def search_btn():
        try:
                cur.execute('SELECT * FROM patient WHERE lower(name) LIKE ?', (f'%{search_entry.get().lower()}%',))
                conn.commit()
                for row in table.get_children():
                        table.delete(row)
        
                results=cur.fetchall()
                # Iterate over the rows and display the results.
                for row in results:
                        table.insert("", "end", values=row)
        except :
                messagebox.showwarning("Entry Error", "Please Enter a Name of patient to search.")
search_button = Button(search_frame , cursor="hand2" , text="Search Name" ,
                        padding=3,command=search_btn) # create search button

search_entry.pack(side="left" , padx = "5" , pady=10)
search_button.pack(side="right" , padx="5" , pady=10)

# Entry Styling
style.configure("TEntry",
                padding = 5,
                fieldbackground = "white",
                font = ("Tahoma" , 12),
                bordercolor = "#071952"
                )



table_frame.pack()


#Columns Headings
table.heading("id" , text="Id" , anchor="center")
table.heading("name" , text="Name" , anchor="w")
table.heading("age" , text="Age" , anchor="center")
table.heading("phone" , text="Phone Number" , anchor="w")
table.heading("blood_type" , text="Blood Type" , anchor="center")
table.heading("gender" , text="Gender" , anchor="w")
table.heading("status" , text="Status" , anchor="w")
table.heading("nameDoc" , text="Name_Doctor" , anchor="w")
table.heading("datee" , text="Date" , anchor="w")

# Define the column widths and other properties
table.column("id", width=50, stretch=NO , anchor="center")
table.column("name", width=200, stretch=NO)
table.column("age", width=70, stretch=NO , anchor="center")
table.column("phone", width=150, stretch=NO )
table.column("blood_type", width=200, stretch=NO , anchor="center")
table.column("gender", width=150, stretch=NO )
table.column("status", width=150, stretch=NO )
table.column("nameDoc", width=150, stretch=NO )
table.column("datee", width=150, stretch=NO )

# Table Styling
style.configure("Treeview", # Rows and Table Styling
                background="#35adb8", 
                foreground="white", 
                rowheight=28, 
                fieldbackground="#35adb8", 
                font=("Tahoma", 13))

style.configure("Treeview.Heading", # Headings Styling
                background="#071952", 
                foreground="white", 
                font=("Tahoma", 12, "bold"),
                borderwidth = 0,
                )

style.map("Treeview", # Selecting rows Styling
        background=[('selected', '#ffc300')], 
        foreground=[('selected', 'black')])

style.map("Treeview.Heading",  # Selecting Headings Styling
        background=[('selected', '#071952')], 
        foreground=[('selected', 'white')])


# Create vertical scrollbar
scroll = Scrollbar(table_frame, orient=VERTICAL, command=table.yview ,
                style="Vertical.TScrollbar")
# Display Scroll Bar
table.configure(yscrollcommand=scroll.set) # 
# Scroll bar Styling
style.configure("Vertical.TScrollbar",
                gripcount=0, # number of '-' in the scroll bar
                background="lightgray", # color of scroll bar and arrows background
                troughcolor="darkgray", # color of background
                arrowcolor="black",
                width=16)

# Iterate over the rows and display the results.
for row in results:
        table.insert("", "end", values=row)

scroll.pack(side=RIGHT, fill=Y)
# Display Table
table.pack()

# Frame for delete and edit
buttons_frame = Frame(root) 

# Buttons Frame Styling
style.configure("TFrame",
                background = "#EBF4F6")
# delete methode
def delete_item():
        try:
                selected_item = table.selection()[0]
                selected_patient_id = table.item(selected_item)['values'][0]

                cur.execute('DELETE FROM patient WHERE id=?', (selected_patient_id,))
                conn.commit()
                

                messagebox.showinfo('Notification', 'The patient was deleted successfully')
                table.delete(selected_item)
        except IndexError:
                messagebox.showwarning("Selection Error", "Please select a patient to delete.")
# Delete and Edit Buttons
delete_button = Button(buttons_frame , text="Delete" , cursor="hand2" , style="TButton",command=delete_item)
edit_button = Button(buttons_frame , text="Edit" , cursor="hand2" , style="TButton")

# Show Buttons
delete_button.pack(side=RIGHT, padx=5)
edit_button.pack(side=LEFT, padx=5)

# Show Frame
buttons_frame.pack(pady=5)

root.mainloop()
conn.close()