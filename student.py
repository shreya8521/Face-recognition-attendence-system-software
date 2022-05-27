from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2

class Student:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Student");

        #vairiables 
        self.var_dep=StringVar()
        self.var_course=StringVar()
        self.var_year=StringVar()
        self.var_semester=StringVar()
        self.var_stu_id=StringVar()
        self.var_stu_name=StringVar()
        self.var_div=StringVar()
        self.var_roll=StringVar()
        self.var_gender=StringVar()
        self.var_dob=StringVar()
        self.var_email=StringVar()
        self.var_phone=StringVar()
        self.var_address=StringVar()
        self.var_teacher=StringVar()

        #firstImage 
        img1=Image.open(r"C:\Users\hp\OneDrive\Desktop\face regonisition system\pictures\studentpy1.png")
        img1=img1.resize((420,150),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        f_label=Label(self.root,image=self.photoimg1)
        f_label.place(x=0,y=0,width=420,height=150)

        #secondImage

        img2=Image.open(r"C:\Users\hp\OneDrive\Desktop\face regonisition system\pictures\studentmiddle.png")
        img2=img2.resize((420,150),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        f_label=Label(self.root,image=self.photoimg2)
        f_label.place(x=420,y=0,width=420,height=150)

        #thirdImage

        img3=Image.open(r"C:\Users\hp\OneDrive\Desktop\face regonisition system\pictures\studentpylast.png")
        img3=img3.resize((440,150),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        f_label=Label(self.root,image=self.photoimg3)
        f_label.place(x=840,y=0,width=440,height=150)

        #bg image

        img4=Image.open(r"C:\Users\hp\OneDrive\Desktop\face regonisition system\pictures\black_light.jpg")
        self.photoimg4=ImageTk.PhotoImage(img4)

        bg_image=Label(self.root,image=self.photoimg4)
        bg_image.place(x=0,y=130,width=1280,height=520)

        title_lbl=Label(bg_image,text="STUDENT MANAGENMENT SYSTEM",font=("times new roman",22,"bold"),bg="#CD7054",fg="white")
        title_lbl.place(x=0,y=0,width=1280,height=20)

        main_frame=Frame(bg_image,bd=2,bg="black")
        main_frame.place(x=5,y=22,width=1260,height=500)

        #left label frame 
        Left_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Details",font=("times new roman",12,"bold"))
        Left_frame.place(x=10,y=10,width=610,height=460)

        #current course
        current_course_frame=LabelFrame(Left_frame,bd=2,bg="white",relief=RIDGE,text="Current course",font=("times new roman",12,"bold"))
        current_course_frame.place(x=5,y=0,width=600,height=120)

        #department

        dep_label=Label(current_course_frame,text="Department",font=("times new roman",12,"bold"),bg="white")
        dep_label.grid(row=0,column=0,padx=10,sticky=W)
        
        dep_combo=ttk.Combobox(current_course_frame,textvariable=self.var_dep,font=("times new roman",12,"bold"),width=20,state="readonly")
        dep_combo["values"]=("Select Department","Computer","IT","Civil","Mechanical")
        dep_combo.current(0)
        dep_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)

        #COurse 
        course_label=Label(current_course_frame,text="Course",font=("times new roman",12,"bold"),bg="white")
        course_label.grid(row=0,column=2,padx=10,sticky=W)
        
        course_combo=ttk.Combobox(current_course_frame,textvariable=self.var_course,font=("times new roman",12,"bold"),width=20,state="readonly")
        course_combo["values"]=("Select Course","FE","SE","TE","BE")
        course_combo.current(0)
        course_combo.grid(row=0,column=3,padx=2,pady=10,sticky=W)

        #year
        year_label=Label(current_course_frame,text="Year",font=("times new roman",12,"bold"),bg="white")
        year_label.grid(row=1,column=0,padx=10,sticky=W)
        
        year_combo=ttk.Combobox(current_course_frame,textvariable=self.var_year,font=("times new roman",12,"bold"),width=20,state="readonly")
        year_combo["values"]=("Select Year","2021-21","2021-22","2022-23","2023-24")
        year_combo.current(0)
        year_combo.grid(row=1,column=1,padx=2,pady=10,sticky=W)

        #semester
        semester_label=Label(current_course_frame,text="Semester",font=("times new roman",12,"bold"),bg="white")
        semester_label.grid(row=1,column=2,padx=10,sticky=W)
        
        search_combo=ttk.Combobox(current_course_frame,textvariable=self.var_semester,font=("times new roman",12,"bold"),width=20,state="readonly")
        search_combo["values"]=("Select Semester","Semester-1","Semester-2")
        search_combo.current(0)
        search_combo.grid(row=1,column=3,padx=2,pady=10,sticky=W)

        #classS student_information 

        class_student_frame=LabelFrame(Left_frame,bd=2,bg="white",relief=RIDGE,text="Class student information",font=("times new roman",12,"bold"))
        class_student_frame.place(x=5,y=140,width=600,height=290)

        #student ID

        student_ID_label=Label(class_student_frame,text="StudentID",font=("times new roman",12,"bold"),bg="white")
        student_ID_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)

        student_ID_entry=ttk.Entry(class_student_frame,textvariable=self.var_stu_id,width=15,font=("times new roman",12,"bold"))
        student_ID_entry.grid(row=0,column=1,padx=10,pady=5,sticky=W)

        #student name

        student_name_label=Label(class_student_frame,text="Student Name",font=("times new roman",12,"bold"),bg="white")
        student_name_label.grid(row=0,column=2,padx=10,pady=5,sticky=W)

        student_name_entry=ttk.Entry(class_student_frame,textvariable=self.var_stu_name,width=15,font=("times new roman",12,"bold"))
        student_name_entry.grid(row=0,column=3,padx=10,pady=5,sticky=W)

        #class_division

        class_div_label=Label(class_student_frame,text="Class Division",font=("times new roman",12,"bold"),bg="white")
        class_div_label.grid(row=1,column=0,padx=10,pady=5,sticky=W)

        class_division_combo=ttk.Combobox(class_student_frame,textvariable=self.var_div,font=("times new roman",12,"bold"),width=13,state="readonly")
        class_division_combo["values"]=("Select","A","B","C")
        class_division_combo.current(0)
        class_division_combo.grid(row=1,column=1,padx=10,pady=5,sticky=W)

        #roll_number

        roll_number_label=Label(class_student_frame,text="Roll Number",font=("times new roman",12,"bold"),bg="white")
        roll_number_label.grid(row=1,column=2,padx=10,pady=5,sticky=W)

        roll_number_entry=ttk.Entry(class_student_frame,textvariable=self.var_roll,width=15,font=("times new roman",12,"bold"))
        roll_number_entry.grid(row=1,column=3,padx=10,pady=5,sticky=W)

        #gender

        gender_label=Label(class_student_frame,text="Gender",font=("times new roman",12,"bold"),bg="white")
        gender_label.grid(row=2,column=0,padx=10,pady=5,sticky=W)

        gender_combo=ttk.Combobox(class_student_frame,textvariable=self.var_gender,font=("times new roman",12,"bold"),width=13,state="readonly")
        gender_combo["values"]=("Select","Male","Female","Other")
        gender_combo.current(0)
        gender_combo.grid(row=2,column=1,padx=10,pady=5,sticky=W)

        #Date of Birth

        DOB_label=Label(class_student_frame,text="DOB",font=("times new roman",12,"bold"),bg="white")
        DOB_label.grid(row=2,column=2,padx=10,pady=5,sticky=W)

        DOB_entry=ttk.Entry(class_student_frame,textvariable=self.var_dob,width=15,font=("times new roman",12,"bold"))
        DOB_entry.grid(row=2,column=3,padx=10,pady=5,sticky=W)

        #Email

        Email_label=Label(class_student_frame,text="Email",font=("times new roman",12,"bold"),bg="white")
        Email_label.grid(row=3,column=0,padx=10,pady=5,sticky=W)

        Email_entry=ttk.Entry(class_student_frame,textvariable=self.var_email,width=15,font=("times new roman",12,"bold"))
        Email_entry.grid(row=3,column=1,padx=10,pady=5,sticky=W)

        #Phone Number

        Phone_Number_label=Label(class_student_frame,text="Phone Number",font=("times new roman",12,"bold"),bg="white")
        Phone_Number_label.grid(row=3,column=2,padx=10,pady=5,sticky=W)

        Phone_Number_entry=ttk.Entry(class_student_frame,textvariable=self.var_phone,width=15,font=("times new roman",12,"bold"))
        Phone_Number_entry.grid(row=3,column=3,padx=10,pady=5,sticky=W)

        #Address

        Adress_label=Label(class_student_frame,text="Address",font=("times new roman",12,"bold"),bg="white")
        Adress_label.grid(row=4,column=0,padx=10,pady=5,sticky=W)

        Address_entry=ttk.Entry(class_student_frame,textvariable=self.var_address,width=15,font=("times new roman",12,"bold"))
        Address_entry.grid(row=4,column=1,padx=10,pady=5,sticky=W)

        #Teacher Name 

        Teacher_name_label=Label(class_student_frame,text="Teacher Name",font=("times new roman",12,"bold"),bg="white")
        Teacher_name_label.grid(row=4,column=2,padx=10,pady=5,sticky=W)

        Teacher_name_entry=ttk.Entry(class_student_frame,textvariable=self.var_teacher,width=15,font=("times new roman",12,"bold"))
        Teacher_name_entry.grid(row=4,column=3,padx=10,pady=5,sticky=W)

        #radio Buttons 
        self.var_radio1=StringVar()
        radiobtn1=ttk.Radiobutton(class_student_frame,variable=self.var_radio1,text="Take Photo Sample",value="Yes")
        radiobtn1.grid(row=6,column=0)

        radiobtn2=ttk.Radiobutton(class_student_frame,variable=self.var_radio1,text="No Photo Sample",value="No")
        radiobtn2.grid(row=6,column=1)
        
        #Button  Frame

        btn_frame=Frame(class_student_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=0,y=200,width=560,height=35)
    
        save_btn=Button(btn_frame,text="Save",command=self.add_data,width="14",font=("times new roman",11,"bold"),bg="#CD7054",fg="white")
        save_btn.grid(row=0,column=0,padx=2)

        update_btn=Button(btn_frame,text="Update",command=self.update_data,width="14",font=("times new roman",11,"bold"),bg="#CD7054",fg="white")
        update_btn.grid(row=0,column=1,padx=2)

        delete_btn=Button(btn_frame,text="Delete",command=self.delete_data,width="14",font=("times new roman",11,"bold"),bg="#CD7054",fg="white")
        delete_btn.grid(row=0,column=2,padx=2)

        reset_btn=Button(btn_frame,text="Reset",command=self.reset_data,width="14",font=("times new roman",11,"bold"),bg="#CD7054",fg="white")
        reset_btn.grid(row=0,column=3,padx=2)

        btn_frame1=Frame(class_student_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame1.place(x=0,y=235,width=560,height=29)

        take_photo_btn=Button(btn_frame1,command=self.generate_datset,text="Take Photo Sample",width="60",font=("times new roman",12,"bold"),bg="#CD7054",fg="white")
        take_photo_btn.grid(row=0,column=0,padx=2)


        #right label frame 
        right_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE)
        right_frame.place(x=630,y=10,width=610,height=460)

        img_right=Image.open(r"C:\Users\hp\OneDrive\Desktop\face regonisition system\pictures\student_details.png")
        img_right=img_right.resize((600,120),Image.ANTIALIAS)
        self.photoimg_right=ImageTk.PhotoImage(img_right)

        f_label=Label(right_frame,image=self.photoimg_right)
        f_label.place(x=5,y=0,width=600,height=120)


        #table frame

        table_frame=Frame(right_frame,bd=2,bg="white",relief=RIDGE)
        table_frame.place(x=5,y=135,width=600,height=300)

        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.student_table=ttk.Treeview(table_frame,columns=("dep","course","year","sem","id","name","div","roll","gender","dob","email","phone","address","teacher","photo"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)


        self.student_table.heading("dep",text="Department")
        self.student_table.heading("course",text="Course")
        self.student_table.heading("year",text="Year")
        self.student_table.heading("sem",text="Semester")
        self.student_table.heading("id",text="StudentId")
        self.student_table.heading("name",text="Name")
        self.student_table.heading("div",text="Division")
        self.student_table.heading("roll",text="Roll No")
        self.student_table.heading("gender",text="Gender")
        self.student_table.heading("dob",text="DOB")
        self.student_table.heading("email",text="Email")
        self.student_table.heading("phone",text="Phone")
        self.student_table.heading("address",text="Address")
        self.student_table.heading("teacher",text="Teacher")
        self.student_table.heading("photo",text="PhotoSampleStatus")
        self.student_table["show"]="headings"

        self.student_table.column("dep",width=100)
        self.student_table.column("course",width=100)
        self.student_table.column("year",width=100)
        self.student_table.column("sem",width=100)
        self.student_table.column("id",width=100)
        self.student_table.column("name",width=100)
        self.student_table.column("roll",width=100)
        self.student_table.column("gender",width=100)
        self.student_table.column("div",width=100)
        self.student_table.column("dob",width=100)
        self.student_table.column("email",width=100)
        self.student_table.column("phone",width=100)
        self.student_table.column("address",width=100)
        self.student_table.column("teacher",width=100)
        self.student_table.column("photo",width=100)




        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()


    #function decration 

    def add_data(self):
        if self.var_dep.get()=="Select Department" or self.var_stu_name.get()=="" or self.var_stu_id.get()=="":
            messagebox.showerror("Error","All Fields are required",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",user="root",password="shreya8521",database="face_recognizer")
                mycursor=conn.cursor()
                mycursor.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                    self.var_dep.get(),
                    self.var_course.get(),
                    self.var_year.get(),
                    self.var_semester.get(),
                    self.var_stu_id.get(),
                    self.var_stu_name.get(),
                    self.var_div.get(),
                    self.var_roll.get(),
                    self.var_gender.get(),
                    self.var_dob.get(),
                    self.var_email.get(),
                    self.var_phone.get(),
                    self.var_address.get(),
                    self.var_teacher.get(),
                    self.var_radio1.get()
                ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","Student details has been successfully added",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)

    #fetch data 
    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",user="root",password="shreya8521",database="face_recognizer")
        mycursor=conn.cursor()
        mycursor.execute("select * from student")
        data=mycursor.fetchall()

        if len(data)!=0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("",END,values=i)
            conn.commit()
        conn.close()

    #get cursor 
    def get_cursor(self,event=""):
        cursor_focus=self.student_table.focus()
        content=self.student_table.item(cursor_focus)
        data=content["values"]


        self.var_dep.set(data[0]),
        self.var_course.set(data[1]),
        self.var_year.set(data[2]),
        self.var_semester.set(data[3]),
        self.var_stu_id.set(data[4]),
        self.var_stu_name.set(data[5]),
        self.var_div.set(data[6]),
        self.var_roll.set(data[7]),
        self.var_gender.set(data[8]),
        self.var_dob.set(data[9]),
        self.var_email.set(data[10]),
        self.var_phone.set(data[11]),
        self.var_address.set(data[12]),
        self.var_teacher.set(data[13]),
        self.var_radio1.set(data[14])

    #update function
    def update_data(self):
        if self.var_dep.get()=="Select Department" or self.var_stu_name.get()=="" or self.var_stu_id.get()=="":
            messagebox.showerror("Error","All Fields are required",parent=self.root)
        else:
            try:
                Update=messagebox.askyesno("Update","Do you want to update this student details",parent=self.root)
                if Update>0:
                    conn=mysql.connector.connect(host="localhost",user="root",password="shreya8521",database="face_recognizer")
                    mycursor=conn.cursor()
                    mycursor.execute("update student set Dep=%s,course=%s,year=%s,Semester=%s,Name=%s,Division=%s,Roll=%s,Gender=%s,Dob=%s,Email=%s,Phone=%s,Address=%s,Teacher=%s,PhotoSample=%s where Student_id=%s",(
                    self.var_dep.get(),
                    self.var_course.get(),
                    self.var_year.get(),
                    self.var_semester.get(),
                    self.var_stu_name.get(),
                    self.var_div.get(),
                    self.var_roll.get(),
                    self.var_gender.get(),
                    self.var_dob.get(),
                    self.var_email.get(),
                    self.var_phone.get(),
                    self.var_address.get(),
                    self.var_teacher.get(),
                    self.var_radio1.get(),
                    self.var_stu_id.get()
                ))

                else:
                    if not Update: 
                        return
                messagebox.showinfo("Success","Student detail successfully updated",parent=self.root)
                conn.commit()
                self.fetch_data()
                conn.close()
            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)
    
    #delete function 
    def delete_data(self):
        if self.var_stu_id.get()=="":
            messagebox.showerror("Error","Student id must be required",parent=self.root)
        else:
            try:
                delete=messagebox.askyesno("Student Delete Page","Do you want to delete this student",parent=self.root)
                if delete>0:
                    conn=mysql.connector.connect(host="localhost",user="root",password="shreya8521",database="face_recognizer")
                    mycursor=conn.cursor()
                    sql="delete from student where Student_id=%s"
                    val=(self.var_stu_id.get(),)
                    mycursor.execute(sql,val)
                else:
                    if not delete:
                        return

                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Delete","Successfully deleted student details",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)

    #reset function 
    def reset_data(self):
        self.var_dep.set("Select Department"),
        self.var_course.set("Select Course"),
        self.var_year.set("Select Year"),
        self.var_semester.set("Select Semester"),
        self.var_stu_id.set(""),
        self.var_stu_name.set(""),
        self.var_div.set("Select"),
        self.var_roll.set(""),
        self.var_gender.set("Select"),
        self.var_dob.set(""),
        self.var_email.set(""),
        self.var_phone.set(""),
        self.var_address.set(""),
        self.var_teacher.set(""),
        self.var_radio1.set("")


    #generate dataset and take photo samples
    def generate_datset(self):
        if self.var_dep.get()=="Select Department" or self.var_stu_name.get()=="" or self.var_stu_id.get()=="":
            messagebox.showerror("Error","All Fields are required",parent=self.root)
        else:
            try:    
                conn=mysql.connector.connect(host="localhost",user="root",password="shreya8521",database="face_recognizer")
                mycursor=conn.cursor()
       
                mycursor.execute("select * from student")
                myresult=mycursor.fetchall()
                id=0
                for x in myresult:
                    id+=1
                mycursor.execute("update student set Dep=%s,course=%s,year=%s,Semester=%s,Name=%s,Division=%s,Roll=%s,Gender=%s,Dob=%s,Email=%s,Phone=%s,Address=%s,Teacher=%s,PhotoSample=%s where Student_id=%s",(
                    self.var_dep.get(),
                    self.var_course.get(),
                    self.var_year.get(),
                    self.var_semester.get(),
                    self.var_stu_name.get(),
                    self.var_div.get(),
                    self.var_roll.get(),
                    self.var_gender.get(),
                    self.var_dob.get(),
                    self.var_email.get(),
                    self.var_phone.get(),
                    self.var_address.get(),
                    self.var_teacher.get(),
                    self.var_radio1.get(),
                    self.var_stu_id.get()==id+1
                ))
                conn.commit()
                self.fetch_data()
                self.reset_data()
                conn.close()

                #load predefined data on face frontals from opne cv 
                
                face_classifier=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
                
                def face_cropped(img):
                    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                    faces=face_classifier.detectMultiScale(gray,1.3,5)
                    #1.3-->Scaling Factor 
                    #5-->Minimum Neighbour 

                    for (x,y,w,h) in faces:
                        face_cropped=img[y:y+h,x:x+w]
                        return face_cropped

                cap=cv2.VideoCapture(0) 
                img_id=0
                while True:
                    ret,my_frame=cap.read()
                    if face_cropped(my_frame) is not None:
                        img_id+=1
                        face=cv2.resize(face_cropped(my_frame),(450,450))
                        face=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
                        file_name_path="data/user."+str(id)+"."+str(img_id)+".jpg"
                        cv2.imwrite(file_name_path,face)
                        cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2)
                        cv2.imshow("Cropped Face",face)

                    if cv2.waitKey(1)==13 or int(img_id)==100:
                        break
                cap.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("Result","Generating data sets completed")
            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)

if __name__ =="__main__":
    root=Tk()
    obj=Student(root)
    root.mainloop()
