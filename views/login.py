# Import necessary modules from the Tkinter and PIL libraries
from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox
from PIL import Image, ImageTk

# Constants for the window size
WINDOW_WIDTH = 1000
WINDOW_HEIGHT = 600

#Styling properties
# style = Style()
# style.theme_use('c') # To make Style modern 

class MedicalCenterGUI:
    def __init__(self, master):
        # Initialize the GUI window
        self.master = master
        self.master.title("Medical Center")
        self.center_window()
        self.load_background_image()
        self.create_login_frame()
        self.create_login_elements()
        self.create_login_button()

    # Center the GUI window on the screen
    def center_window(self):
        x = int((self.master.winfo_screenwidth() - WINDOW_WIDTH) / 2)
        y = int((self.master.winfo_screenheight() - WINDOW_HEIGHT) / 2)
        self.master.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}+{x}+{y}")
        self.master.resizable(False, False)

    # Load an image from a file path and resize it if necessary
    def load_image(self, file_path, size=None):
        try:
            img = Image.open(file_path)
            if size:
                img = img.resize(size)
            return ImageTk.PhotoImage(img)
        except Exception as e:
            raise RuntimeError(f"Error loading image: {e}")

    # Load the background image for the GUI
    def load_background_image(self):
        self.bg_image = self.load_image('images/background.jpg', size=(1280, 700))
        self.bg_label = Label(self.master, image=self.bg_image)
        self.bg_label.place(x=0, y=0)

    # Create the login frame for the GUI
    def create_login_frame(self):
        self.login_frame = Frame(self.master)
        self.style = Style()
        self.style.configure('Tlogin_frame.TFrame', background='white',borderwidth=0, highlightthickness=0)
        self.login_frame.place(anchor='center', relx=0.5, rely=0.5)
        self.login_frame.configure(style='Tlogin_frame.TFrame')

    # Create the login elements (logo, username, password) within the login frame
    def create_login_elements(self):
        self.logo_image = self.load_image('images/icon_login.jpg')
        self.logo_label = Label(self.login_frame, image=self.logo_image)
        self.logo_label.grid(row=0, column=0, columnspan=2, pady=10)

        self.username_image = self.load_image('images/username.jpg')
        self.username_label = Label(self.login_frame, image=self.username_image, text="Username", compound=LEFT, font=('times new roman', 15))
        self.username_label.grid(row=1, column=0, padx=10, pady=10)

        self.username_entry = Entry(self.login_frame, font=('times new roman', 15, 'bold'))
        self.username_entry.grid(row=1, column=1, padx=10, pady=10)

        self.password_image = self.load_image('images/password.jpg')
        self.password_label = Label(self.login_frame, image=self.password_image, text="Password", compound=LEFT, font=('times new roman', 15))
        self.password_label.grid(row=2, column=0, pady=10)

        self.password_entry = Entry(self.login_frame, font=('times new roman', 15, 'bold'), show='*')
        self.password_entry.grid(row=2, column=1, pady=10)

    # Handle the login process
    def login(self):
        if self.username_entry.get() == '' or self.password_entry.get() == '':
            messagebox.showerror('Error', 'Fields cannot be empty')
        elif self.username_entry.get() == 'kareem' and self.password_entry.get() == '1234':
            messagebox.showinfo('Success', 'Welcome')
        else:
            messagebox.showerror('Error', 'Please enter correct value')

    # Create the login button
    def create_login_button(self):
        self.login_button = Button(self.login_frame, text='Login', command=self.login)
        self.style = Style()
        self.style.configure('TButton', background='blue',borderwidth=0)
        self.login_button.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

# Run the main loop of the GUI
if __name__ == "__main__":
    root = Tk()
    app = MedicalCenterGUI(root)
    root.mainloop()