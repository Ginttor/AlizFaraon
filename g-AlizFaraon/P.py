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

class Pan(Tk):
    def __init__(self):
        super().__init__()
        self.title("AlizFaraon")
        self.config(bg="#00aae4")
        self.geometry("500x350")
        self.resizable(0,0)
        self.iconbitmap("perspective-dice-six-faces-random_38559.ico")
        self.Exp=Frame()
        self.Exp.place(x="0", y="100")
        self.Exp.config(bg="#2271b3", width="297", height="145", relief="groove", bd="3")

        self.tti=Frame()
        self.tti.place(x="50", y="4")
        self.tti.config(bg="#ffffff", width="195", height="80")
        #------<o>--------+
        self.A=Button(self.tti, text="A")
        self.A.place(x="10", y="10")
        self.A.config(bg="#ffff8e", fg="#000000", font=("Roman SD",20))
        self.LI=Button(self.tti, text="LI")
        self.LI.place(x="70", y="10")
        self.LI.config(bg="#ffff8e", fg="#000000", font=("Roman SD",20))
        self.Z=Button(self.tti, text="Z")
        self.Z.place(x="130", y="10")
        self.Z.config(bg="#ffff8e", fg="#000000", font=("Roman SD",20))
        fa=Label(self.tti, text="f a r a o n", fg="#ff00ff")
        fa.config(bg="#ffffff")
        fa.place(x="70", y="60")
        #------<o>--------+
        self.entra=StringVar()
        self.ffil=Entry(self.Exp, textvariable=self.entra, fg="#00ff00",bg="#000000", insertbackground='#ffffff').place(x="85", y="3")
        self.go=Button(self.Exp, text="GO>", command=self.ver, bg="#ffff00").place(x="210", y="0")
        self.cant=IntVar();self.cant.set(0);self.cc=Label(self.Exp, textvariabl=self.cant, fg="#00ff00",bg="#000000");self.cc.place(x="180", y="30")
        self.nn=IntVar();self.nn.set(r[1]);self.num=Label(self.Exp, textvariabl=self.nn, fg="#000000",bg="#ffffff").place(x="85", y="30")
        self.maz=Button(self.Exp, text="+", command=self.au).place(x="205", y="28")
        self.mmi=Button(self.Exp, text="-", command=self.mi).place(x="165", y="28")
        self.ott=Button(self.Exp, text="again (F)", command=s).place(x="230", y="28")
        self.otl=Button(self.Exp, text="again [L]", command=s).place(x="230", y="55")
        self.suitch=BooleanVar()
        self.ots=Checkbutton(self.Exp, text="the part", variable=self.suitch).place(x="230", y="82")
        self.ero=Label(self.Exp, text="<x>", fg="#ff0000",bg="#2271b3");self.ero.place(x="0", y="1000")
        self.borrar=Button(self.Exp, text="  Delete  ", command=s).place(x="0", y="0")
        self.exp=Button(self.Exp, text=" Explore ", command=s).place(x="0", y="30")
        self.ouu=Button(self.Exp, text="Oupent ", command=s).place(x="0", y="60")
        self.gbk=Button(self.Exp, text="Go Back", command=s).place(x="0", y="90")
        self.ent1=StringVar();self.fil1=Entry(self.Exp, textvariable=self.ent1, fg="#00ff00",bg="#000000", insertbackground='#ffffff').place(x="85", y="55")
        self.ent2=StringVar();self.fil2=Entry(self.Exp, textvariable=self.ent2, fg="#00ff00",bg="#000000", insertbackground='#ffffff').place(x="85", y="75")
        self.ent3=StringVar();self.fil3=Entry(self.Exp, textvariable=self.ent3, fg="#00ff00",bg="#000000", insertbackground='#ffffff').place(x="85", y="95")
        self.ent4=StringVar();self.fil4=Entry(self.Exp, textvariable=self.ent4, fg="#00ff00",bg="#000000", insertbackground='#ffffff').place(x="85", y="115")
        #------ooo--------+

        self.li=Frame()
        self.li.pack(side="right", anchor="n")
        self.li.config(bg="#000000", width="200", height="345")
        #------<o>--------+
        self.TiT=Label(self.li, text="HI HI HI:", fg="#ffff00", font=("Roman SD",12))
        self.TiT.config(bg="#9b9b9b")
        self.TiT.place(x="10", y="10")
        self.bf=Button(self.li, text="F.",fg="#00ff00",bg="#000000", command = s).place(x="1", y="40")
        self.cf=Label(self.li, text=r[1], fg="#00ff00",bg="#000000").place(x="20", y="40")
        self.lis=Listbox(self.li, fg="#00ff00", bg="#000000",  width="32", height="17")
        self.lis.pack();self.lis.place(x="1", y="70")
        for i in mmm:self.lis.insert(END, i)

    def ver(self):
        global lu;global x
        if self.entra.get()!="" and 0<self.entra.get().count("/") and 0==self.entra.get().count(".txt"):
            self.entra.set(self.entra.get().replace("\n", ""));r[1]=int(r[1])
            if len(lu)<=1:lu=os.listdir(self.entra.get())
            if r[1]<=0:r[1]=len(lu)
            if r[1]>len(lu):r[1]=len(lu)
            x = random.randint(0, r[1]-1)
            mu=(self.entra.get()+"\\"+lu[x])
            self.rde()
            while self.cant.get() > 0:
                x = random.randint(0, r[1]-1)
                print(x,"/",r[1],"[a ver en grupo]:\t",(self.entra.get()+"\\"+lu[x]))
                shutil.move((self.entra.get()+"\\"+lu[x]), "boul"+"\\"+lu[x])
                mu="boul"
                self.cant.set(self.cant.get()-1);lu.remove(lu[x])
                r[1]-=1
                if r[1]<=1:break
            print(x,"/",r[1],"a ver:\t",mu)
            os.startfile(mu)
            lu.remove(lu[x])
            y=random.randint(0, 3);print("intento de cambio a:\t",y)
            if y==0 and self.ent1.get()!="":self.entra.set(self.ent1.get());lu=os.listdir(self.entra.get());print("cambiado, nuebo lugar:\t",self.entra.get())
            if y==1 and self.ent2.get()!="":self.entra.set(self.ent2.get());lu=os.listdir(self.entra.get());print("cambiado, nuebo lugar:\t",self.entra.get())
            if y==2 and self.ent3.get()!="":self.entra.set(self.ent3.get());lu=os.listdir(self.entra.get());print("cambiado, nuebo lugar:\t",self.entra.get())
            if y==3 and self.ent4.get()!="":self.entra.set(self.ent4.get());lu=os.listdir(self.entra.get());print("cambiado, nuebo lugar:\t",self.entra.get())
            self.nn.set(r[1])

            self.ero.place(x="0", y="1000")
        else:self.ero.place(x="55", y="0")

    def rde(self):
        me=os.listdir("boul")
        print(self.entra.get(),me)
        if len(me)>0:
            for i in me:
                print(x,"/",r[1],"[a ver en grupo]:\t",("boul"+"\\"+i))
                shutil.move("boul"+"\\"+i, self.entra.get()+"\\"+i)

    def au(self):
        if self.cant.get() < 100:
            self.cant.set(self.cant.get()+5)
            self.cc.config(fg="#ffff00")

    def mi(self):
        self.cant.set(self.cant.get()-1)
        if self.cant.get() < 1:self.cant.set(0);self.cc.config(fg="#00ff00")

P = Pan()
P.mainloop()

#rde()
#if entra.get()!="" and 0<entra.get().count("/"):
#    mm=entra.get().replace("\n", "")
#else:mm=entra.set(".../..")
#for i in mmm:
#    if i==entra.get():mmm.remove(i);mm=i
#reg=open("base.txt", "w",encoding='utf-8')
#for i in mmm:mm+="|"+i
#mm=mm.replace("\n", "")
#mm+="\n"+str(r[1])
#reg.write(mm)