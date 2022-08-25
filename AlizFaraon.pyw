from cProfile import label
from cgitb import text
from distutils.command.config import config
import os
import string
from tkinter import*
#----------------------------------------
import webbrowser as wb
import random
from io import open
#-----------------------------------------------------------------------
reg=open("base.txt", "r")
r=reg.readlines()
mmm=r[0].split("|")
reg.close()

def buscar():
    lu=os.listdir('D:/biblioteca')
    print(lu)
def explorar():
    os.system('explorer')
def abrir():
    os.startfile(entra.get())
def opene():
    wb.open_new(r'C:\Users\Tinti\OneDrive\Documentos\MEGA\MEGAsync\prollectos\lienso\20210412_203617.xcf')
def tellme():
    x = random.randint(0, 3)
def dame1():
    ccc.set(1)
    #ma = entra.get()
    if entra.get() == "":
        reg=open("base.txt", "r")
        r=reg.readlines()
        mmm=r[0].split("|")
        entra.set(mmm[0])
        reg.close()
    
    
    lu=os.listdir(entra.get())
    print(">>>>",lu)
    m = len(lu)
    x = random.randint(0, m)
    print(x, "/", m)
    psa.set(entra.get() + "\\"+ lu[x])
    wb.open_new(entra.get() + "\\"+ lu[x])
def regres1():
    wb.open_new(psa.get())
def delete():
    entra.set("")
    e1.set("")
    e2.set("")
    e3.set("")
def s0():
    reg=open("base.txt", "r")
    r=reg.readlines()
    reg.close()
    reg=open("base.txt", "w")
    r[1]=str(-1)
    reg.write(r[0] + r[1]+"\n"+r[2])
def AU():
    if nn.get() < 60:
       nn.set(nn.get()+1)
    num.config(fg="#ffff00")
def MI():
    if nn.get() <= 0:
       nn.set(60)
    nn.set(nn.get()-1)
def barios():
    while nn.get() > 0:
        dame1()
        nn.set(nn.get()-1)
        print(nn.get())
    num.config(fg="#00ff00")
def soloS1():
    if entra.get() == "":
        dame1()
    lu=os.listdir(entra.get())
    print(">>>>",lu)
    m = len(lu)
    reg=open("base.txt", "r")
    r=reg.readlines()
    na.set(int(r[1]))
    reg.close()
    if na.get() <= 0:
        na.set(m)
    x = random.randint(0, na.get())
    print(x, "/", m)
    wb.open_new(entra.get() + "\\"+ lu[x])
    psa.set(lu[x])
    na.set(na.get()-1)

    reg=open("base.txt", "r")
    r=reg.readlines()
    reg.close()
    reg=open("base.txt", "w")
    r[1]=str(na.get())
    reg.write(r[0] + r[1]+"\n"+r[2])
def MPebtere():
    #ma = entra.get()
    if e1.get() == "":
        e1.set(mmm[1])
    if e2.get() == "":
        e2.set(mmm[2])
    if e3.get() == "":
        e3.set(mmm[3])

    if entra.get() == "":
        dame1()
    x = random.randint(0, 3)
    if x == 0:
        entra.set(e1.get())
    if x == 1:
        entra.set(e2.get())
    if x == 2:
        entra.set(e3.get())
    dame1()
def recordar0():
    print()
    reg=open("base.txt", "r")
    r=reg.readlines()
    mmm=r[0].split("|")
    reg.close()
    entra.set(mmm[0])
def recordar1():
    print(1)
    reg=open("base.txt", "r")
    r=reg.readlines()
    mmm=r[0].split("|")
    reg.close()
    entra.set(mmm[1])
def recordar2():
    print(2)
    reg=open("base.txt", "r")
    r=reg.readlines()
    mmm=r[0].split("|")
    reg.close()
    entra.set(mmm[2])
def recordar3():
    print(3)
    reg=open("base.txt", "r")
    r=reg.readlines()
    mmm=r[0].split("|")
    reg.close()
    entra.set(mmm[3])

def PinicioP():
    gm1.place(x="100", y="120")
    cel.place(x="100", y="150")
    so1.place(x="100", y="180")
    ms1.place(x="100", y="210")
    #|+++++o+++|
    ffil.place(x="100", y="50")
    go.place(x="100", y="50")
    borrar.place(x="100", y="50")
    exp.place(x="100", y="50")
    ouu.place(x="100", y="50")
    gmb.place(x="100", y="50")
    maz.place(x="100", y="50")
    mmi.place(x="100", y="50")
    num.place(x="100", y="50")
    gbk.place(x="100", y="50")
    go1.place(x="100", y="50")
    go2.place(x="100", y="50")
    nam.place(x="100", y="50")
    go3.place(x="100", y="50")
    f1.place(x="100", y="50")
    f2.place(x="100", y="50")
    f3.place(x="100", y="50")
def Pdeme1P():
    gm1.place(x="100", y="50")
    cel.place(x="100", y="50")
    so1.place(x="100", y="50")
    ms1.place(x="100", y="50")
    #|+++++o+++|
    ffil.place(x="84", y="100")
    go.place(x="210", y="98")
    borrar.place(x="160", y="130")
    exp.place(x="90", y="130")
    ouu.place(x="160", y="170")
    gbk.place(x="90", y="170")

    gmb.place(x="4", y="315")
def PlistarP():
    ffil.place(x="84", y="150")
    gmb.place(x="4", y="315")
    maz.place(x="120", y="120")
    mmi.place(x="84", y="120")
    num.place(x="100", y="120")
    go1.place(x="145", y="120")
    ouu.place(x="160", y="170")
    borrar.place(x="90", y="170")
    #|+++++o+++|
    gm1.place(x="100", y="50")
    cel.place(x="100", y="50")
    so1.place(x="100", y="50")
    ms1.place(x="100", y="50")
def Psolo1P():
    gmb.place(x="4", y="315")
    ffil.place(x="84", y="150")
    nam.place(x="100", y="120")
    go2.place(x="145", y="120")
    borrar.place(x="145", y="170")
    ouu.place(x="145", y="200")
    gbk.place(x="90", y="170")
    #|+++++o+++|
    gm1.place(x="100", y="50")
    cel.place(x="100", y="50")
    so1.place(x="100", y="50")
    ms1.place(x="100", y="50")
def P1entreMP():
    gmb.place(x="4", y="315")
    ffil.place(x="84", y="150")
    go3.place(x="145", y="120")
    f1.place(x="84", y="200")
    f2.place(x="84", y="210")
    f3.place(x="84", y="220")
    borrar.place(x="145", y="170")
    exp.place(x="90", y="120")
    gbk.place(x="90", y="170")
    ouu.place(x="160", y="240")
    #|+++++o+++|
    gm1.place(x="100", y="50")
    cel.place(x="100", y="50")
    so1.place(x="100", y="50")
    ms1.place(x="100", y="50")

#---------------------------------------------------------------------
print ("Hello world")
Pan=Tk()
Pan.title("AlizFaraon")
Pan.config(bg="#00aae4")
Pan.geometry("500x350")
Pan.resizable(0,0)#bloquea ono la dimenion
Pan.iconbitmap("perspective-dice-six-faces-random_38559.ico")
#------------------------------------------------------------
In=Frame()
In.pack(side="left", anchor="n")
In.config(bg="#2271b3", width="295", height="345", relief="groove", bd="3")

entra=StringVar()
ffil=Entry(In, textvariable=entra, fg="#00ff00",bg="#000000")
ffil.place(x="100", y="50")
go=Button(In, text="GO>", command=dame1, bg="#ffff00")
go.place(x="100", y="50")
borrar=Button(In, text="  Delete  ", command=delete)
borrar.place(x="100", y="50")
exp=Button(In, text="Explorar", command=explorar)
exp.place(x="100", y="50")
ouu=Button(In, text=" Oupent ", command=abrir)
ouu.place(x="100", y="50")
gbk=Button(In, text=" Go Bak ", command=regres1)
gbk.place(x="100", y="50")
psa=StringVar()


maz=Button(In, text="+", command=AU)
maz.place(x="100", y="50")
mmi=Button(In, text="-", command=MI)
mmi.place(x="100", y="50")
nn=IntVar()
num=Label(In, textvariable=nn, fg="#00ff00",bg="#000000")
num.place(x="100", y="50")
go1=Button(In, text="GO>", command=barios, bg="#ffff00")
go1.place(x="100", y="50")

na=IntVar()
nam=Label(In, textvariable=na, fg="#00ff00",bg="#000000")
nam.place(x="100", y="50")
go2=Button(In, text="GO>", command=soloS1, bg="#ffff00")
go2.place(x="100", y="50")

e1=StringVar()
e2=StringVar()
e3=StringVar()
f1=Entry(In, textvariable=e1, fg="#00ff00",bg="#000000")
f1.place(x="100", y="50")
f2=Entry(In, textvariable=e2, fg="#00ff00",bg="#000000")
f2.place(x="100", y="50")
f3=Entry(In, textvariable=e3, fg="#00ff00",bg="#000000")
f3.place(x="100", y="50")
go3=Button(In, text="GO>", command=MPebtere, bg="#ffff00")
go3.place(x="100", y="50")

gm1=Button(In, text="<--Give me 1-->", command=Pdeme1P,fg="#ff00ff",bg="#00aae4")
gm1.place(x="100", y="120")
cel=Button(In, text="<-----Listar---->", command=PlistarP,fg="#ff00ff",bg="#00aae4")
cel.place(x="100", y="150")
so1=Button(In, text="<----Only 1---->", command=Psolo1P,fg="#ff00ff",bg="#00aae4")
so1.place(x="100", y="180")
ms1=Button(In, text="<---1 in a lot-->", command=P1entreMP,fg="#ff00ff",bg="#00aae4")
ms1.place(x="100", y="210")
gmb=Button(In, text="<GO BAK |||", command=PinicioP)
gmb.place(x="100", y="50")
gmb.config(bg="#ffa500", fg="#ffc0cb",font=("Roman SD",9))

#+++++o+++
ti=Frame()
ti.place(x="50", y="4")
ti.config(bg="#ffffff", width="195", height="80")
A=Button(ti, text="A")
A.place(x="10", y="10")
A.config(bg="#ffff8e", fg="#000000", font=("Roman SD",20))
LI=Button(ti, text="LI")
LI.place(x="70", y="10")
LI.config(bg="#ffff8e", fg="#000000", font=("Roman SD",20))
Z=Button(ti, text="Z")
Z.place(x="130", y="10")
Z.config(bg="#ffff8e", fg="#000000", font=("Roman SD",20))
fa=Label(ti, text="f a r a o n", fg="#ff00ff")
fa.config(bg="#ffffff")
fa.place(x="70", y="60")
#Se=Frame(In)
#Se.place(x="3", y="10")
#Se.config(bg="#00aae4", width="280", height="280", relief="groove", bd="3")
#------------------------------------------------------------
li=Frame()
li.pack(side="right", anchor="n")
li.config(bg="#000000", width="200", height="345")
TiT=Label(li, text="HI HI HI:", fg="#ffff00", font=("Roman SD",12))
TiT.config(bg="#9b9b9b")
TiT.place(x="10", y="10")
b0=Button(li, text="1.",fg="#00ff00",bg="#000000", command = recordar0)
b0.place(x="1", y="40")
c0=Label(li, text=mmm[0], fg="#00ff00",bg="#000000").place(x="20", y="40")
b1=Button(li, text="2.",fg="#00ff00",bg="#000000", command = recordar1).place(x="1", y="60")
c1=Label(li, text=mmm[1], fg="#00ff00",bg="#000000").place(x="20", y="60")
b2=Button(li, text="3.",fg="#00ff00",bg="#000000", command = recordar2).place(x="1", y="80")
c2=Label(li, text=mmm[2], fg="#00ff00",bg="#000000").place(x="20", y="80")
b3=Button(li, text="4.",fg="#00ff00",bg="#000000", command = recordar3).place(x="1", y="100")
c3=Label(li, text=mmm[3], fg="#00ff00",bg="#000000").place(x="20", y="100")
bf=Button(li, text="F.",fg="#00ff00",bg="#000000", command = s0).place(x="1", y="120")
cf=Label(li, text=r[1], fg="#00ff00",bg="#000000").place(x="20", y="120")

ccc = IntVar()
Pan.mainloop()

if ccc.get() == 1:
    reg=open("base.txt", "r")
    r=reg.readlines()
    mmm=r[0].split("|")
    reg.close()
    if entra.get() != mmm[0]:
        reg=open("base.txt", "w")
        jpg = mmm[0]+"|"+mmm[1]+"|"+mmm[2]+"|"+mmm[3]
        reg.write(entra.get()+"|"+jpg+"\n"+r[1]+r[2])
    elif entra.get() == mmm[3]:
        reg=open("base.txt", "w")
        jpg = mmm[0]+"|"+mmm[1]+"|"+mmm[2]+"|"+mmm[3]
        reg.write(entra.get()+"|"+jpg+"\n"+r[1]+r[2])
reg.close()