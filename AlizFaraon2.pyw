from tkinter import*
import os
import shutil
import random
from datetime import datetime
#----------------------------------------
#py install auto-py-to-exe

mm="";lu="";x=0
reg=open("base.txt", "r",encoding='utf-8')
r=reg.readlines()
reg.close()
try:
    with open("base.txt", "r",encoding='utf-8') as reg:
        r=reg.readlines()
except FileNotFoundError:
    with open("base.txt", "w",encoding='utf-8') as reg:
        reg.write(".../..|.../..|.../..|.../..\n0")
if 0<len(r) and 3<=r[0].count("|") and r[1]!="\n" and r[0]!="":
    mmm=r[0].split("|")
else:
    with open("base.txt", "w",encoding='utf-8') as reg:
        reg.write(".../..|.../..|.../..|.../..\n0")
    with open("base.txt", "r",encoding='utf-8') as reg:
        r=reg.readlines()
def s():
    pass
def see():
    if entra.get()!=""  and 0<entra.get().count("/")  and 0<entra.get().count(".txt"):
        abrir()
        rreg=open(entra.get(), "r",encoding='utf-8')
        rr=rreg.readlines()
        x=random.randint(0, len(rr))
        entra.set(rr[x])
        erow.place(x="0", y="1000")
    else:erow.place(x="55", y="0")
def rde():
    me=os.listdir("boul")
    print(entra.get(),me)
    if len(me)>0:
        for i in me:
            print(x,"/",r[1],"[a ver en grupo]:\t",("boul"+"\\"+i))
            shutil.move("boul"+"\\"+i, entra.get()+"\\"+i)
def ver():
    global lu;global x
    if entra.get()!="" and 0<entra.get().count("/") and 0==entra.get().count(".txt"):
        entra.set(entra.get().replace("\n", ""));r[1]=int(r[1])
        if len(lu)<=1:lu=os.listdir(entra.get())
        if r[1]<=0:r[1]=len(lu)
        if r[1]>len(lu):r[1]=len(lu)
        x = random.randint(0, r[1]-1)
        mu=(entra.get()+"\\"+lu[x])
        rde()
        while cant.get() > 0:
            x = random.randint(0, r[1]-1)
            print(x,"/",r[1],"[a ver en grupo]:\t",(entra.get()+"\\"+lu[x]))
            shutil.move((entra.get()+"\\"+lu[x]), "boul"+"\\"+lu[x])
            mu="boul"
            cant.set(cant.get()-1);lu.remove(lu[x])
            r[1]-=1
            if r[1]<=1:break
        print(x,"/",r[1],"a ver:\t",mu)
        os.startfile(mu)
        lu.remove(lu[x])
        y=random.randint(0, 3);print("intento de cambio a:\t",y)
        if y==0 and ent1.get()!="":entra.set(ent1.get());lu=os.listdir(entra.get());print("cambiado, nuebo lugar:\t",entra.get())
        if y==1 and ent2.get()!="":entra.set(ent2.get());lu=os.listdir(entra.get());print("cambiado, nuebo lugar:\t",entra.get())
        if y==2 and ent3.get()!="":entra.set(ent3.get());lu=os.listdir(entra.get());print("cambiado, nuebo lugar:\t",entra.get())
        if y==3 and ent4.get()!="":entra.set(ent4.get());lu=os.listdir(entra.get());print("cambiado, nuebo lugar:\t",entra.get())
        nn.set(r[1])

        ero.place(x="0", y="1000")
    else:ero.place(x="55", y="0")
def au():
    if cant.get() < 100:
       cant.set(cant.get()+5)
    cc.config(fg="#ffff00")

def mi():
    cant.set(cant.get()-1)
    if cant.get() < 1:cant.set(0)
    
def aut():
    if cantt.get() < 100:
       cantt.set(cantt.get()+10)
    cc.config(fg="#ffff00")
def mit():
    if cantt.get() < 1:
       cantt.set(0)
    cantt.set(cantt.get()-1)
def regres1():
    if len(lu)>=1:os.startfile(entra.get()+ "\\"+lu[x])
def reset():
    global lu;global r
    rde()
    entra.set("")
    ent1.set("")
    ent2.set("")
    ent3.set("")
    ent4.set("")
    cant.set(0)
    nn.set(0)
    lu="";r[1]=0
def explorar():
    os.system('explorer')
def abrir():
    os.startfile(entra.get())

def reint():
    global lu
    rde()
    entra.set("")
    r[1]=0
    cant.set(0)
    lu=""
def relut():
    rde()
    ent1.set("")
    ent2.set("")
    ent3.set("")
    ent4.set("")
def IN():
    rde()
    Exp.place(x="0", y="500")
    Ext.place(x="0", y="500")
    Exw.place(x="0", y="500")
def LOOK():
    Exp.place(x="0", y="100")
def TANOS():
    Ext.place(x="0", y="100")
def PENWO():
    Exw.place(x="0", y="100")
def comp():
    now=datetime.now();global lu;global x
    if entra.get()=="" and entrat.get()!="":entra.set(entrat.get());entrat.set("")
    if entra.get()!="" and entrat.get()==str(now.day)+str(now.month)+str(now.year):got.place(x="200", y="40")
    if entra.get()!="" and cantt.get()>0:
        entra.set(entra.get().replace("\n", ""))
        if len(lu)<=1:lu=os.listdir(entra.get())
        mu="boul"
        rde();ll=int(len(lu)/cantt.get())
        while ll> 0:
            x = random.randint(0, len(lu)-1)
            print(x,"/",ll,"[a ver en grupo]:\t",(entra.get()+"\\"+lu[x]))
            shutil.move((entra.get()+"\\"+lu[x]), "boul"+"\\"+lu[x])
            mu="boul"
            ll-=1;lu.remove(lu[x])
        os.startfile(mu)
        ert.place(x="0", y="1000")
        cantt.set(0)
    else:ert.place(x="55", y="0")  
def vert():
    pass#--------------------------------------------------------------

Pan=Tk()
Pan.title("AlizFaraon")
Pan.config(bg="#00aae4")
Pan.geometry("500x350")
Pan.resizable(0,0)
Pan.iconbitmap("perspective-dice-six-faces-random_38559.ico")
#------ooo--------+
gob=Button(Pan, text="<GO BAK", command=IN, bg="#ffff00").place(x="0", y="300")
sea=Button(Pan, text=" Look a thing ", command=LOOK).place(x="30", y="100")
tan=Button(Pan, text="    Purge list    ", command=TANOS).place(x="30", y="130")
vtp=Button(Pan, text="Random data", command=PENWO).place(x="30", y="160")

Ext=Frame()
Ext.place(x="0", y="500")
Ext.config(bg="#2271b3", width="295", height="145", relief="groove", bd="3")
#------<o>--------+
entra=StringVar();entra.set("");dipur=Label(Ext, textvariabl=entra, fg="#00ff00",bg="#000000");dipur.place(x="165", y="0")
entrat=StringVar();ffilt=Entry(Ext, textvariable=entrat, fg="#00ff00",bg="#000000", insertbackground='#ffffff').place(x="165", y="20")
bet=Button(Ext, text="[SEE]", command=comp, bg="#ffff00").place(x="165", y="40")
got=Button(Ext, text="GO>", command=vert, bg="#ffff00");got.place(x="200", y="500")
ert=Label(Ext, text="<x>", fg="#ff0000",bg="#2271b3");ert.place(x="0", y="1000")
cantt=IntVar();cantt.set(0);cct=Label(Ext, textvariabl=cantt, fg="#00ff00",bg="#000000");cct.place(x="140", y="20")
mazt=Button(Ext, text="+", command=aut).place(x="140", y="0")
mmit=Button(Ext, text="-", command=mit).place(x="140", y="40")
ottt=Button(Ext, text="again (F)", command=reint).place(x="70", y="0")

Exp=Frame()
Exp.place(x="0", y="500")
Exp.config(bg="#2271b3", width="295", height="145", relief="groove", bd="3")
#------<o>--------+
ffil=Entry(Exp, textvariable=entra, fg="#00ff00",bg="#000000", insertbackground='#ffffff').place(x="85", y="3")
go=Button(Exp, text="GO>", command=ver, bg="#ffff00").place(x="210", y="0")
cant=IntVar();cant.set(0);cc=Label(Exp, textvariabl=cant, fg="#00ff00",bg="#000000");cc.place(x="180", y="30")
nn=IntVar();nn.set(r[1]);num=Label(Exp, textvariabl=nn, fg="#000000",bg="#ffffff").place(x="85", y="30")
maz=Button(Exp, text="+", command=au).place(x="205", y="28")
mmi=Button(Exp, text="-", command=mi).place(x="165", y="28")
ott=Button(Exp, text="again (F)", command=reint).place(x="230", y="28")
otl=Button(Exp, text="again [L]", command=relut).place(x="230", y="55")
ero=Label(Exp, text="<x>", fg="#ff0000",bg="#2271b3");ero.place(x="0", y="1000")
borrar=Button(Exp, text="  Delete  ", command=reset).place(x="0", y="0")
exp=Button(Exp, text=" Explore ", command=explorar).place(x="0", y="30")
ouu=Button(Exp, text="Oupent ", command=abrir).place(x="0", y="60")
gbk=Button(Exp, text="Go Back", command=regres1).place(x="0", y="90")
ent1=StringVar();fil1=Entry(Exp, textvariable=ent1, fg="#00ff00",bg="#000000", insertbackground='#ffffff').place(x="85", y="55")
ent2=StringVar();fil2=Entry(Exp, textvariable=ent2, fg="#00ff00",bg="#000000", insertbackground='#ffffff').place(x="85", y="75")
ent3=StringVar();fil3=Entry(Exp, textvariable=ent3, fg="#00ff00",bg="#000000", insertbackground='#ffffff').place(x="85", y="95")
ent4=StringVar();fil4=Entry(Exp, textvariable=ent4, fg="#00ff00",bg="#000000", insertbackground='#ffffff').place(x="85", y="115")

Exw=Frame()
Exw.place(x="0", y="500")
Exw.config(bg="#2271b3", width="295", height="145", relief="groove", bd="3")
#------<o>--------+
ffiw=Entry(Exw, textvariable=entra, fg="#00ff00",bg="#000000", insertbackground='#ffffff').place(x="85", y="3")
gow=Button(Exw, text="GO>", command=see, bg="#ffff00").place(x="210", y="0")
erow=Label(Exw, text="<x>", fg="#ff0000",bg="#2271b3");erow.place(x="0", y="1000")
borrar=Button(Exw, text="  Delete  ", command=reset).place(x="0", y="0")
exp=Button(Exw, text=" Explore ", command=explorar).place(x="0", y="30")
ouu=Button(Exw, text="Oupent ", command=abrir).place(x="0", y="60")
gbk=Button(Exw, text="Go Back", command=regres1).place(x="0", y="90")

tti=Frame()
tti.place(x="50", y="4")
tti.config(bg="#ffffff", width="195", height="80")
#------<o>--------+
A=Button(tti, text="A")
A.place(x="10", y="10")
A.config(bg="#ffff8e", fg="#000000", font=("Roman SD",20))
LI=Button(tti, text="LI")
LI.place(x="70", y="10")
LI.config(bg="#ffff8e", fg="#000000", font=("Roman SD",20))
Z=Button(tti, text="Z")
Z.place(x="130", y="10")
Z.config(bg="#ffff8e", fg="#000000", font=("Roman SD",20))
fa=Label(tti, text="f a r a o n", fg="#ff00ff")
fa.config(bg="#ffffff")
fa.place(x="70", y="60")


li=Frame()
li.pack(side="right", anchor="n")
li.config(bg="#000000", width="200", height="345")
#------<o>--------+
TiT=Label(li, text="HI HI HI:", fg="#ffff00", font=("Roman SD",12))
TiT.config(bg="#9b9b9b")
TiT.place(x="10", y="10")
bf=Button(li, text="F.",fg="#00ff00",bg="#000000", command = s).place(x="1", y="40")
cf=Label(li, text=r[1], fg="#00ff00",bg="#000000").place(x="20", y="40")
lis=Listbox(li, fg="#00ff00", bg="#000000",  width="32", height="17")
lis.pack();lis.place(x="1", y="70")
for i in mmm:lis.insert(END, i)

Pan.mainloop()

rde()
if entra.get()!="" and 0<entra.get().count("/"):
    mm=entra.get().replace("\n", "")
else:mm=entra.set(".../..")
for i in mmm:
    if i==entra.get():mmm.remove(i);mm=i
reg=open("base.txt", "w",encoding='utf-8')
for i in mmm:mm+="|"+i
mm=mm.replace("\n", "")
mm+="\n"+str(r[1])
reg.write(mm)