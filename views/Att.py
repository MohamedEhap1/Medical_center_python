import tkinter as tk
from tkinter import ttk
from tkinter import *
from tkinter .ttk import *
# Sample data
doctors = [
    {"name": "Dr. Smith", "specialization": "Cardiology"},
    {"name": "Dr. Johnson", "specialization": "Neurology"},
    {"name": "Dr. Williams", "specialization": "Orthopedics"},
    {"name": "Dr. Williams", "specialization": "Orthopedics"},
    {"name": "Dr. Williams", "specialization": "Orthopedics"},
    {"name": "Dr. Williams", "specialization": "Orthopedics"},
    {"name": "Dr. Williams", "specialization": "Orthopedics"},
    {"name": "Dr. Williams", "specialization": "Orthopedics"},
    {"name": "Dr. Williams", "specialization": "Orthopedics"},
    {"name": "Dr. Williams", "specialization": "Orthopedics"},
]

# Create the main window
root = tk.Tk()
root.title("Doctors Attendance")

# Create a frame for the table
frame = tk.Frame(root)
frame.pack()

# Create a Treeview widget
tree = ttk.Treeview(frame, columns=("Name", "Specialization", "Attendance"), show='headings')
tree.heading("Name", text="Name")
tree.heading("Specialization", text="Specialization")
tree.heading("Attendance", text="Attendance")

# Add data to the Treeview
for doctor in doctors:
    tree.insert("", "end", values=(doctor["name"], doctor["specialization"], ""))

tree.grid(row=0, column=0, sticky='nsew')


#add colors
style = ttk.Style()
style.theme_use("clam") # To make Style modern
style.theme_use('default')
style.configure("Treeview",
                   background="#37B7C3",
                   foreground="#EBF4F6",
                   rowheight=25,
                   fieldbackground="#d9d9d9")
style.map('Treeview',
            background=[('selected', '#37B7C3')],
            foreground=[('selected', 'white')])

style.configure("Treeview.Heading", # Headings Styling
                background="#071952", 
                foreground="white"
                )
# Create a frame for checkboxes
checkbox_frame = tk.Frame(frame)
checkbox_frame.grid(row=0, column=1, sticky='nsew')

# Create checkboxes for attendance
attendance_vars = []
for i, doctor in enumerate(doctors):
    var = tk.BooleanVar()
    checkbox = tk.Checkbutton(checkbox_frame, variable=var)
    checkbox.grid(row=i, column=0, sticky='w')
    attendance_vars.append(var)

# Function to update attendance
def update_attendance():
    for i, item in enumerate(tree.get_children()):
        values = tree.item(item, "values")
        attendance = "Present" if attendance_vars[i].get() else "Absent"
        tree.item(item, values=(values[0], values[1], attendance))

# Button to update attendance
update_button = tk.Button(root, text="Update Attendance", command=update_attendance ,font=('Arial',11),bg='#071952',fg="#EBF4F6")
update_button.pack()

# Run the application
root.mainloop()
