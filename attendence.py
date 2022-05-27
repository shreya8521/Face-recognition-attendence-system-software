
from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
from cv2 import EMD
import mysql.connector
import cv2
import os 
import csv
from tkinter import filedialog


mydata=[]
class Attendence:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Attendence")

        #variables 
        self.var_attend_id=StringVar()
        self.var_attend_roll=StringVar()
        self.var_attend_name=StringVar()
        self.var_attend_dep=StringVar()
        self.var_attend_time=StringVar()
        self.var_attend_date=StringVar()
        self.var_attend_attendence=StringVar()
        





        #firstImage 
        img1=Image.open(r"pictures\attend4.jpg")
        img1=img1.resize((640,150),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        f_label=Label(self.root,image=self.photoimg1)
        f_label.place(x=0,y=0,width=640,height=150)

        #secondImage

        img2=Image.open(r"pictures\attend3.webp")
        img2=img2.resize((640,150),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        f_label=Label(self.root,image=self.photoimg2)
        f_label.place(x=640,y=0,width=640,height=150)

        title_lbl=Label(self.root,text="STUDENT MANAGENMENT SYSTEM",font=("times new roman",22,"bold"),bg="black",fg="white")
        title_lbl.place(x=0,y=150,width=1280,height=20)

        main_frame=Frame(self.root,bd=2,bg="black")
        main_frame.place(x=5,y=180,width=1260,height=460)

        #left label frame 
        Left_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Attendence Details",font=("times new roman",12,"bold"))
        Left_frame.place(x=10,y=10,width=610,height=440)

        img_left=Image.open(r"C:\Users\hp\OneDrive\Desktop\face regonisition system\pictures\thirdimage.webp")
        img_left=img_left.resize((600,70),Image.ANTIALIAS)
        self.photoimg_left=ImageTk.PhotoImage(img_left)

        f_label=Label(Left_frame,image=self.photoimg_left)
        f_label.place(x=5,y=0,width=600,height=70)

        left_inside_frame=Frame(Left_frame,bd=2,relief=RIDGE,bg="white")
        left_inside_frame.place(x=5,y=75,width=600,height=330)

        #label and entry 

        #attendenece id 

        attendence_ID_label=Label(left_inside_frame,text="AttendenceID",font=("times new roman",12,"bold"),bg="white")
        attendence_ID_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)

        attendence_ID_entry=ttk.Entry(left_inside_frame,width=15,textvariable=self.var_attend_id,font=("times new roman",12,"bold"))
        attendence_ID_entry.grid(row=0,column=1,padx=10,pady=5,sticky=W)

        # roll

        Roll_label=Label(left_inside_frame,text="Roll",font=("times new roman",12,"bold"),bg="white")
        Roll_label.grid(row=0,column=2,padx=10,pady=5,sticky=W)

        Roll_entry=ttk.Entry(left_inside_frame,width=15,textvariable=self.var_attend_roll,font=("times new roman",12,"bold"))
        Roll_entry.grid(row=0,column=3,padx=10,pady=5,sticky=W)

        #name 
        Name_label=Label(left_inside_frame,text="Name",font=("times new roman",12,"bold"),bg="white")
        Name_label.grid(row=1,column=0,padx=10,pady=5,sticky=W)

        Name_entry=ttk.Entry(left_inside_frame,width=15,textvariable=self.var_attend_name,font=("times new roman",12,"bold"))
        Name_entry.grid(row=1,column=1,padx=10,pady=5,sticky=W)

        #Departement 
        Departement_label=Label(left_inside_frame,text="Department",font=("times new roman",12,"bold"),bg="white")
        Departement_label.grid(row=1,column=2,padx=10,pady=5,sticky=W)

        Departement_entry=ttk.Entry(left_inside_frame,width=15,textvariable=self.var_attend_dep,font=("times new roman",12,"bold"))
        Departement_entry.grid(row=1,column=3,padx=10,pady=5,sticky=W)

        #Time 
        Time_label=Label(left_inside_frame,text="Time",font=("times new roman",12,"bold"),bg="white")
        Time_label.grid(row=2,column=0,padx=10,pady=5,sticky=W)

        Time_entry=ttk.Entry(left_inside_frame,width=15,textvariable=self.var_attend_time,font=("times new roman",12,"bold"))
        Time_entry.grid(row=2,column=1,padx=10,pady=5,sticky=W)

        #Date 
        Date_label=Label(left_inside_frame,text="Date",font=("times new roman",12,"bold"),bg="white")
        Date_label.grid(row=2,column=2,padx=10,pady=5,sticky=W)

        Date_entry=ttk.Entry(left_inside_frame,width=15,textvariable=self.var_attend_date,font=("times new roman",12,"bold"))
        Date_entry.grid(row=2,column=3,padx=10,pady=5,sticky=W)

        #Attendence 
        Attendence_label=Label(left_inside_frame,text="Attendence Status",font=("times new roman",12,"bold"),bg="white")
        Attendence_label.grid(row=3,column=0,padx=10,pady=5,sticky=W)

        Attendence_combo=ttk.Combobox(left_inside_frame,font=("times new roman",12,"bold"),width=13,textvariable=self.var_attend_attendence,state="readonly")
        Attendence_combo["values"]=("Status","Present","Absent")
        Attendence_combo.current(0)
        Attendence_combo.grid(row=3,column=1,padx=10,pady=5,sticky=W)

        btn_frame=Frame(left_inside_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=0,y=280,width=580,height=30)

        save_btn=Button(btn_frame,text="Import csv",command=self.importCsv,width="15",font=("times new roman",11,"bold"),bg="blue",fg="white")
        save_btn.grid(row=0,column=0)

        update_btn=Button(btn_frame,text="Export csv",command=self.exportCsv,width="15",font=("times new roman",11,"bold"),bg="blue",fg="white")
        update_btn.grid(row=0,column=1)

        delete_btn=Button(btn_frame,text="Update",width="15",font=("times new roman",11,"bold"),bg="blue",fg="white")
        delete_btn.grid(row=0,column=2)

        reset_btn=Button(btn_frame,text="Reset",width="15",command=self.reset_data,font=("times new roman",11,"bold"),bg="blue",fg="white")
        reset_btn.grid(row=0,column=3)
    

        #right label frame 
        right_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Attendence Details",font=("times new roman",12,"bold"))
        right_frame.place(x=630,y=10,width=610,height=440)

        table_frame=Frame(right_frame,bd=2,relief=RIDGE,bg="white")
        table_frame.place(x=5,y=5,width=595,height=400)

        #scroll bar table 
        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.AttendenceReportTable=ttk.Treeview(table_frame,column=("id","roll","name","department","time","date","attendence"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.AttendenceReportTable.xview)
        scroll_y.config(command=self.AttendenceReportTable.yview)

        self.AttendenceReportTable.heading("id",text="AttendenceID")
        self.AttendenceReportTable.heading("roll",text="Roll")
        self.AttendenceReportTable.heading("name",text="Name")
        self.AttendenceReportTable.heading("department",text="Department")
        self.AttendenceReportTable.heading("time",text="Time")
        self.AttendenceReportTable.heading("date",text="Date")
        self.AttendenceReportTable.heading("attendence",text="Attendence Status")

        self.AttendenceReportTable["show"]="headings"
        self.AttendenceReportTable.column("id",width=100)
        self.AttendenceReportTable.column("roll",width=100)
        self.AttendenceReportTable.column("name",width=100)
        self.AttendenceReportTable.column("department",width=100)
        self.AttendenceReportTable.column("time",width=100)
        self.AttendenceReportTable.column("date",width=100)
        self.AttendenceReportTable.column("attendence",width=105)

        self.AttendenceReportTable.pack(fill=BOTH,expand=1)
        self.AttendenceReportTable.bind("<ButtonRelease>",self.get_cursor)

        #fetch data 
    
    def fetchData(self,rows):
        self.AttendenceReportTable.delete(*self.AttendenceReportTable.get_children())
        for i in rows:
            self.AttendenceReportTable.insert("",END,values=i)

    #importCSV
    def importCsv(self):
        global mydata
        mydata.clear()
        fln=filedialog.askopenfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*.csv"),("All File","*,*")),parent=self.root)
        with open(fln) as myfile:
            csvread=csv.reader(myfile,delimiter=",")
            for i in csvread:
                mydata.append(i)
            self.fetchData(mydata)

    #export CSV 

    def exportCsv(self):
        try:
            if len(mydata)<1:
                messagebox.showerror("No Data","No Data found to export",parent=self.root)
                return False
            fln=filedialog.asksaveasfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*.csv"),("All File","*,*")),parent=self.root)
            with open(fln,mode="w",newline="") as myfile:
                exp_write=csv.writer(myfile,delimiter=",")
                for i in mydata:
                    exp_write.writerow(i)
                messagebox.showinfo("Data Export","Data Exported to "+os.path.basename(fln)+" successfully")
        except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)

    def get_cursor(self,event=""):
        cursor_row=self.AttendenceReportTable.focus()
        content=self.AttendenceReportTable.item(cursor_row)
        rows=content['values']
        self.var_attend_id.set(rows[0])
        self.var_attend_roll.set(rows[1])
        self.var_attend_name.set(rows[2])
        self.var_attend_dep.set(rows[3])
        self.var_attend_time.set(rows[4])
        self.var_attend_date.set(rows[5])
        self.var_attend_attendence.set(rows[6])

    #reset

    def reset_data(self):
        self.var_attend_id.set("")
        self.var_attend_roll.set("")
        self.var_attend_name.set("")
        self.var_attend_dep.set("")
        self.var_attend_time.set("")
        self.var_attend_date.set("")
        self.var_attend_attendence.set("")

    #update 
    


        

        







              





















if __name__ =="__main__":
    root=Tk()
    obj=Attendence(root)
    root.mainloop()