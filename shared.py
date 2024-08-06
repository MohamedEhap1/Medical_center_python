from tkinter import *
from PIL import Image ,ImageTk
root=Tk()
# screen info
weidth=1000    
height=500
def screen(root):
    x=int((root.winfo_screenwidth()-weidth)/2)
    y=int((root.winfo_screenheight()-height)/2)
    root.title("Medical Center")
    root.geometry(f"{weidth}x{height}+{x}+{y}")
    root.resizable(False,False)

screen(root)
# Background image
def background(root, weidth, height,path_img):
    img=Image.open(path_img)
    image=img.resize((weidth,height))
    img_tk=ImageTk.PhotoImage(image)
    lb=Label(root,image=img_tk)
    lb.image = img_tk  # This line keeps a reference to the image
    lb.pack()

background(root=root,weidth= weidth,height= height,path_img='images/background.jpg')






root.mainloop()