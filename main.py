from tkinter import *
import tkinter.messagebox
import mysql.connector
from PIL import Image

root=Tk()
root.title("MobiExpert")
w,h=root.winfo_screenwidth(),root.winfo_screenheight()

root.geometry("%dx%d+0+0"%(w,h))
root.resizable(0,0)

mydb=mysql.connector.connect(host="localhost",user="root",passwd="",database="MobiExpert")

mycursor=mydb.cursor()

background_image=PhotoImage(file="Resources/bg5.png")

bg=Label(root,image=background_image)
bg.place(x=0,y=0,relwidth=1,relheight=1)

login_frame=Frame(root,bg="white")
login_frame.grid(row=0,column=0,padx=575,pady=300,ipadx=10,ipady=10)
#login_frame.pack(fill=Y)
 
def ml():
	frame3.destroy()
	print(10-ans1.get())
	print(10-ans2.get())
	print(10-ans3.get())

def ques1():
	 login_frame.destroy()
	 global frame1
	 frame1=Frame(root,bg="white")
	 global ans1
	 ans1=IntVar()
	 frame1.grid(row=0,column=0,padx=500,pady=250,ipadx=10,ipady=10)
	 l6=Label(frame1,text="\n\tHow much will you prefer to use your mobile phone for Gaming ?\n\n\t",bg="white").grid(row=0,column=0)
	 r1=Radiobutton(frame1,text="Strongly Prefered",bg="white",variable=ans1,value=1,command=ques2,padx=5,pady=10).grid(row=1,column=0)
	 r2=Radiobutton(frame1,text="Moderately Prefered",bg="white",variable=ans1,value=2,command=ques2,padx=5,pady=10).grid(row=2,column=0)
	 r3=Radiobutton(frame1,text="Weakely Prefered",bg="white",variable=ans1,value=3,command=ques2,padx=5,pady=10).grid(row=3,column=0)
	 r4=Radiobutton(frame1,text="Less Prefered",bg="white",variable=ans1,value=4,command=ques2,padx=5,pady=10).grid(row=4,column=0)
	 r5=Radiobutton(frame1,text="Not Prefered",bg="white",variable=ans1,value=5,command=ques2,padx=5,pady=10).grid(row=5,column=0)

def ques2():
	frame1.destroy()
	global frame2
	frame2=Frame(root,bg="white")
	global ans2
	ans2=IntVar()
	frame2.grid(row=0,column=0,padx=450,pady=300,ipadx=10,ipady=10)
	l7=Label(frame2,text="\n\tHow much will you prefer to use your mobile phone for Watching Movies or Videos ?\n\n\t",bg="white").grid(row=0,column=0)
	r6=Radiobutton(frame2,text="Strongly Prefered",bg="white",variable=ans2,command=ques3,value=1,padx=5,pady=10).grid(row=1,column=0)
	r7=Radiobutton(frame2,text="Moderately Prefered",bg="white",variable=ans2,command=ques3,value=2,padx=5,pady=10).grid(row=2,column=0)
	r8=Radiobutton(frame2,text="Weakely Prefered",bg="white",variable=ans2,command=ques3,value=3,padx=5,pady=10).grid(row=3,column=0)
	r9=Radiobutton(frame2,text="Less Prefered",bg="white",variable=ans2,command=ques3,value=4,padx=5,pady=10).grid(row=4,column=0)
	r10=Radiobutton(frame2,text="Not Prefered",bg="white",variable=ans2,command=ques3,value=5,padx=5,pady=10).grid(row=5,column=0)

def ques3():
	 frame2.destroy()
	 global frame3
	 frame3=Frame(root,bg="white")
	 global ans3
	 ans3=IntVar()
	 frame3.grid(row=0,column=0,padx=375,pady=300,ipadx=10,ipady=10)
	 l6=Label(frame3,text="\n\tHow much will you prefer to use your mobile phone for Clicking Pictures or making Videos etc. ?\n\n\t",bg="white").grid(row=0,column=0)
	 r1=Radiobutton(frame3,text="Strongly Prefered",bg="white",variable=ans3,value=1,command=ml,padx=5,pady=10).grid(row=1,column=0)
	 r2=Radiobutton(frame3,text="Moderately Prefered",bg="white",variable=ans3,value=2,command=ml,padx=5,pady=10).grid(row=2,column=0)
	 r3=Radiobutton(frame3,text="Weakely Prefered",bg="white",variable=ans3,value=3,command=ml,padx=5,pady=10).grid(row=3,column=0)
	 r4=Radiobutton(frame3,text="Less Prefered",bg="white",variable=ans3,value=4,command=ml,padx=5,pady=10).grid(row=4,column=0)
	 r5=Radiobutton(frame3,text="Not Prefered",bg="white",variable=ans3,value=5,command=ml,padx=5,pady=10).grid(row=5,column=0)


def login():
	mycursor.execute("""Select Password from Users where Name = %s""",(n.get(),))
	result=mycursor.fetchall()
	sqlpass="%s"%(result[0])
	if(sqlpass==p.get()):
		ques1()
	else:
		tkinter.messagebox.showinfo("Error","Wrong Credentials")


n=StringVar()
p=StringVar()


user=PhotoImage("Resources/user.png")
l5=Label(login_frame,image=user)
l5.image=user
l5.grid(row=10,column=0)

l1=Label(login_frame,text="\nLogin with your details..\n",bg="white").grid(row=0,column=1,padx=5,pady=5)
l2=Label(login_frame,text="UserName :",bg="white").grid(row=1,column=0,padx=5,pady=5)
e1=Entry(login_frame,textvariable=n)
e1.grid(row=1,column=1,padx=5,pady=5)
l3=Label(login_frame,text="Password :",bg="white").grid(row=2,column=0,padx=10,pady=10)
e2=Entry(login_frame,show="*",textvariable=p)
e2.grid(row=2,column=1,padx=5,pady=5)
b2=Button(login_frame,text="Login",bg="white",command=login)
b2.grid(row=4,columnspan=2,padx=5,pady=5)
l4=Label(login_frame,text="-------OR-------",bg="white").grid(row=5,columnspan=2,padx=5,pady=5)

def sign_up():
	b2.destroy()
	n=e1.get()
	Label(login_frame,text="Enter Name :",bg="white").grid(row=7,column=0,padx=5,pady=5)
	Entry(login_frame).grid(row=7,column=1)
	Label(login_frame,text="Set Password :",bg="white").grid(row=8,column=0,padx=5,pady=5)
	Entry(login_frame,show="*").grid(row=8,column=1)


b1=Button(login_frame,text="Sign Up",bg="white",command=sign_up).grid(row=9,columnspan=2,padx=5,pady=5)

root.mainloop()