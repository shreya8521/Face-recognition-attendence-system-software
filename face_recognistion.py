from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import tkinter
from time import strftime
from datetime import datetime 
import cv2
import os
import numpy as np

class Face_Recognition:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face_Recognition");

        title_lbl=Label(self.root,text="FACE RECOGNITION",font=("times new roman",32,"bold"),bg="black",fg="white")
        title_lbl.place(x=0,y=0,width=1280,height=45)

    #     #first image

        img_top=Image.open(r"pictures\secondimage.jfif")
        img_top=img_top.resize((600,550),Image.ANTIALIAS)
        self.photoimg_top=ImageTk.PhotoImage(img_top)

        f_label=Label(self.root,image=self.photoimg_top)
        f_label.place(x=0,y=45,width=600,height=550)

    #     #second image 

        img_bottom=Image.open(r"pictures\firstimage.webp")
        img_bottom=img_bottom.resize((700,550),Image.ANTIALIAS)
        self.photoimg_bottom=ImageTk.PhotoImage(img_bottom)

        f_label=Label(self.root,image=self.photoimg_bottom)
        f_label.place(x=600,y=45,width=700,height=550)

        #button

        b1_1=Button(f_label,text="Face Recognition",command=self.face_recog,cursor="hand2",font=("times new roman",17,"bold"),bg="white",fg="red")
        b1_1.place(x=250,y=500,width=200,height=40)


        #attendence 

    def mark_attendence(self,i,r,n,d):
        with open("shreya.csv","r+",newline="\n") as f:
            myDataList=f.readlines()
            name_list=[]
            for line in myDataList:
                entry=line.split((","))
                name_list.append(entry[0])
            if((i not in name_list) and (r not in name_list) and (n not in name_list) and (d not in name_list) ):
                now=datetime.now()
                d1=now.strftime("%d/%m/%Y")
                dtString=now.strftime("%H:%M:%S")
                f.writelines(f"\n{i},{r},{n},{d},{dtString},{d1},Preset")

    #face recognition 

    def face_recog(self):
        def draw_boundary(img,classfier,scaleFactor,minNeighbors,color,text,clf):
            gray_image=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
            features=classfier.detectMultiScale(gray_image,scaleFactor,minNeighbors)

            coord=[]
            for (x,y,w,h) in features:
                cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)
                id,predict=clf.predict(gray_image[y:y+h,x:x+w])
                confidence=int((100*(1-predict/300)))

                conn=mysql.connector.connect(host="localhost",user="root",password="shreya8521",database="face_recognizer")
                mycursor=conn.cursor()

                mycursor.execute("select Name from student where Student_id="+str(id))
                n=mycursor.fetchone()
                n="+".join(n)

                mycursor.execute("select Roll from student where Student_id="+str(id))
                r=mycursor.fetchone()
                r="+".join(r)

                mycursor.execute("select Dep from student where Student_id="+str(id))
                d=mycursor.fetchone()
                d="+".join(d)

                mycursor.execute("select Student_id from student where Student_id="+str(id))
                i=mycursor.fetchone()
                i="+".join(i)

                if confidence>77:
                    cv2.putText(img,f"ID:{i}",(x,y-75),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"Roll:{r}",(x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"Name:{n}",(x,y-30),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"Dep:{d}",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    self.mark_attendence(i,r,n,d)
                else:
                    cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),3)
                    cv2.putText(img,"Unknown Face",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)

                coord=[x,y,w,h]
            return coord
        
        def recognise(img,clf,faceCascade):
            coord=draw_boundary(img,faceCascade,1.1,10,(255,25,255),"Face",clf)
            return img
        
        faceCascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")

        video_cap=cv2.VideoCapture(0)
        while True:
            ret,img=video_cap.read()
            img=recognise(img,clf,faceCascade)
            cv2.imshow("Welcome to face recognition",img)
            
            if cv2.waitKey(1)==13:
                break
        video_cap.release()
        cv2.destroyAllWindows()

if __name__ == "__main__":
    root=Tk()
    obj=Face_Recognition(root)
    root.mainloop()