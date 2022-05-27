from tkinter import*    
from tkinter import ttk
import tkinter
from PIL import Image,ImageTk
import tkinter
import os
from student import Student
from train import Training_Data
from face_recognistion import Face_Recognition
from attendence import Attendence
from developer import Developer
from help_desk import HelpDesk
from time import strftime
from datetime import datetime
from chatbot import ChatBot

class Face_recognition_System:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face regonistion System")

        #firstImage 
        img1=Image.open(r"pictures\firstimage.webp")
        img1=img1.resize((420,130),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        f_label=Label(self.root,image=self.photoimg1)
        f_label.place(x=0,y=0,width=420,height=130)

        #secondImage

        img2=Image.open(r"pictures\secondimage.jfif")
        img2=img2.resize((420,130),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        f_label=Label(self.root,image=self.photoimg2)
        f_label.place(x=420,y=0,width=420,height=130)

        #thirdImage

        img3=Image.open(r"pictures\thirdimage.webp")
        img3=img3.resize((450,130),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        f_label=Label(self.root,image=self.photoimg3)
        f_label.place(x=840,y=0,width=450,height=130)

        #bg image

        img4=Image.open(r"pictures\black_light.jpg")
        self.photoimg4=ImageTk.PhotoImage(img4)

        bg_image=Label(self.root,image=self.photoimg4)
        bg_image.place(x=0,y=130,width=1280,height=520)

        title_lbl=Label(bg_image,text="FACE RECOGNITION ATTENDENCE SYSTEM SOFTWARE",font=("Bodoni MT",25,"bold"),bg="#CD7054",fg="#F5F5F5")
        title_lbl.place(x=0,y=0,width=1280,height=45)

        def time():
            string = strftime('%H:%M:%S %p')
            lbl.config(text=string)
            lbl.after(1000,time)

        lbl=Label(title_lbl, font = ('times new roman',14,'bold'),background='#CD7054',foreground='white')
        lbl.place(x=0,y=5,width=110,height=50)
        time()

        #student Button

        img5=Image.open(r"pictures\student.jpg")
        img5=img5.resize((190,200),Image.ANTIALIAS)
        self.photoimg5=ImageTk.PhotoImage(img5)

        b1=Button(bg_image,bd=2,image=self.photoimg5,command=self.student_details,cursor="hand2")
        b1.place(x=100,y=100,width=200,height=150)  

        b1_1=Button(bg_image,text="Student Details",command=self.student_details,cursor="hand2",font=("times new roman",15,"bold"),bg="#CD7054",fg="#FCFCFC")
        b1_1.place(x=100,y=250,width=200,height=40)

        #detect face Button

        img6=Image.open(r"pictures\facedetect.jpg")
        img6=img6.resize((190,200),Image.ANTIALIAS)
        self.photoimg6=ImageTk.PhotoImage(img6)

        b1=Button(bg_image,bd=2,image=self.photoimg6,cursor="hand2",command=self.face_data)
        b1.place(x=400,y=100,width=200,height=150)

        b1_1=Button(bg_image,text="Face Detector",cursor="hand2",command=self.face_data,font=("times new roman",15,"bold"),bg="#CD7054",fg="white")
        b1_1.place(x=400,y=250,width=200,height=40)

        #attendence face Button

        img7=Image.open(r"pictures\attendence.jpg")
        img7=img7.resize((190,200),Image.ANTIALIAS)
        self.photoimg7=ImageTk.PhotoImage(img7)

        b1=Button(bg_image,bd=2,image=self.photoimg7,cursor="hand2",command=self.attendence_data)
        b1.place(x=700,y=100,width=200,height=150)

        b1_1=Button(bg_image,text="Attendence",cursor="hand2",command=self.attendence_data,font=("times new roman",15,"bold"),bg="#CD7054",fg="white")
        b1_1.place(x=700,y=250,width=200,height=40)

        # chat bot Button

        img8=Image.open(r"C:\Users\hp\OneDrive\Desktop\face regonisition system\chat-bot.webp")
        img8=img8.resize((190,200),Image.ANTIALIAS)
        self.photoimg8=ImageTk.PhotoImage(img8)

        b1=Button(bg_image,bd=2,image=self.photoimg8,cursor="hand2",command=self.chatbot_data)
        b1.place(x=1000,y=100,width=200,height=150)

        b1_1=Button(bg_image,text="ChatBot",cursor="hand2",command=self.chatbot_data,font=("times new roman",15,"bold"),bg="#CD7054",fg="white")
        b1_1.place(x=1000,y=250,width=200,height=40)

        #train data 

        img9=Image.open(r"pictures\train_data.jpg")
        img9=img9.resize((190,200),Image.ANTIALIAS)
        self.photoimg9=ImageTk.PhotoImage(img9)

        b1=Button(bg_image,bd=2,image=self.photoimg9,cursor="hand2",command=self.train_data)
        b1.place(x=100,y=300,width=200,height=150)

        b1_1=Button(bg_image,text="Train Data ",cursor="hand2",command=self.train_data,font=("times new roman",15,"bold"),bg="#CD7054",fg="white")
        b1_1.place(x=100,y=450,width=200,height=40)

        #photos data 

        img10=Image.open(r"pictures\photo.jpg")
        img10=img10.resize((190,200),Image.ANTIALIAS)
        self.photoimg10=ImageTk.PhotoImage(img10)

        b1=Button(bg_image,bd=2,image=self.photoimg10,cursor="hand2",command=self.open_img)
        b1.place(x=400,y=300,width=200,height=150)

        b1_1=Button(bg_image,text="Photos ",cursor="hand2",command=self.open_img,font=("times new roman",15,"bold"),bg="#CD7054",fg="white")
        b1_1.place(x=400,y=450,width=200,height=40)

        #developer page  data 

        img11=Image.open(r"pictures\developer.jpg")
        img11=img11.resize((190,200),Image.ANTIALIAS)
        self.photoimg11=ImageTk.PhotoImage(img11)

        b1=Button(bg_image,bd=2,image=self.photoimg11,cursor="hand2",command=self.developer_data)
        b1.place(x=700,y=300,width=200,height=150)

        b1_1=Button(bg_image,text="Developer",cursor="hand2",command=self.developer_data,font=("times new roman",15,"bold"),bg="#CD7054",fg="white")
        b1_1.place(x=700,y=450,width=200,height=40)

        #exit face button

        img12=Image.open(r"pictures\exit.jpg")
        img12=img12.resize((190,200),Image.ANTIALIAS)
        self.photoimg12=ImageTk.PhotoImage(img12)

        b1=Button(bg_image,bd=2,image=self.photoimg12,cursor="hand2",command=self.iExit)
        b1.place(x=1000,y=300,width=200,height=150)

        b1_1=Button(bg_image,text="Exit ",cursor="hand2",command=self.iExit,font=("times new roman",15,"bold"),bg="#CD7054",fg="white")
        b1_1.place(x=1000,y=450,width=200,height=40)

    #to open the image

    def open_img(self):
        os.startfile("data")

    #to exit 

    def iExit(self):
        self.iExit=tkinter.messagebox.askyesno("Face Recognition","Are you sure you want to exit this project",parent=self.root)
        if self.iExit>0:
            self.root.destroy()
        else:
            return




    #function buttons 

    def student_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Student(self.new_window)

    def train_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Training_Data(self.new_window)

    def face_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Face_Recognition(self.new_window)

    def attendence_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Attendence(self.new_window)

    def developer_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Developer(self.new_window)

    def chatbot_data(self):
        self.new_window=Toplevel(self.root)
        self.app=ChatBot(self.new_window)



if __name__ =="__main__":
    root=Tk();
    obj=Face_recognition_System(root)
    root.mainloop()
