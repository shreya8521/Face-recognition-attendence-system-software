from tkinter import*
from tkinter import ttk
from turtle import right, st
from PIL import Image,ImageTk
from cv2 import EMD
from numpy import imag
from pip import main
  
class ChatBot:
    def __init__(self,root):
        self.root=root
        self.root.title("ChatBot")
        self.root.geometry("730x620+0+0")
        self.root.bind('<Return>',self.enter_func)

        main_frame=Frame(self.root,bd=4,bg="powder blue",width=610)
        main_frame.pack()

        img_Chat=Image.open('chat-bot.webp')
        img_Chat=img_Chat.resize((200,70),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img_Chat)

        title_label=Label(main_frame,bd=3,relief=RIDGE,anchor='nw',width=730,compound=LEFT,image=self.photoimg,text="CHAT ME",font=('arial',30,'bold'),fg='green',bg='white')
        title_label.pack(side=TOP)

        self.scroll_y=ttk.Scrollbar(main_frame,orient=VERTICAL)
        self.text=Text(main_frame,width=65,height=20,bd=3,relief=RIDGE,font=('arial',14),yscrollcommand=self.scroll_y.set)
        self.scroll_y.pack(side=RIGHT,fill=Y)
        self.text.pack()

        btn_frame=Frame(self.root,bd=4,bg="white",width=730)
        btn_frame.pack()

        label1=Label(btn_frame,text="TYPE SOMETHING",font=('arial',14,'bold'),fg='green',bg='white')
        label1.grid(row=0,column=0,padx=5,sticky=W)

        self.entry=StringVar()

        self.entry1=ttk.Entry(btn_frame,textvariable=self.entry,width=32,font=('arial',16,'bold'))
        self.entry1.grid(row=0,column=1,padx=5,sticky=W)

        self.send=Button(btn_frame,text="Send",command=self.send,font=('arial',16,'bold'),width=8,bg='green')
        self.send.grid(row=0,column=2,padx=5,sticky=W)

        self.clear=Button(btn_frame,text="Clear Data",command=self.clear,font=('arial',10,'bold'),width=8,bg='red',fg='white')
        self.clear.grid(row=1,column=0,padx=5,sticky=W)

        self.msg=''
        self.label2=Label(btn_frame,text=self.msg,font=('arial',14,'bold'),fg='red',bg='white')
        self.label2.grid(row=1,column=1,padx=5,sticky=W)

    def enter_func(self,event):
        self.send.invoke()
        self.entry.set('')

    def clear(self):
        self.text.delete('1.0',END)
        self.entry.set('')


        

    def send(self):
        send='\t\t\t'+'You: '+self.entry.get()
        self.text.insert(END,'\n'+send)

        self.text.yview(END)

        if(self.entry.get()==""):
            self.msg='Enter some input'
            self.label2.config(text=self.msg,fg='red')
        else:
            self.msg=''
            self.label2.config(text=self.msg,fg='red')

        if(self.entry.get()=='hello'):
            self.text.insert(END,'\n\n'+'Bot: Hi')
        
        elif(self.entry.get()=='hi'):
            self.text.insert(END,'\n\n'+'Bot: Hello')

        elif(self.entry.get()=='How are you?'):
                self.text.insert(END,'\n\n'+'Bot: Fine what about you')

        elif(self.entry.get()=='Fantastic'):
            self.text.insert(END,'\n\n'+'Bot: Nice to hear that')

        elif(self.entry.get()=='Who created you'):
            self.text.insert(END,'\n\n'+'Bot: Shreya')

        elif(self.entry.get()=='What is your name'):
            self.text.insert(END,'\n\n'+'Bot:  My name is Zen') 

        elif(self.entry.get()=='bye'):
            self.text.insert(END,'\n\n'+'Bot: Thanks,have a nice day ahead')

        elif(self.entry.get()=='What is a ChatBot?'):
            self.text.insert(END,'\n\n'+'Bot: a computer program designed \nto simulate conversation with human\n users, especially over the internet.')

        else:
            self.text.insert(END,'\n\n'+'Bot: Sorry I did not get it.')


            



        
            
    

if __name__ == '__main__':
    root=Tk()
    obj=ChatBot(root)
    root.mainloop()



    