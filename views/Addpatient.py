from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Combobox, Radiobutton, Style  # Import Style from ttk
from PIL import Image, ImageTk
from datetime import date
import sqlite3
import os
# Placeholder class
class PlaceholderEntry(Entry):
    def __init__(self, master=None, placeholder="", *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.placeholder = placeholder
        self._placeholder_id = None
        
        # Configure initial appearance
        self._set_placeholder()
        
        # Bind events
        self.bind("<FocusIn>", self._on_focus_in)
        self.bind("<FocusOut>", self._on_focus_out)
    
    def _set_placeholder(self):
        if not self.get():
            self.config(fg='grey')
            self._placeholder_id = self.insert(0, self.placeholder)
            self.icursor(0)

    def _on_focus_in(self, event=None):
        if self.get() == self.placeholder:
            self.delete(0, "end")
            self.config(fg='black')

    def _on_focus_out(self, event=None):
        if not self.get():
            self._set_placeholder()

#reset Frame
def reset_frame():
    user_ent.delete(0, "end")
    user_ent.insert(0,'Enter patient name')
    phone_ent.delete(0, "end")
    phone_ent.insert(0,'Enter patient phone')
    id_ent.delete(0, "end")
    id_ent.insert(0,'Enter patient ID')
    age_ent.delete(0, "end")
    age_ent.insert(0,'Enter patient Age')
    date_ent.config(state='normal')
    date_ent.delete(0, "end")
    date_ent.insert(0, date.today().strftime('%Y-%m-%d'))
    date_ent.config(state='readonly')
    combo_stat.set('Select Status')
    combo1_stat.set('Select Doctor')
    combo2_stat.set('Select blood type')
    radio_var.set('Male')

# Screen Center Function
def center_screen(root, w, h):
    screenwidth = root.winfo_screenwidth()
    screenheight = root.winfo_screenheight()
    
    x = int((screenwidth - w) / 2)
    y = int((screenheight - h) / 2)
    
    root.geometry(f"{w}x{h}+{x}+{y}")


#connect to the database
conn=sqlite3.connect('Medical_Center.db') 
# get a cursur 
cur=conn.cursor()



#Button Add command
def checker():
    if user_ent.get() !='Enter patient name' and phone_ent.get() != 'Enter patient phone' and id_ent.get()!='Enter patient ID' and age_ent.get()!='Enter patient Age' and combo_stat.get()!='Select Status' and combo1_stat.get()!='Select Doctor'and combo2_stat.get()!='Select blood type'and date_ent.get()!='' :
        try:
            cur.execute('''INSERT INTO patient(id,name,age,phone,blood_type,gender,status,nameDoc,datee)
                        
                        VALUES(?,?,?,?,?,?,?,?,?)
                        ''',(id_ent.get(),user_ent.get(),age_ent.get(), phone_ent.get(),combo2_stat.get(),radio_var.get(),combo_stat.get(),combo1_stat.get(),date_ent.get()))
            conn.commit()
            messagebox.showinfo("Succeful", "Data added succefully.")
        except:
            messagebox.showerror("Failed", "Please check your data entry.")
        reset_frame()
    else:
        messagebox.showerror("Error", "Please make sure to fill all the required info .")
        

# Initialize Tkinter root widget and title
root = Tk()
root.title("Add Patient")
font1 = ('times new roman', 14, 'bold')  # Updated font to bold

# Style configuration for the radiobuttons
style = Style()
style.configure("TRadiobutton",
                background="#071952",  # Background color
                foreground="white",    # Text color
                font=('times new roman', 14, 'bold'))  # Font style
style.map("TRadiobutton",
        background=[('selected', '#EBF4F6')],
        foreground=[('selected', 'black')])

# Icon Image
root.iconbitmap("images/Patient.ico")

# Background Image
img_path = "images/Add Patient.png"  # Use raw string for Windows path
img = Image.open(img_path)
img = img.resize((1500, 750))

# Convert image to PhotoImage
img_tk = ImageTk.PhotoImage(img)

# Create a label with the image
bglabel = Label(root, image=img_tk)
bglabel.place(relwidth=1, relheight=1)  # Make label fill the whole window

# Center the window
center_screen(root, 1500, 750)
root.resizable(False, False)

# User (patient name) Icon
usericon_path = "images/Usericon.png"  # Use raw string for Windows path
Userimg = Image.open(usericon_path)
Userimg = Userimg.resize((80, 80))
Userimg_tk = ImageTk.PhotoImage(Userimg)
icon_label = Label(root, image=Userimg_tk, relief='flat', borderwidth=0, highlightthickness=0)
icon_label.place(x=220, y=130)

# Patient name entry
user_ent = PlaceholderEntry(root, placeholder="Enter patient name", font=font1)
user_ent.place(x=300, y=155, width=200, height=30)

# Phone number Icon
phoneicon_path = "images/Phoneicon.png"  # Use raw string for Windows path
phoneimg = Image.open(phoneicon_path)
phoneimg = phoneimg.resize((80, 80))
phoneimg_tk = ImageTk.PhotoImage(phoneimg)
phone_icon_label = Label(root, image=phoneimg_tk, relief='flat', borderwidth=0, highlightthickness=0)
phone_icon_label.place(x=620, y=130)

# Phone number entry
phone_ent = PlaceholderEntry(root, placeholder="Enter patient phone", font=font1)
phone_ent.place(x=700, y=155, width=200, height=30)

#Gender Icon
genicon_path = "images/Gender.png"  # Use raw string for Windows path
genimg = Image.open(genicon_path)
genimg = genimg.resize((80, 80))
genimg_tk = ImageTk.PhotoImage(genimg)
gen_icon_label = Label(root, image=genimg_tk, relief='flat', borderwidth=0, highlightthickness=0)
gen_icon_label.place(x=970, y=252)

# Gender radiobuttons
radio_var = StringVar()
radio_var.set('Male')

# Create and place radiobuttons
rbtn1 = Radiobutton(root, text="Male", value='Male', variable=radio_var)
rbtn2 = Radiobutton(root, text="Female", value='Female', variable=radio_var)
rbtn1.pack(padx=110,pady=110)
rbtn2.pack(padx=110,pady=110)
rbtn1.place(x=1050, y=274, width=100, height=30)
rbtn2.place(x=1190, y=274, width=100, height=30)


#Patient Id icon
idicon_path = "images/Id.png"  # Use raw string for Windows path
idimg = Image.open(idicon_path)
idimg = idimg.resize((80, 80))
idimg_tk = ImageTk.PhotoImage(idimg)
icon_label = Label(root, image=idimg_tk, relief='flat', borderwidth=0, highlightthickness=0)
icon_label.place(x=220, y=250)

#Patient Id entry
id_ent = PlaceholderEntry(root, placeholder="Enter patient ID", font=font1)
id_ent.place(x=300, y=274, width=200, height=30)

#patient Age icon
ageicon_path = "images/Age.png"  # Use raw string for Windows path
ageimg = Image.open(ageicon_path)
ageimg = ageimg.resize((80, 80))
ageimg_tk = ImageTk.PhotoImage(ageimg)
phone_icon_label = Label(root, image=ageimg_tk, relief='flat', borderwidth=0, highlightthickness=0)
phone_icon_label.place(x=620, y=250)

#patient Age entry
age_ent = PlaceholderEntry(root, placeholder="Enter patient Age", font=font1)
age_ent.place(x=700, y=274, width=200, height=30)

#patient status icon
staticon_path = "images/status.png"  # Use raw string for Windows path
statimg = Image.open(staticon_path)
statimg = statimg.resize((80, 80))
statimg_tk = ImageTk.PhotoImage(statimg)
phone_icon_label = Label(root, image=statimg_tk, relief='flat', borderwidth=0, highlightthickness=0)
phone_icon_label.place(x=220, y=374)

#patient status combo box
combo_stat_var = StringVar()
combo_stat_var.set('Select Status')
combo_stat = Combobox(root, values=('Allergy and Immunology', 'Anesthesiology', 'Cardiology', 'Dermatology', 'Emergency Medicine', 'Family Medicine', 'Gastroenterology', 'Geriatrics', 'Hematology', 'Infectious Disease', 'Internal Medicine', 'Medical Genetics', 'Nephrology', 'Neurology', 'Neurosurgery', 'Obstetrics and Gynecology', 'Oncology', 'Ophthalmology', 'Orthopedic Surgery', 'Otolaryngology', 'Pathology', 'Pediatrics', 'Physical Medicine and Rehabilitation', 'Plastic Surgery', 'Preventive Medicine', 'Psychiatry', 'Pulmonology', 'Radiology', 'Surgery', 'Urology'), textvariable=combo_stat_var, state='readonly')
combo_stat.place(x=300,y=400,width=200,height=30)

# blood_type  icon
blood_type_path = "images/BloodType.png"  # Use raw string for Windows path
blood_type_img = Image.open(blood_type_path)
blood_type_img = blood_type_img.resize((80, 80))
blood_type_tk = ImageTk.PhotoImage(blood_type_img)
blood_type_label = Label(root, image=blood_type_tk, relief='flat', borderwidth=0, highlightthickness=0)
blood_type_label.place(x=970, y=374)

#blood_type combo box
combo2_stat_var = StringVar()
combo2_stat_var.set('Select bllod type')
combo2_stat = Combobox(root, values=('A ', 'B', 'O','A+','C'), textvariable=combo2_stat_var, state='readonly')
combo2_stat.place(x=1050,y=400,width=200,height=30)

# Doctor Name icon
doctor_name_path = "images/Doctor Icon.png"  # Use raw string for Windows path
doctor_name_img = Image.open(doctor_name_path)
doctor_name_img = doctor_name_img.resize((80, 80))
doctor_name_tk = ImageTk.PhotoImage(doctor_name_img)
doctor_name_label = Label(root, image=doctor_name_tk, relief='flat', borderwidth=0, highlightthickness=0)
doctor_name_label.place(x=620, y=374)

#Doctor Name combo box
combo1_stat_var = StringVar()
combo1_stat_var.set('Select Doctor')
combo1_stat = Combobox(root, values=('Ahmed ', 'Hassan', 'Mohamed','Weliam','cris'), textvariable=combo1_stat_var, state='readonly')
combo1_stat.place(x=700,y=400,width=200,height=30)


#date icon
dateicon_path = "images/calender.png"  # Use raw string for Windows path
dateimg = Image.open(dateicon_path)
dateimg = dateimg.resize((80, 80))
dateimg_tk = ImageTk.PhotoImage(dateimg)
date_icon_label = Label(root, image=dateimg_tk, relief='flat', borderwidth=0, highlightthickness=0)
date_icon_label.place(x=970, y=130)

#date entry
date_ent = Entry(root, font=font1)
date_ent.insert(0, date.today().strftime('%Y-%m-%d'))
date_ent.place(x=1050, y=155, width=225, height=30)

#add button
addbtn=Button(root, text = "Add", font=font1, width=30,height=50,command=checker, bg='#37B7C3', fg='#EBF4F6')
addbtn.place(x=700,y=500,width=200,height=30)
# back button
def backBtn():
    root.destroy()
    os.system("python views/dashboard.py")
    
back_img = Image.open("images/BackBtn.png")
back_tk = ImageTk.PhotoImage(back_img)
back_button = Button(root, image=back_tk,relief='flat',command=backBtn)
back_button.place(x=10, y=10)
# Start Tkinter event loop
root.mainloop()
conn.close()

