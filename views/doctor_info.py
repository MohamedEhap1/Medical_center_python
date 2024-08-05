import tkinter as tk
from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox

# Create the main window
root = tk.Tk()
root.title("Doctor Info")
# root.geometry("1000x800")  # Set the window size

# Set the background color of the window
root.configure(bg='#eaf6f8')

# Create the Treeview widget
style = Style()
style.theme_use('clam')

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



tree = Treeview(table_frame, columns=('Id', 'Name', 'National Id', 'Age', 'Specialty', 'Phone Number'), show='headings')

# Define the column headings
columns = ['Id', 'Name', 'National Id', 'Age', 'Specialty', 'Phone Number']
for col in columns:
    tree.heading(col, text=col)

#
tree.heading("Name" , anchor="w")
tree.heading("National Id" , anchor="w")
tree.heading("Phone Number" , anchor="w")
tree.heading("Specialty" , anchor="w")

# Define the column widths
tree.column('Id', width=50 , anchor="center")
tree.column('Name', width=200)
tree.column('National Id', width=150)
tree.column('Age', width=70 , anchor="center")
tree.column('Specialty', width=150)
tree.column('Phone Number', width=150)


# Create vertical scrollbar
scroll = Scrollbar(table_frame, orient=VERTICAL, command=tree.yview ,
                    style="Vertical.TScrollbar")
# Display Scroll Bar
scroll.pack(side=RIGHT, fill=Y)
tree.configure(yscrollcommand=scroll.set) # 
# Scroll bar Styling
style.configure("Vertical.TScrollbar",
                gripcount=0, # number of '-' in the scroll bar
                background="lightgray", # color of scroll bar and arrows background
                troughcolor="darkgray", # color of background
                arrowcolor="black",
                width=16)
# Add sample data to the Treeview
data = [
    (1, 'John Doe', '123456', 25, 'Cardiology', '555-1234'),
    (2, 'Jane Smith', '654321', 30, 'Neurology', '555-5678'),
    (3, 'Alice Johnson', '789012', 40, 'Pediatrics', '555-9012'),
    (4, 'Bob Brown', '345678', 50, 'Dermatology', '555-3456'),
    (1, 'John Doe', '123456', 25, 'Cardiology', '555-1234'),
    (2, 'Jane Smith', '654321', 30, 'Neurology', '555-5678'),
    (3, 'Alice Johnson', '789012', 40, 'Pediatrics', '555-9012'),
    (4, 'Bob Brown', '345678', 50, 'Dermatology', '555-3456'),
    (1, 'John Doe', '123456', 25, 'Cardiology', '555-1234'),
    (2, 'Jane Smith', '654321', 30, 'Neurology', '555-5678'),
    (3, 'Alice Johnson', '789012', 40, 'Pediatrics', '555-9012'),
    (4, 'Bob Brown', '345678', 50, 'Dermatology', '555-3456'),
    (1, 'John Doe', '123456', 25, 'Cardiology', '555-1234'),
    (2, 'Jane Smith', '654321', 30, 'Neurology', '555-5678'),
    (3, 'Alice Johnson', '789012', 40, 'Pediatrics', '555-9012'),
    (4, 'Bob Brown', '345678', 50, 'Dermatology', '555-3456'),
    (1, 'John Doe', '123456', 25, 'Cardiology', '555-1234'),
    (2, 'Jane Smith', '654321', 30, 'Neurology', '555-5678'),
    (3, 'Alice Johnson', '789012', 40, 'Pediatrics', '555-9012'),
    (4, 'Bob Brown', '345678', 50, 'Dermatology', '555-3456'),
    (1, 'John Doe', '123456', 25, 'Cardiology', '555-1234'),
    (2, 'Jane Smith', '654321', 30, 'Neurology', '555-5678'),
    (3, 'Alice Johnson', '789012', 40, 'Pediatrics', '555-9012'),
    (4, 'Bob Brown', '345678', 50, 'Dermatology', '555-3456'),
    (1, 'John Doe', '123456', 25, 'Cardiology', '555-1234'),
    (2, 'Jane Smith', '654321', 30, 'Neurology', '555-5678'),
    (3, 'Alice Johnson', '789012', 40, 'Pediatrics', '555-9012'),
    (4, 'Bob Brown', '345678', 50, 'Dermatology', '555-3456'),
    (1, 'John Doe', '123456', 25, 'Cardiology', '555-1234'),
    (2, 'Jane Smith', '654321', 30, 'Neurology', '555-5678'),
    (3, 'Alice Johnson', '789012', 40, 'Pediatrics', '555-9012'),
    (4, 'Bob Brown', '345678', 50, 'Dermatology', '555-3456'),
    (1, 'John Doe', '123456', 25, 'Cardiology', '555-1234'),
    (2, 'Jane Smith', '654321', 30, 'Neurology', '555-5678'),
    (3, 'Alice Johnson', '789012', 40, 'Pediatrics', '555-9012'),
    (4, 'Bob Brown', '345678', 50, 'Dermatology', '555-3456'),
    (1, 'John Doe', '123456', 25, 'Cardiology', '555-1234'),
    (2, 'Jane Smith', '654321', 30, 'Neurology', '555-5678'),
    (3, 'Alice Johnson', '789012', 40, 'Pediatrics', '555-9012'),
    (4, 'Bob Brown', '345678', 50, 'Dermatology', '555-3456'),
    (1, 'John Doe', '123456', 25, 'Cardiology', '555-1234'),
    (2, 'Jane Smith', '654321', 30, 'Neurology', '555-5678'),
    (3, 'Alice Johnson', '789012', 40, 'Pediatrics', '555-9012'),
    (4, 'Bob Brown', '345678', 50, 'Dermatology', '555-3456'),
    (1, 'John Doe', '123456', 25, 'Cardiology', '555-1234'),
    (2, 'Jane Smith', '654321', 30, 'Neurology', '555-5678'),
    (3, 'Alice Johnson', '789012', 40, 'Pediatrics', '555-9012'),
    (4, 'Bob Brown', '345678', 50, 'Dermatology', '555-3456'),
    (1, 'John Doe', '123456', 25, 'Cardiology', '555-1234'),
    (2, 'Jane Smith', '654321', 30, 'Neurology', '555-5678'),
    (3, 'Alice Johnson', '789012', 40, 'Pediatrics', '555-9012'),
    (4, 'Bob Brown', '345678', 50, 'Dermatology', '555-3456'),
    (1, 'John Doe', '123456', 25, 'Cardiology', '555-1234'),
    (2, 'Jane Smith', '654321', 30, 'Neurology', '555-5678'),
    (3, 'Alice Johnson', '789012', 40, 'Pediatrics', '555-9012'),
    (4, 'Bob Brown', '345678', 50, 'Dermatology', '555-3456'),
    (1, 'John Doe', '123456', 25, 'Cardiology', '555-1234'),
    (2, 'Jane Smith', '654321', 30, 'Neurology', '555-5678'),
    (3, 'Alice Johnson', '789012', 40, 'Pediatrics', '555-9012'),
    (4, 'Bob Brown', '345678', 50, 'Dermatology', '555-3456'),
    (1, 'John Doe', '123456', 25, 'Cardiology', '555-1234'),
    (2, 'Jane Smith', '654321', 30, 'Neurology', '555-5678'),
    (3, 'Alice Johnson', '789012', 40, 'Pediatrics', '555-9012'),
    (4, 'Bob Brown', '345678', 50, 'Dermatology', '555-3456'),
    (1, 'John Doe', '123456', 25, 'Cardiology', '555-1234'),
    (2, 'Jane Smith', '654321', 30, 'Neurology', '555-5678'),
    (3, 'Alice Johnson', '789012', 40, 'Pediatrics', '555-9012'),
    (4, 'Bob Brown', '345678', 50, 'Dermatology', '555-3456'),
    (1, 'John Doe', '123456', 25, 'Cardiology', '555-1234'),
    (2, 'Jane Smith', '654321', 30, 'Neurology', '555-5678'),
    (3, 'Alice Johnson', '789012', 40, 'Pediatrics', '555-9012'),
    (4, 'Bob Brown', '345678', 50, 'Dermatology', '555-3456'),
    (1, 'John Doe', '123456', 25, 'Cardiology', '555-1234'),
    (2, 'Jane Smith', '654321', 30, 'Neurology', '555-5678'),
    (3, 'Alice Johnson', '789012', 40, 'Pediatrics', '555-9012'),
    (4, 'Bob Brown', '345678', 50, 'Dermatology', '555-3456'),
    (1, 'John Doe', '123456', 25, 'Cardiology', '555-1234'),
    (2, 'Jane Smith', '654321', 30, 'Neurology', '555-5678'),
    (3, 'Alice Johnson', '789012', 40, 'Pediatrics', '555-9012'),
    (4, 'Bob Brown', '345678', 50, 'Dermatology', '555-3456'),
    (1, 'John Doe', '123456', 25, 'Cardiology', '555-1234'),
    (2, 'Jane Smith', '654321', 30, 'Neurology', '555-5678'),
    (3, 'Alice Johnson', '789012', 40, 'Pediatrics', '555-9012'),
    (4, 'Bob Brown', '345678', 50, 'Dermatology', '555-3456'),
    # Add more data as needed
]

for item in data:
    tree.insert('', 'end', values=item)

# Display Table
tree.pack()

# Function to delete an item
def delete_item():
    def confirm_delete():
        id_to_delete = int(entry_id.get())
        messagebox.showinfo("Success", f"Simulated deletion of item with ID {id_to_delete}")
        delete_window.destroy()

    # Create the delete confirmation window
    delete_window = tk.Toplevel(root)
    delete_window.title("Delete Confirmation")
    delete_window.geometry("300x150")
    delete_window.configure(bg='#eaf6f8')

    tk.Label(delete_window, text="Enter ID to delete:", bg='#eaf6f8').pack(pady=10)
    entry_id = tk.Entry(delete_window)
    entry_id.pack(pady=5)

    frame = tk.Frame(delete_window, bg='#eaf6f8')
    frame.pack(pady=10)

    cancel_button = tk.Button(frame, text="Cancel", command=delete_window.destroy, bg='#0a2540', fg='white', font=('Helvetica', 12), width=8, height=1)
    cancel_button.pack(side='left', padx=5)

    confirm_button = tk.Button(frame, text="Delete", command=confirm_delete, bg='#0a2540', fg='white', font=('Helvetica', 12), width=8, height=1)
    confirm_button.pack(side='left', padx=5)

# Create Edit and Delete buttons
frame = tk.Frame(root, bg='#eaf6f8')
frame.pack(pady=10)

edit_button = tk.Button(frame, text="Edit", bg='#0a2540', fg='white', font=('Helvetica', 12), width=8, height=1 , cursor="hand2")
edit_button.pack(padx=10 , side="left")

delete_button = tk.Button(frame, text="Delete", bg='#0a2540', fg='white', font=('Helvetica', 12), width=8, height=1, command=delete_item , cursor="hand2")
delete_button.pack(padx=10 , side="right")

# Run the application
root.mainloop()
