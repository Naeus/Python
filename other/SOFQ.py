from tkinter import *
import os
import tkinter.messagebox as tm

t=Tk()
t.title('Gym Management')
t["bg"]="black"

#declaration of frame
top=Frame(t)
top.grid(row=0,columnspan=2)
left=Frame(t)
left.grid(row=1,column=0)
right=Frame(t,bg="black")
right.grid(row=1,column=1)

#top frame
l1=Label(top,text="Silver`s Gym",fg="yellow",bg="black",font="impact 50 bold",pady=30)
l1.grid(sticky=E)

#left frame
img1=PhotoImage(file="1.png")
i1=Label(left,image=img1,padx=10)
i1.grid(row=0,column=0,sticky=E)

#right frame
l2=Label(right,text="USERNAME",fg="white",bg="black",padx=10,width=10)
l2.grid(row=0,column=0)
l3=Label(right,text="PASSWORD",fg="white",bg="black",padx=10,width=10)
l3.grid(row=1,column=0)
e2=Entry(right)
e2.grid(row=0,column=1)
e3=Entry(right,show="*")
e3.grid(row=1,column=1)
checkbox = Checkbutton(right, text="Keep me logged in",fg="white",bg="black")
checkbox.grid(columnspan=2)

# defining login button
def login_btn_clickked():
        enter code here`#print("Clicked")
        username = e2.get()
        password = e3.get()

        #print(username, password)

        if username == "john" and password == "password":
            tm.showinfo("Login info", "Welcome John")
        else:
            tm.showerror("Login error", "Incorrect username")
#defining signup button
def sugnup_btn_clickked():
    filename = 'test.py'
    os.system(filename) #Open file [Same as Right-click Open]
    os.system('notepad '+filename)

logbtn = Button(right, text="Login", command = login_btn_clickked,width=15,padx=2)
logbtn.grid(row=3,column=0)
signup = Button(right, text="sign up", command = sugnup_btn_clickked,width=15,padx=2)
signup.grid(row=3,column=1)
t.mainloop()
