from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2

class Developer:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Developer");

        title_lbl=Label(self.root,text="DEVELOPER",font=("times new roman",32,"bold"),bg="black",fg="white")
        title_lbl.place(x=0,y=0,width=1280,height=45)

        img_top=Image.open(r"pictures\dev.webp")
        img_top=img_top.resize((1280,610),Image.ANTIALIAS)
        self.photoimg_top=ImageTk.PhotoImage(img_top)

        f_label=Label(self.root,image=self.photoimg_top)
        f_label.place(x=0,y=45,width=1280,height=610)

        #frame 

        main_frame=Frame(f_label,bd=2,bg="white")
        main_frame.place(x=900,y=0,width=350,height=300)

        #developer image
        img_developer=Image.open(r"pictures\shreya.jpeg")
        img_developer=img_developer.resize((250,200),Image.ANTIALIAS)
        self.photoimg_developer=ImageTk.PhotoImage(img_developer)

        f_label=Label(main_frame,image=self.photoimg_developer)
        f_label.place(x=50,y=0,width=250,height=200)

        #developer info

        dev_label=Label(main_frame,text="Hello,my name is Shreya Dokania",font=("times new roman",15,"bold"),bg="white")
        dev_label.place(x=30,y=205)

        # dev_label=Label(main_frame,text="I am a full stack developer",font=("times new roman",11,"bold"),bg="white")
        # dev_label.place(x=0,y=40)

        # img3=Image.open(r"C:\Users\hp\OneDrive\Desktop\face regonisition system\pictures\thirdimage.webp")
        # img3=img3.resize((380,300),Image.ANTIALIAS)
        # self.photoimg3=ImageTk.PhotoImage(img3)

        # f_label=Label(main_frame,image=self.photoimg3)
        # f_label.place(x=0,y=210,width=380,height=300)





if __name__ =="__main__":
    root=Tk()
    obj=Developer(root)
    root.mainloop()