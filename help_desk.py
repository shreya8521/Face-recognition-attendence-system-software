from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2

class HelpDesk:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Help desk");

        title_lbl=Label(self.root,text="Help Desk",font=("times new roman",32,"bold"),bg="black",fg="red")
        title_lbl.place(x=0,y=0,width=1280,height=45)

        img_top=Image.open(r"pictures\secondimage.jfif")
        img_top=img_top.resize((1280,610),Image.ANTIALIAS)
        self.photoimg_top=ImageTk.PhotoImage(img_top)

        f_label=Label(self.root,image=self.photoimg_top)
        f_label.place(x=0,y=45,width=1280,height=610)

        help_label=Label(f_label,text="Email:shreyadokaniagrd@gmail.com",font=("times new roman",12,"bold"),bg="white")
        help_label.place(x=500,y=300)

       


if __name__ =="__main__":
    root=Tk()
    obj=HelpDesk(root)
    root.mainloop()