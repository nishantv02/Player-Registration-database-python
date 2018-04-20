from tkinter import *

import tkinter
top=tkinter.Tk()
count=0

Pid=StringVar()
Pname=StringVar()
age=StringVar()
position=StringVar()
salary=StringVar()

def Add_Vehicle():
    f=open('pythonDB.txt','a')
    Pid=E1.get()
    Pname=E2.get()
    age=E3.get()
    position=E4.get()
    salary=E5.get()
    if(Pid=='' or Pname=='' or  age=='' or position=='' or salary==''):
        print("Details can't be empty!")
        exit()
    f.writelines(Pid.ljust(20)+Pname.ljust(20)+age.ljust(20)+position.ljust(20)+salary.ljust(3)+"\n")
    print("Record added to file!")
    f.close()

def Delete_Vehicle():
    k=Pid.get()
    f=open('pythonDB.txt','r')
    ctr=0
    for line in f:
        ctr=ctr+1
    print("No. of lines in file:")
    print(ctr)
    f.seek(0)
    lines=f.readlines()
    print(lines)
    f.close()
    f=open('pythonDB.txt','w')
    for ve in lines:
        j=ve.split()
        print(j)
        if(j[0]!=k):
            f.writelines(j[0].ljust(20)+j[1].ljust(20)+j[2].ljust(20)+j[3].ljust(20)+j[4].ljust(5)+"\n")
    f.close()

def Search_Vehicle():
    k=Pid.get()
    f=open('pythonDB.txt','r')
    ctr=0
    flag=0
    for line in f:
        ctr=ctr+1
    print("No. of lines in file:")
    print(ctr)
    f.seek(0)
    lines=f.readlines()
    print(lines)
    for book in lines:
        j=book.split()
        if(j[0]==k):
            print(j)
            Pid.set(j[0])
            Pname.set(j[1])
            age.set(j[2])
            position.set(j[3])
            salary.set(j[4])
            flag=1
            break
    if(flag==0):
        print("Record not found!")
    else:
        print("Record found!")
    f.close()

def Update_Vehicle():
    new_Pid=Pid.get()
    new_Pname=Pname.get()
    new_age=age.get()
    new_position=position.get()
    new_salary=salary.get()
    f=open('pythonDB.txt','r')
    ctr=0
    for line in f:
        ctr=ctr+1
    print("No. of lines in file:")
    print(ctr)
    f.seek(0)
    lines=f.readlines()
    f.close()
    f=open('pythonDB.txt','w')
    for vec in lines:
        j=vec.split()
        if(j[0]!=new_Pid):
            f.writelines(j[0].ljust(20)+j[1].ljust(20)+j[2].ljust(20)+j[3].ljust(20)+j[4].ljust(3)+"\n")
        else:
            f.writelines(j[0].ljust(20)+new_Pname.ljust(20)+new_age.ljust(20)+new_position.ljust(20)+new_salary.ljust(3)+"\n")
    print("Record updated!!")
    f.close()

def Get_First_Record():
    global count
    count=1
    f=open('pythonDB.txt','r')
    ctr=0
    flag=0
    for line in f:
        ctr=ctr+1
    print("No. of lines in file:")
    print(ctr)
    f.seek(0)
    lines=f.readlines()
    l=list(lines)
    print("\n")
    print(l)
    j=l[0].split()
    Pid.set(j[0])
    Pname.set(j[1])
    age.set(j[2])
    position.set(j[3])
    salary.set(j[4])
    print("\n First Record of file is as:")
    print(l[0])
    f.close()


def Get_Last_Record():
    f=open('pythonDB.txt','r')
    ctr=0
    flag=0
    for line in f:
        ctr=ctr+1
    print("No. of lines in file:")
    print(ctr)
    f.seek(0)
    lines=f.readlines()
    l=list(lines)
    print(l)
    j=l[ctr-1].split()
    Pid.set(j[0])
    Pname.set(j[1])
    age.set(j[2])
    position.set(j[3])
    salary.set(j[4])
    print("\n Last Record of file is as:")
    print(l[ctr-1])
    f.close()
    global count
    count=ctr-1


def Get_Next_Record():

    global count
    i=0
    ctr=0
    f=open('pythonDB.txt','r')
    for line in f:
        ctr=ctr+1
    print("No. of lines in file:")
    print(ctr)
    f.seek(0)
    try:
        while(i<=count):
            l=f.readline()
            i=i+1
        m=l.split()
        Pid.set(m[0])
        Pname.set(m[1])
        age.set(m[2])
        position.set(m[3])
        salary.set(m[4])
        print(m)
    except:
        Pid.set("")
        Pname.set("")
        age.set("")
        position.set("")
        salary.set("")
        print("Sorry, no more records!")
    count=count+1
    f.close()

def Get_Prev_Record():
    global count
    i=0
    ctr=0
    f=open('pythonDB.txt','r')
    for line in f:
        ctr=ctr+1
    print("No. of lines in file:")
    print(ctr)
    f.seek(0)
    try:
        while(i<=count-1):
            l=f.readline()
            i=i+1
        m=l.split()
        Pid.set(m[0])
        Pname.set(m[1])
        age.set(m[2])
        position.set(m[3])
        salary.set(m[4])
        print(m)
    except:
        Pid.set("")
        Pname.set("")
        age.set("")
        position.set("")
        salary.set("")
        print("Sorry, no more records!")
    count=count-1
    f.close()

tkinter.Label(top, text="Player ID:",font=('Berlin Sans FB',15),bg="cyan").grid(row=0)
tkinter.Label(top, text="Player Name:",font=('Berlin Sans FB',15),bg="cyan").grid(row=1)
tkinter.Label(top, text="Player age:",font=('Berlin Sans FB',15),bg="cyan").grid(row=2)
tkinter.Label(top, text="Player position:",font=('Berlin Sans FB',15),bg="cyan").grid(row=3)
tkinter.Label(top, text="salary:",font=('Berlin Sans FB',15),bg="cyan").grid(row=4)
E1 = tkinter.Entry(top,textvariable=Pid)
E2 = tkinter.Entry(top,textvariable=Pname)
E3 = tkinter.Entry(top,textvariable=age)
E4 = tkinter.Entry(top,textvariable=position)
E5 = tkinter.Entry(top,textvariable=salary)
E1.grid(row=0, column=1)
E2.grid(row=1, column=1)
E3.grid(row=2, column=1)
E4.grid(row=3, column=1)
E5.grid(row=4, column=1)

fr=tkinter.Button(top,text="First",width=15,bg="light salmon",font=('Berlin Sans FB',15 ),command=Get_First_Record).grid(row=5, column=0)
pr=tkinter.Button(top,text="Previous",width=15,bg="light salmon",font=('Berlin Sans FB',15 ),command=Get_Prev_Record).grid(row=5, column=1)
nr=tkinter.Button(top,text="Next",width=15,bg="light salmon",font=('Berlin Sans FB',15 ),command=Get_Next_Record).grid(row=5, column=2)
lr=tkinter.Button(top,text="Last",width=15,bg="light salmon",font=('Berlin Sans FB',15 ),command=Get_Last_Record).grid(row=5, column=3)

rb=tkinter.Button(top,text="ADD",width=15,bg="light salmon",font=('Berlin Sans FB',15 ),command=Add_Vehicle).grid(row=7, column=0)
db=tkinter.Button(top,text="DELETE",width=15,bg="light salmon",font=('Berlin Sans FB',15 ),command=Delete_Vehicle).grid(row=7, column=1)
sb=tkinter.Button(top,text="SEARCH",width=15,bg="light salmon",font=('Berlin Sans FB',15 ),command=Search_Vehicle).grid(row=7, column=2)
ub=tkinter.Button(top,text="UPDATE",width=15,bg="light salmon",font=('Berlin Sans FB',15 ),command=Update_Vehicle).grid(row=7, column=3)
top.configure(bg="light salmon")
canv = Canvas(top,bg = 'powderblue',height = 200,width=200)
canv.grid(row=2,column=2,columnspan=2,rowspan=2)
file = PhotoImage(file = 'bro.png')
img = canv.create_image(102,102,image=file)
top.mainloop()
