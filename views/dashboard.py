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


# Initialize Tkinter root widget and title
root = Tk()
root.title("Medical Center")
font1 = ('times new roman', 14, 'bold')  # Updated font to bold

# Style configuration for the radiobuttons
style = Style()

# Icon Image
root.iconbitmap("images/Patient.ico")

# Background Image
img_path = "images/main menu.jpg"  # Use raw string for Windows path
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


#Add Doctor button
btnx=680
btny=200
img_add = Image.open("images/Add doctor btn.png")
img_tk_Add_doc = ImageTk.PhotoImage(img_add)
AddDoc_button = Button(root, image=img_tk_Add_doc)
AddDoc_button.place(x=btnx, y=btny)
#Add Patient button
img_add = Image.open("images/Add patient btn.png")
img_tk_Add_pat = ImageTk.PhotoImage(img_add)
AddDoc_button = Button(root, image=img_tk_Add_pat)
AddDoc_button.place(x=btnx, y=btny+100)
#Doctor info button
img_add = Image.open("images/Doctor Info btn.png")
img_tk_DocInfo = ImageTk.PhotoImage(img_add)
AddDoc_button = Button(root, image=img_tk_DocInfo)
AddDoc_button.place(x=btnx, y=btny+200)
#patient info button
img_add = Image.open("images/Patient info btn.png")
img_tk_PatInfo = ImageTk.PhotoImage(img_add)
AddDoc_button = Button(root, image=img_tk_PatInfo)
AddDoc_button.place(x=btnx, y=btny+300)

# Start Tkinter event loop
root.mainloop()


