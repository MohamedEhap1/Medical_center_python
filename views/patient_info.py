from tkinter import *
from tkinter.ttk import *

root = Tk()
root.config(background="#EBF4F6") # frame background color
root.title("Patient Info")

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




# Backward Button 
back_button = Button(root , text="<" , width=4,style="TButton",
                      cursor="hand2") #Pointer cursor
# Display Backward Button
back_button.pack(anchor="w" , pady=10 , padx=5)




# Table and Scroll bar Frame
table_frame = Frame(root)
table_frame.pack()

#Table Columns
cols = ("id" , "name" , "national_id" , "age" , "blood_type" , 
        "address" , "phone_number")

#Create Table
table = Treeview(table_frame , columns=cols , show="headings" ,
                  style="Treeview")

#Columns Headings
table.heading("id" , text="Id" , anchor="center")
table.heading("name" , text="Name" , anchor="w")
table.heading("national_id" , text="National Id" , anchor="w")
table.heading("age" , text="Age" , anchor="center")
table.heading("blood_type" , text="Blood Type" , anchor="center")
table.heading("address" , text="Address" , anchor="w")
table.heading("phone_number" , text="Phone Number" , anchor="w")

# Define the column widths and other properties
table.column("id", width=50, stretch=NO , anchor="center")
table.column("name", width=200, stretch=NO)
table.column("national_id", width=200, stretch=NO )
table.column("age", width=70, stretch=NO , anchor="center")
table.column("blood_type", width=200, stretch=NO , anchor="center")
table.column("address", width=200, stretch=NO )
table.column("phone_number", width=150, stretch=NO )

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
scroll.pack(side=RIGHT, fill=Y)
table.configure(yscrollcommand=scroll.set) # 
# Scroll bar Styling
style.configure("Vertical.TScrollbar",
                gripcount=0, # number of '-' in the scroll bar
                background="lightgray", # color of scroll bar and arrows background
                troughcolor="darkgray", # color of background
                arrowcolor="black",
                width=16)

# Data for expirment
data = [
    (1, "John Doe", "123456", 25, "A+", "123 Main St", "555-1234"),
    (2, "Jane Smith", "654321", 30, "B+", "456 Elm St", "555-5678"),
    (2, "Jane Smith", "654321", 30, "B+", "456 Elm St", "555-5678"),
    (2, "Jane Smith", "654321", 30, "B+", "456 Elm St", "555-5678"),
    (2, "Jane Smith", "654321", 30, "B+", "456 Elm St", "555-5678"),
    (2, "Jane Smith", "654321", 30, "B+", "456 Elm St", "555-5678"),
    (2, "Jane Smith", "654321", 30, "B+", "456 Elm St", "555-5678"),
    (2, "Jane Smith", "654321", 30, "B+", "456 Elm St", "555-5678"),
    (2, "Jane Smith", "654321", 30, "B+", "456 Elm St", "555-5678"),
    (2, "Jane Smith", "654321", 30, "B+", "456 Elm St", "555-5678"),
    (2, "Jane Smith", "654321", 30, "B+", "456 Elm St", "555-5678"),
    (2, "Jane Smith", "654321", 30, "B+", "456 Elm St", "555-5678"),
    (2, "Jane Smith", "654321", 30, "B+", "456 Elm St", "555-5678"),
    (2, "Jane Smith", "654321", 30, "B+", "456 Elm St", "555-5678"),
    (2, "Jane Smith", "654321", 30, "B+", "456 Elm St", "555-5678"),
    (2, "Jane Smith", "654321", 30, "B+", "456 Elm St", "555-5678"),
    (2, "Jane Smith", "654321", 30, "B+", "456 Elm St", "555-5678"),
    (2, "Jane Smith", "654321", 30, "B+", "456 Elm St", "555-5678"),
    (2, "Jane Smith", "654321", 30, "B+", "456 Elm St", "555-5678"),
    (2, "Jane Smith", "654321", 30, "B+", "456 Elm St", "555-5678"),
    (2, "Jane Smith", "654321", 30, "B+", "456 Elm St", "555-5678"),
    (2, "Jane Smith", "654321", 30, "B+", "456 Elm St", "555-5678"),
    (2, "Jane Smith", "654321", 30, "B+", "456 Elm St", "555-5678"),
    (2, "Jane Smith", "654321", 30, "B+", "456 Elm St", "555-5678"),
    (2, "Jane Smith", "654321", 30, "B+", "456 Elm St", "555-5678"),
    (2, "Jane Smith", "654321", 30, "B+", "456 Elm St", "555-5678"),
    (2, "Jane Smith", "654321", 30, "B+", "456 Elm St", "555-5678"),
    (2, "Jane Smith", "654321", 30, "B+", "456 Elm St", "555-5678"),
    (2, "Jane Smith", "654321", 30, "B+", "456 Elm St", "555-5678"),
    (2, "Jane Smith", "654321", 30, "B+", "456 Elm St", "555-5678"),
    (2, "Jane Smith", "654321", 30, "B+", "456 Elm St", "555-5678"),
    (20, "Jane Smith", "654321", 30, "B+", "456 Elm St", "555-5678"),
    (50, "Jane Smith", "654321", 30, "B+", "456 Elm St", "555-5678"),
    (2, "Jane Smith", "654321", 30, "B+", "456 Elm St", "555-5678"),
    (3, "Jane Smith", "654321", 30, "B+", "456 Elm St", "555-5678")
]

for item in data:
    table.insert("", "end", values=item)

# Display Table
table.pack()

# Frame for delete and edit
buttons_frame = Frame(root) 

# Buttons Frame Styling
style.configure("TFrame",
                background = "#EBF4F6")

# Delete and Edit Buttons
delete_button = Button(buttons_frame , text="Delete" , cursor="hand2" , style="TButton")
edit_button = Button(buttons_frame , text="Edit" , cursor="hand2" , style="TButton")

# Show Buttons
delete_button.pack(side=RIGHT, padx=5)
edit_button.pack(side=LEFT, padx=5)

# Show Frame
buttons_frame.pack(pady=5)

root.mainloop()