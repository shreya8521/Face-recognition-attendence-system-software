from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import tkinter
from student import Student
from train import Training_Data
from face_recognistion import Face_Recognition
from attendence import Attendence
from developer import Developer
from help_desk import HelpDesk
from time import strftime
from datetime import datetime
from chatbot import ChatBot
from main import Face_recognition_System



def main():
    win=Tk()
    app=Login_Window(win)
    win.mainloop()


class Login_Window:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Login")

        self.bg=ImageTk.PhotoImage(file=r"C:\Users\hp\OneDrive\Desktop\face regonisition system\pictures\black_light.jpg")
        lbl_bg=Label(self.root,image=self.bg)
        lbl_bg.place(x=0,y=0,relwidth=1,relheight=1)

        frame=Frame(self.root,bg="#CD7054")
        frame.place(x=510,y=170,width=340,height=450)

        img1=Image.open(r"pictures\black_login.jpg")
        img1=img1.resize((100,100),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        lblimage1=Label(image=self.photoimg1,bg="black",borderwidth=0)
        lblimage1.place(x=630,y=170,width=100,height=100)

        get_str=Label(frame,text="GET STARTED",font=("Bodoni MT",20,"bold"),bg="#CD7054",fg="#F5F5F5")
        get_str.place(x=85,y=100)

        #label 
        username=lbl=Label(frame,text="Username:",font=("Bodoni MT",15,"bold"),bg="#CD7054",fg="black")
        username.place(x=38,y=155)

        self.txtuser=ttk.Entry(frame,font=("Bodoni MT",15,"bold"))
        self.txtuser.place(x=40,y=180,width=270)

        password=lbl=Label(frame,text="Password:",font=("Bodoni MT",15,"bold"),bg="#CD7054",fg="black")
        password.place(x=38,y=225)

        self.txtpass=ttk.Entry(frame,font=("Bodoni MT",15,"bold"))
        self.txtpass.place(x=40,y=250,width=270)

        loginbtn=Button(frame,command=self.login,text="Login",font=("Bodoni MT",20,"bold"),bd=3,relief=RIDGE,fg="white",bg="black")
        loginbtn.place(x=110,y=300,width=120,height=35)

        registerbtn=Button(frame,text="New user Register",command=self.register_win,font=("Bodoni MT",10,"bold"),borderwidth=0,fg="black",bg="#CD7054",activebackground="#CD7054")
        registerbtn.place(x=15,y=350,width=160)

        forgetpassbtn=Button(frame,text="Forget Password",command=self.forget_pass_win,font=("Bodoni MT",10,"bold"),borderwidth=0,fg="black",bg="#CD7054",activebackground="#CD7054")
        forgetpassbtn.place(x=10,y=370,width=160)
    
    def register_win(self):
        self.new_window=Toplevel(self.root)
        self.app=Register(self.new_window)

    def login(self):
        if self.txtuser.get()=="" or self.txtpass.get()=="":
            messagebox.showerror("Error","All fields are required")

        elif self.txtuser.get()=="shreya" and self.txtpass.get()=="shreya8521":
            messagebox.showinfo("Welcome","logged in successfully")

        else:
            conn=mysql.connector.connect(host="localhost",user="root",password="shreya8521",database="mydata")
            my_cursor=conn.cursor()
            my_cursor.execute("select * from registerr where email=%s and password=%s",(
                self.txtuser.get(),
                self.txtpass.get()
            ))
            row=my_cursor.fetchone()
            if row==None:
                messagebox.showerror("Error","Invalid Username or password")
            else:
                open_main=messagebox.askyesno("YesNo","Access only admin")
                if open_main>0:
                    self.new_window=Toplevel(self.root)
                    self.app=Face_recognition_System(self.new_window)
                else:
                    if not open_main:
                        return
            conn.commit()
            conn.close()

    #reset password window
    def reset_pass(self):
        if self.combo_security_Q.get()=="Select":
            messagebox.showerror("Error","Select Security Question",parent=self.root2)
        elif self.txt_security_A.get()=="":
            messagebox.showerror("Error","Please enter the answer",parent=self.root2)
        elif self.txt_new_password.get()=="":
            messagebox.showerror("Error","Please enter the new password",parent=self.root2)
        else:
            conn=mysql.connector.connect(host="localhost",user="root",password="shreya8521",database="mydata")
            my_cursor=conn.cursor()
            qury=("select * from registerr where email=%s and securityQ=%s and securityA=%s")
            vlue=(self.txtuser.get(),self.combo_security_Q.get(),self.txt_security_A.get(),)
            my_cursor.execute(qury,vlue)
            row=my_cursor.fetchone()
            if row==None:
                messagebox.showerror("Error","Please enter correct Answer",parent=self.root2)
            else:
                query=("update registerr set password=%s where email=%s")
                value=(self.txt_new_password.get(),self.txtuser.get())
                my_cursor.execute(query,value)

                conn.commit()
                conn.close()
                messagebox.showinfo("Info","Your password has been reset",parent=self.root2)
                self.root2.destroy()
    
    #forget password window

    def forget_pass_win(self):
        if self.txtuser.get()=="":
            messagebox.showerror("Error","Enter the Email Address to reset password")
        else:
            conn=mysql.connector.connect(host="localhost",user="root",password="shreya8521",database="mydata")
            my_cursor=conn.cursor()
            query=("select * from registerr where email=%s")
            value=(self.txtuser.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()

            if row==None:
                messagebox.showerror("Error","Please enter valid username")
            else:
                conn.close()
                self.root2=Toplevel()
                self.root2.title("Forget Password")
                self.root2.geometry("340x450+510+170")

                l=Label(self.root2,text="Forget Password",font=("Bodoni MT",15,"bold"),bg="#CD7054",fg="white")
                l.place(x=0,y=10,relwidth=1)

                security_q=Label(self.root2,text="Select Security Question",font=("times new roman",10,"bold"),bg="white")
                security_q.place(x=50,y=80)

                self.combo_security_Q=ttk.Combobox(self.root2,font=("times new roman",10,"bold"),state="readonly")
                self.combo_security_Q["values"]=("Select","Your Birth Place","Your School Name","Your Pet Name")
                self.combo_security_Q.place(x=50,y=110,width=200)
                self.combo_security_Q.current(0)

                security_A=Label(self.root2,text="Security Answer",font=("times new roman",10,"bold"),bg="white")
                security_A.place(x=50,y=150)

                self.txt_security_A=ttk.Entry(self.root2,font=("times new roman",10,"bold"))
                self.txt_security_A.place(x=50,y=180,width=200)

                new_password=Label(self.root2,text="New Password",font=("times new roman",10,"bold"),bg="white")
                new_password.place(x=50,y=220)

                self.txt_new_password=ttk.Entry(self.root2,font=("times new roman",10,"bold"))
                self.txt_new_password.place(x=50,y=250,width=200)

                btn=Button(self.root2,text="Reset",command=self.reset_pass,font=("times new roman",10,"bold"),fg="white",bg="#CD7054")
                btn.place(x=100,y=290)

                



                







                

            

class Register:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Register")

        #variables 
        self.var_fname=StringVar()
        self.var_lname=StringVar()
        self.var_contact=StringVar()
        self.var_email=StringVar()
        self.var_security_q=StringVar()
        self.var_security_A=StringVar()
        self.var_pswd=StringVar()
        self.var_confirm_pswd=StringVar()

        #background image

        self.bg=ImageTk.PhotoImage(file=r"C:\Users\hp\OneDrive\Desktop\face regonisition system\pictures\blue_back.jpg")
        bg_lbl=Label(self.root,image=self.bg)
        bg_lbl.place(x=0,y=0,relheight=1,relwidth=1)

        #left image

        self.bg1=ImageTk.PhotoImage(file=r"C:\Users\hp\OneDrive\Desktop\face regonisition system\pictures\side2.jpeg")
        left_lbl=Label(self.root,image=self.bg1)
        left_lbl.place(x=40,y=90,width=370,height=500)

        #main frame

        frame=Frame(self.root,bg="white")
        frame.place(x=410,y=90,width=700,height=500)

        #label 
        register_lbl=Label(frame,text="REGISTER HERE",font=("times new roman",20,"bold"),fg="black",bg="white")
        register_lbl.place(x=20,y=20)

        #row1
        fname=Label(frame,text="First Name",font=("times new roman",10,"bold"),bg="white")
        fname.place(x=50,y=100)

        fname_entry=ttk.Entry(frame,textvariable=self.var_fname,font=("times new roman",10,"bold"))
        fname_entry.place(x=50,y=130,width=200)

        lname=Label(frame,text="Last Name",font=("times new roman",10,"bold"),bg="white")
        lname.place(x=300,y=100)

        self.txt_lname=ttk.Entry(frame,textvariable=self.var_lname,font=("times new roman",10,"bold"))
        self.txt_lname.place(x=300,y=130,width=200)

        #row2

        contact=Label(frame,text="Contact No",font=("times new roman",10,"bold"),bg="white")
        contact.place(x=50,y=170)

        self.txt_contact=ttk.Entry(frame,textvariable=self.var_contact,font=("times new roman",10,"bold"))
        self.txt_contact.place(x=50,y=200,width=200)

        email=Label(frame,text="Email",font=("times new roman",10,"bold"),bg="white")
        email.place(x=300,y=170)

        self.txt_email=ttk.Entry(frame,textvariable=self.var_email,font=("times new roman",10,"bold"))
        self.txt_email.place(x=300,y=200,width=200)

        #row3 
        security_q=Label(frame,text="Select Security Question",font=("times new roman",10,"bold"),bg="white")
        security_q.place(x=50,y=240)

        self.combo_security_Q=ttk.Combobox(frame,textvariable=self.var_security_q,font=("times new roman",10,"bold"),state="readonly")
        self.combo_security_Q["values"]=("Select","Your Birth Place","Your School Name","Your Pet Name")
        self.combo_security_Q.place(x=50,y=270,width=200)
        self.combo_security_Q.current(0)

        security_A=Label(frame,text="Security Answer",font=("times new roman",10,"bold"),bg="white")
        security_A.place(x=300,y=240)

        self.txt_security_A=ttk.Entry(frame,textvariable=self.var_security_A,font=("times new roman",10,"bold"))
        self.txt_security_A.place(x=300,y=270,width=200)

        #row 4

        pswd=Label(frame,text="Password",font=("times new roman",10,"bold"),bg="white")
        pswd.place(x=50,y=310)

        self.txt_pswd=ttk.Entry(frame,textvariable=self.var_pswd,font=("times new roman",10,"bold"))
        self.txt_pswd.place(x=50,y=340,width=200)

        confirm_pswd=Label(frame,text="Confirm Password",font=("times new roman",10,"bold"),bg="white")
        confirm_pswd.place(x=300,y=310)

        self.txt_confirm_pswd=ttk.Entry(frame,textvariable=self.var_confirm_pswd,font=("times new roman",10,"bold"))
        self.txt_confirm_pswd.place(x=300,y=340,width=200)

        #checkButton 
        self.var_check=IntVar()
        self.check_btn=Checkbutton(frame,variable=self.var_check,text="I Agree The Terms and Conditions",font=("times new roman",10,"bold"),onvalue=1,offvalue=0)
        self.check_btn.place(x=50,y=380)

        #buttons 
        img=Image.open(r"C:\Users\hp\OneDrive\Desktop\face regonisition system\pictures\Register.jpg")
        img=img.resize((150,40),Image.ANTIALIAS)
        self.photoimage=ImageTk.PhotoImage(img)
        b1=Button(frame,image=self.photoimage,command=self.register_data,borderwidth=0,cursor="hand2")
        b1.place(x=10,y=420,width=300)

        


    #function declaration 
    def register_data(self):
        if self.var_fname.get()=="" or self.var_email.get()=="" or self.var_security_q.get()=="Select":
            messagebox.showerror("Error","All fields are required")
        elif self.var_pswd.get()!=self.var_confirm_pswd.get():
            messagebox.showerror("Error","password and confirm password must be same")
        elif self.var_check.get()==0:
            messagebox.showerror("Error","Agree to our terms and conditions")
        else:
            conn=mysql.connector.connect(host="localhost",user="root",password="shreya8521",database="mydata")
            my_cursor=conn.cursor()
            query=("select * from registerr where email=%s")
            value=(self.var_email.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            if row!=None:
                messagebox.showerror("Error","User already exist")
            else:
                my_cursor.execute("insert into registerr values(%s,%s,%s,%s,%s,%s,%s)",(
                    self.var_fname.get(),
                    self.var_lname.get(),
                    self.var_contact.get(),
                    self.var_email.get(),
                    self.var_security_q.get(),
                    self.var_security_A.get(),
                    self.var_pswd.get()
                ))
            conn.commit()
            conn.close()
            messagebox.showinfo("Success","Registered Successfully")

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

    def open_img(self):
        os.startfile("data")

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

    # def helpdesk_data(self):
    #     self.new_window=Toplevel(self.root)
    #     self.app=HelpDesk(self.new_window)

    def chatbot_data(self):
        self.new_window=Toplevel(self.root)
        self.app=ChatBot(self.new_window)


if __name__ =="__main__":
    main()
