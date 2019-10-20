from tkinter import *
import tkinter.messagebox
import mysql.connector

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

login_frame=Frame(root)
login_frame.grid(row=0,column=0,padx=575,pady=300,ipadx=10,ipady=10)
#login_frame.pack(fill=Y)
 
def login():
	mycursor.execute("""Select Password from Users where Name = %s""",(n.get(),))
	result=mycursor.fetchall()
	sqlpass="%s"%(result[0])
	if(sqlpass==p.get()):
		login_frame.destroy()
	else:
		tkinter.messagebox.showinfo("Error","Wrong Credentials")


n=StringVar()
p=StringVar()


user=PhotoImage("Resources/user.png")
l5=Label(login_frame,image=user)
l5.image=user
l5.grid(row=0,column=0)

l1=Label(login_frame,text="Login with your details..").grid(row=0,column=1,padx=5,pady=5)
l2=Label(login_frame,text="UserName :").grid(row=1,column=0,padx=5,pady=5)
e1=Entry(login_frame,textvariable=n)
e1.grid(row=1,column=1,padx=5,pady=5)
l3=Label(login_frame,text="Password :").grid(row=2,column=0,padx=10,pady=10)
e2=Entry(login_frame,show="*",textvariable=p)
e2.grid(row=2,column=1,padx=5,pady=5)
b2=Button(login_frame,text="Login",command=login)
b2.grid(row=4,columnspan=2,padx=5,pady=5)
l4=Label(login_frame,text="-------OR-------").grid(row=5,columnspan=2,padx=5,pady=5)

def sign_up():
	b2.destroy()
	n=e1.get()
	Label(login_frame,text="Enter Name :").grid(row=7,column=0,padx=5,pady=5)
	Entry(login_frame).grid(row=7,column=1)
	Label(login_frame,text="Set Password :").grid(row=8,column=0,padx=5,pady=5)
	Entry(login_frame,show="*").grid(row=8,column=1)


b1=Button(login_frame,text="Sign Up",command=sign_up).grid(row=9,columnspan=2,padx=5,pady=5)

root.mainloop()