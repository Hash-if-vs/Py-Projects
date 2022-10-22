from tkinter import *
import sys
import time
global count
x =0
class stopwatch():
    def reset(self):
        global x
        x=1
        self.t.set('00:00:00')
    def start(self):
        global x
        x=0
        self.timer()
    def resume(self):
        global x
        x=0
        self.timer()
    def pause(self):
        global x
        x=1
    def close(self):
        self.root.destroy()
    def timer(self):
        global x
        if(x==0):
            self.d = str(self.t.get())
            h,m,s = map(int,self.d.split(":"))
            h = int(h)
            m=int(m)
            s= int(s)
            if(s<59):
                s+=1
            elif(s==59):
                s=0
                if(m<59):
                    m+=1
                elif(m==59):
                    m=0
                    h+=1
            if(h<10):
                h = str(0)+str(h)
            else:
                h= str(h)
            if(m<10):
                m = str(0)+str(m)
            else:
                m = str(m)
            if(s<10):
                s=str(0)+str(s)
            else:
                s=str(s)
            self.d=h+":"+m+":"+s
            self.t.set(self.d)
            if(x==0):
                self.root.after(1000,self.timer)
    def __init__(self):
        self.root=Tk()
        self.root.title("Timer")
        self.root.geometry("600x200")
        self.t = StringVar()
        self.t.set("00:00:00")
        self.lb = Label(self.root,textvariable=self.t,font=("Times 45 bold"),bg="white")
        self.bt1 = Button(self.root,text="START",command=self.start,font=("Times 12 bold"),bg=("green"))
        self.bt2 = Button(self.root,text="PAUSE",command=self.pause,font=("Times 12 bold"),bg=("red"))
        self.bt3 = Button(self.root,text="RESET",command=self.reset,font=("Times 12 bold"),bg=("orange"))
        self.bt4 = Button(self.root,text="RESUME",command=self.resume,font=("Times 12 bold"),bg=("yellow"))

        self.lb.place(x=183,y=20)
        self.bt1.place(x=120,y=130)
        self.bt2.place(x=215,y=130)
        self.bt4.place(x=310,y=130)
        self.bt3.place(x=420,y=130)
        self.label = Label(self.root,text="",font=("Times 40 bold"))
        self.root.configure(bg='blue')
        self.root.mainloop()
a=stopwatch()