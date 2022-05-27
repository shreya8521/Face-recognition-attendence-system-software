from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
from cv2 import resize


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

        img1=Image.open(r"C:\Users\hp\OneDrive\Desktop\face regonisition system\pictures\login.webp")
        img1=img1.resize((150,40),Image.ANTIALIAS)
        self.photoimage1=ImageTk.PhotoImage(img1)
        b1=Button(frame,image=self.photoimage1,borderwidth=0,cursor="hand2")
        b1.place(x=330,y=420,width=300)


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








         




      







    


if __name__ =="__main__":
    root=Tk();
    obj=Register(root)
    root.mainloop()
