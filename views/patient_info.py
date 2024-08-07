from tkinter import *
from tkinter.ttk import *
from PIL import Image, ImageTk
from tkinter import messagebox
import sqlite3
import os
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
        os.system("python views/dashboard.py")
        
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
# Delete button
delete_button = Button(buttons_frame , text="Delete" , cursor="hand2" , style="TButton",command=delete_item)
# Edit button
def edit_Frame():
        # Create the edit confirmation window
        edit_window = Toplevel(root)
        edit_window.title("Edit Confirmation")
        edit_window.configure(background='#eaf6f8')     
        # Get the selected item from the table
        selected_item = table.selection()
        if not selected_item:
                messagebox.showwarning("Selection Error", "Please select a patient to Edit.")
                edit_window.destroy()
                return

        # Populate the form with the selected patient's data
        selected_patient_id = table.item(selected_item[0])['values'][0]
        cur.execute('SELECT * FROM patient WHERE id = ?', (selected_patient_id,))
        patient_data = cur.fetchone()

        # Name
        Label(edit_window, text="Name", background='#eaf6f8', font=("Tahoma" , 12)).pack(pady=2)
        entry_name = Entry(edit_window)
        entry_name.insert(0, patient_data[1])
        entry_name.pack(pady=5)

        # Age
        Label(edit_window, text="Age", background='#eaf6f8', font=("Tahoma" , 12)).pack(pady=2)
        entry_age = Entry(edit_window)
        entry_age.insert(0, str(patient_data[2]))
        entry_age.pack(pady=5)

        # Phone Number
        Label(edit_window, text="Phone Number", background='#eaf6f8', font=("Tahoma" , 12)).pack(pady=2)
        entry_phone = Entry(edit_window)
        entry_phone.insert(0, patient_data[3])
        entry_phone.pack(pady=5)

        # Blood type combo box
        combo2_stat_var = StringVar()
        combo2_stat_var.set(patient_data[4])
        combo2_stat = Combobox(edit_window, values=('A ', 'B', 'O','A+','C'), textvariable=combo2_stat_var, state='readonly')
        combo2_stat.pack(pady=5)
        #Gender
        gender=patient_data[5]
        # Patient status combo box
        combo_stat_var = StringVar()
        combo_stat_var.set(patient_data[6])
        combo_stat = Combobox(edit_window, values=('White', 'Red', 'Blue','purple','yellow'), textvariable=combo_stat_var, state='readonly')
        combo_stat.pack(pady=5)
        # Name doctor combo box
        combo3_stat_var = StringVar()
        combo3_stat_var.set(patient_data[7])
        combo3_stat = Combobox(edit_window, values=('Ahmed', 'Ali', 'mohamed'), textvariable=combo3_stat_var, state='readonly')
        combo3_stat.pack(pady=5)
        # Date
        date=patient_data[8]


        frame = Frame(edit_window)
        frame.pack(pady=10)

        cancel_button = Button(frame, text="Cancel", command=edit_window.destroy)
        cancel_button.pack(side='left', padx=5)

        def confirm_edit():
                try:
                        # Get the updated values from the form
                        new_name = entry_name.get()
                        new_age = int(entry_age.get())
                        new_phone = entry_phone.get()
                        new_status = combo_stat_var.get()
                        new_blood_type = combo2_stat_var.get()
                        new_gender=gender
                        new_date=date
                        new_doc_name=combo3_stat_var.get()

                        # Update the patient's information in the database
                        cur.execute('UPDATE patient SET name = ?, age = ?, phone = ?, blood_type = ?,gender = ?, status = ? ,nameDoc =? ,datee = ? WHERE id = ?', 
                                (new_name, new_age, new_phone, new_blood_type,new_gender ,new_status,new_doc_name,new_date ,selected_patient_id))
                        conn.commit()

                        # Update the table with the new information
                        table.item(selected_item[0], values=(selected_patient_id,new_name, new_age, new_phone, new_blood_type,new_gender ,new_status,new_doc_name,new_date ))
                        messagebox.showinfo('Notification', 'The patient was edited successfully')
                        edit_window.destroy()
                except Exception as e:
                        messagebox.showwarning("Error", str(e))

        confirm_button = Button(frame, text="Edit", command=confirm_edit)
        confirm_button.pack(side='left', padx=5)

edit_button = Button(buttons_frame , text="Edit" , cursor="hand2" , style="TButton",command=edit_Frame)
# Show Buttons
delete_button.pack(side=RIGHT, padx=5)
edit_button.pack(side=LEFT, padx=5)

# Show Frame
buttons_frame.pack(pady=5)

root.mainloop()
conn.close()