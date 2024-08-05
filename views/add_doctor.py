from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Combobox, Radiobutton, Style  # Import Style from ttk
from PIL import Image, ImageTk
from datetime import date
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
    phone_ent.delete(0, "end")
    id_ent.delete(0, "end")
    age_ent.delete(0, "end")
    date_ent.config(state='normal')
    date_ent.delete(0, "end")
    date_ent.insert(0, date.today().strftime('%Y-%m-%d'))
    date_ent.config(state='readonly')
    combo_stat.set('Select Status')
    combo1_stat.set('Select Bloodtype')
    radio_var.set(1)

# Screen Center Function
def center_screen(root, w, h):
    screenwidth = root.winfo_screenwidth()
    screenheight = root.winfo_screenheight()
    
    x = int((screenwidth - w) / 2)
    y = int((screenheight - h) / 2)
    
    root.geometry(f"{w}x{h}+{x}+{y}")

#Button Add command
def checker():
    if user_ent.get() !='Enter Doctor name' and phone_ent.get() != 'Enter Doctor phone' and id_ent.get()!='Enter Doctor ID' and age_ent.get()!='Enter Docotr Age' and combo_stat.get()!='Medical Specialty' and combo1_stat.get()!='Select Bloodtype' :
        messagebox.showinfo("Succeful", "Data added succefully.")
        reset_frame()
    else:
        messagebox.showerror("Error", "Please make sure to fill all the required info .")
        

# Initialize Tkinter root widget and title
root = Tk()
root.title("Add Doctor")
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
root.iconbitmap("images/patient.ico")

# Background Image
img_path = "images/Add Doctor.png"  # Use raw string for Windows path
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

# User (Doctor name) Icon
usericon_path = "images/Usericon.png"  # Use raw string for Windows path
Userimg = Image.open(usericon_path)
Userimg = Userimg.resize((80, 80))
Userimg_tk = ImageTk.PhotoImage(Userimg)
icon_label = Label(root, image=Userimg_tk, relief='flat', borderwidth=0, highlightthickness=0)
icon_label.place(x=220, y=130)

# Doctor name entry
user_ent = PlaceholderEntry(root, placeholder="Enter Doctor name", font=font1)
user_ent.place(x=300, y=155, width=200, height=30)

# Phone number Icon
phoneicon_path = "images/Phoneicon.png"  # Use raw string for Windows path
phoneimg = Image.open(phoneicon_path)
phoneimg = phoneimg.resize((80, 80))
phoneimg_tk = ImageTk.PhotoImage(phoneimg)
phone_icon_label = Label(root, image=phoneimg_tk, relief='flat', borderwidth=0, highlightthickness=0)
phone_icon_label.place(x=620, y=130)

# Phone number entry
phone_ent = PlaceholderEntry(root, placeholder="Enter Doctor phone", font=font1)
phone_ent.place(x=700, y=155, width=200, height=30)

#Gender Icon
genicon_path = "images/Gender.png"  # Use raw string for Windows path
genimg = Image.open(genicon_path)
genimg = genimg.resize((80, 80))
genimg_tk = ImageTk.PhotoImage(genimg)
gen_icon_label = Label(root, image=genimg_tk, relief='flat', borderwidth=0, highlightthickness=0)
gen_icon_label.place(x=970, y=252)

# Gender radiobuttons
radio_var = IntVar()
radio_var.set(1)

# Create and place radiobuttons
rbtn1 = Radiobutton(root, text="Male", value=1, variable=radio_var)
rbtn2 = Radiobutton(root, text="Female", value=2, variable=radio_var)
rbtn1.pack(padx=110,pady=110)
rbtn2.pack(padx=110,pady=110)
rbtn1.place(x=1050, y=274, width=100, height=30)
rbtn2.place(x=1190, y=274, width=100, height=30)


#Doctor Id icon
idicon_path = "images/Id.png"  # Use raw string for Windows path
idimg = Image.open(idicon_path)
idimg = idimg.resize((80, 80))
idimg_tk = ImageTk.PhotoImage(idimg)
icon_label = Label(root, image=idimg_tk, relief='flat', borderwidth=0, highlightthickness=0)
icon_label.place(x=220, y=250)

#Doctor Id entry
id_ent = PlaceholderEntry(root, placeholder="Enter Doctor ID", font=font1)
id_ent.place(x=300, y=274, width=200, height=30)

#Doctor Age icon
ageicon_path = "images/Age.png"  # Use raw string for Windows path
ageimg = Image.open(ageicon_path)
ageimg = ageimg.resize((80, 80))
ageimg_tk = ImageTk.PhotoImage(ageimg)
phone_icon_label = Label(root, image=ageimg_tk, relief='flat', borderwidth=0, highlightthickness=0)
phone_icon_label.place(x=620, y=250)

#Doctor Age entry
age_ent = PlaceholderEntry(root, placeholder="Enter Doctor Age", font=font1)
age_ent.place(x=700, y=274, width=200, height=30)

#Doctor status icon
staticon_path = "images/status.png"  # Use raw string for Windows path
statimg = Image.open(staticon_path)
statimg = statimg.resize((80, 80))
statimg_tk = ImageTk.PhotoImage(statimg)
phone_icon_label = Label(root, image=statimg_tk, relief='flat', borderwidth=0, highlightthickness=0)
phone_icon_label.place(x=220, y=374)

#Doctor status combo box
combo_stat_var = StringVar()
combo_stat_var.set('Medical Specialty')
combo_stat = Combobox(root, values=('Allergy and Immunology', 'Anesthesiology', 'Cardiology', 'Dermatology', 'Emergency Medicine', 'Family Medicine', 'Gastroenterology', 'Geriatrics', 'Hematology', 'Infectious Disease', 'Internal Medicine', 'Medical Genetics', 'Nephrology', 'Neurology', 'Neurosurgery', 'Obstetrics and Gynecology', 'Oncology', 'Ophthalmology', 'Orthopedic Surgery', 'Otolaryngology', 'Pathology', 'Pediatrics', 'Physical Medicine and Rehabilitation', 'Plastic Surgery', 'Preventive Medicine', 'Psychiatry', 'Pulmonology', 'Radiology', 'Surgery', 'Urology'), textvariable=combo_stat_var, state='readonly')
combo_stat.place(x=300,y=400,width=200,height=30)

#Doctor bloodType icon
# bloodicon_path = "images/BloodType.png"  # Use raw string for Windows path
# bloodimg = Image.open(bloodicon_path)
# bloodimg = bloodimg.resize((80, 80))
# bloodimg_tk = ImageTk.PhotoImage(bloodimg)
# phone_icon_label = Label(root, image=bloodimg_tk, relief='flat', borderwidth=0, highlightthickness=0)
# phone_icon_label.place(x=620, y=374)

# #bloodType combo box
# combo1_stat_var = StringVar()
# combo1_stat_var.set('Select Bloodtype')
# combo1_stat = Combobox(root, values=('White', 'Red', 'Blue','yellow','purple'), textvariable=combo1_stat_var, state='readonly')
# combo1_stat.place(x=700,y=400,width=200,height=30)

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
addbtn.place(x=1050,y=400,width=200,height=30)

# Start Tkinter event loop
root.mainloop()


