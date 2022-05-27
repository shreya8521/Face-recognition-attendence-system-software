from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import numpy as np 

class Training_Data:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Train Data");

        title_lbl=Label(self.root,text="TRAIN DATA SET",font=("times new roman",32,"bold"),bg="black",fg="white")
        title_lbl.place(x=0,y=0,width=1280,height=45)

        img_top=Image.open(r"pictures\train2.png")
        img_top=img_top.resize((1280,250),Image.ANTIALIAS)
        self.photoimg_top=ImageTk.PhotoImage(img_top)

        f_label=Label(self.root,image=self.photoimg_top)
        f_label.place(x=0,y=45,width=1280,height=250)

        
        b1_1=Button(self.root,text="TRAIN DATA",command=self.train_classifier,cursor="hand2",font=("times new roman",17,"bold"),bg="#CD7054",fg="white")
        b1_1.place(x=550,y=295,width=180,height=40)


        img_bottom=Image.open(r"pictures\train1.jpg")
        img_bottom=img_bottom.resize((1280,315),Image.ANTIALIAS)
        self.photoimg_bottom=ImageTk.PhotoImage(img_bottom)

        f_label=Label(self.root,image=self.photoimg_bottom)
        f_label.place(x=0,y=335,width=1280,height=315)

    def train_classifier(self):
        data_dir=("data")
        path=[os.path.join(data_dir,file) for file in os.listdir(data_dir)]


        faces=[]
        ids=[]

        for image in path:
            img=Image.open(image).convert('L')    #Gray Scale image 
            imageNp=np.array(img,'uint8')
            id=int(os.path.split(image)[1].split('.')[1])

            faces.append(imageNp)
            ids.append(id)
            cv2.imshow("Training",imageNp)
            cv2.waitKey(1)==13
        ids=np.array(ids)


        #train the clasiifier and save 
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces,ids)
        clf.write("classifier.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("Result","Training datasets completed")



if __name__ =="__main__":
    root=Tk()
    obj=Training_Data(root)
    root.mainloop()