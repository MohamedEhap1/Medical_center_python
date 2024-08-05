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

# Screen Center Function
def center_screen(root, w, h):
    screenwidth = root.winfo_screenwidth()
    screenheight = root.winfo_screenheight()
    
    x = int((screenwidth - w) / 2)
    y = int((screenheight - h) / 2)
    
    root.geometry(f"{w}x{h}+{x}+{y}")

#Login Cheacker Function
def checker():
    username='admin'
    password='admin'

    if user_ent.get() !='Enter Username' and user_ent.get()==username and  pass_ent.get() !='**********' and pass_ent.get()==password:
        messagebox.showinfo("Succeful", "Log in succesfully.")
    
    else:
        messagebox.showerror("Error", "Wrong Username or Password.")
# Initialize Tkinter root widget and title
root = Tk()
root.title("Login Screen")
font1 = ('times new roman', 14, 'bold')  # Updated font to bold

#Login screen icon
root.iconbitmap("images/Loginicon.ico")

#Login screen background 

# Background Image
img_path = "images/Loginscreen.png"  # Use raw string for Windows path
img = Image.open(img_path)
img = img.resize((1500, 750))

# Convert image to PhotoImage
img_tk = ImageTk.PhotoImage(img)

# Create a label with the image
bglabel = Label(root, image=img_tk)
bglabel.place(relwidth=1, relheight=1)

# Center the window
center_screen(root, 1500, 750)
root.resizable(False, False)

#username Icon
usericon_path = "images/usernameicon.png"  # Use raw string for Windows path
Userimg = Image.open(usericon_path)
Userimg = Userimg.resize((80, 80))
Userimg_tk = ImageTk.PhotoImage(Userimg)
icon_label = Label(root, image=Userimg_tk, relief='flat', borderwidth=0, highlightthickness=0)
icon_label.place(x=300, y=245)

# Username entry
user_ent = PlaceholderEntry(root, placeholder="Enter Username", font=font1)
user_ent.place(x=390, y=270, width=200, height=30)

#Password icon
passicon_path = "images/Passwordicon.png"  # Use raw string for Windows path
passimg = Image.open(passicon_path)
passimg = passimg.resize((80, 80))
passimg_tk = ImageTk.PhotoImage(passimg)
icon_labe = Label(root, image=passimg_tk, relief='flat', borderwidth=0, highlightthickness=0)
icon_labe.place(x=300, y=375)

#password entry
pass_ent = PlaceholderEntry(root, placeholder="**********", font=font1,show='*')
pass_ent.place(x=390, y=400, width=200, height=30)

#sign in Button
addbtn=Button(root, text = "Add", font=font1,command=checker, width=30,height=50, bg='#37B7C3', fg='#EBF4F6')
addbtn.place(x=430,y=500,width=100,height=30)



# Start Tkinter event loop
root.mainloop()