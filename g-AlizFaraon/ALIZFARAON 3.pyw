from tkinter import*
import random
import os
import shutil

com="";ent="...";fix=False;rr=[];rg=""
def op(d):
   if     d.count("https://")>0:os.system("xdg-open "+d)
   elif   d.count(".txt")>0:
       with open(d, "r",encoding='utf-8') as reg:
        r=reg.readlines()
        x=0
        while x<len(rr):
            rr[x]=rr[x].replace("\n","")
            x+=1
        print("ESCOJIDO => ",r[random.randint(0, len(r)-1)])
   elif   d.count(".exe")>0:os.system("xdg-open "+d)
   elif   d.count("/")>0:
      try:
            os.mkdir(d+"/boul")
            print("Directorio creado exitosamente")
      except FileExistsError:
            print("El directorio ya existe")
      m=os.listdir(d+"/boul")
      for i in m:
            shutil.move(d+"/boul"+"/"+i, d+"/"+i)
      m=os.listdir(d);y=0
      print("ARCHITOS TOTRALES:",len(m)," de>",d)
      while y<len(m)/10:
          m=os.listdir(d)
          if len(m)==0:break
          x=random.randint(0, len(m)-1)
          #print(y,m[x])
          if m[x]!="boul":
            shutil.move(d+"/"+m[x],d+"/boul"+"/"+m[x])
          y+=1
      os.system("xdg-open "+d+"/boul")
      global rg;rg=d
   x=0
   while x<len(rr):
       if rr[x]==d:rr.remove(d);break
       x+=1
           
with open("base.txt", "r",encoding='utf-8') as reg:
    rr=reg.readlines()
    x=0
    while x<len(rr):
        rr[x]=rr[x].replace("\n","")
        x+=1
while com!="x":
    pan="""
{
"""+str(rr)+"""
}
[x]AlizFaraon
 +--------+------
 |[r]:ruta|{"""+ent+"""}
 +--------+------
 |[g]:bucar
 |[e]:explorar
	"""
    print(pan,len(rr))
    com=input("ELIGE: ")
    if rg!="":
        m=os.listdir("boul")
        for i in m:
            print(i,":",rg)
            if i!=".comments" and i.count("html")==0:shutil.move("boul"+"/"+i, rg+"/"+i)
        rg=""
    if   com=="r":
        ent=input("Donde: ")
    elif com=="g":
        if ent!="...":op(ent)
        with open("base.txt", "r",encoding='utf-8') as reg:
                rr=reg.readlines()
                x=0
                while x<len(rr):
                    rr[x]=rr[x].replace("\n","")
                    x+=1
        ai=True
        for i in rr:
            if i.replace("\n","")==ent:ai=False
        if ai:
            with open("base.txt", "a",encoding='utf-8') as reg:
                reg.write("\n"+ent)
                print("-->Nueva ruata wardada<--")
            with open("base.txt", "r",encoding='utf-8') as reg:
                rr=reg.readlines()
                x=0
                while x<len(rr):
                    rr[x]=rr[x].replace("\n","")
                    x+=1
        
        if len(rr):
            x=random.randint(0, len(rr)-1)
            if fix:pass
            else:print(x);ent=rr[x]
    if len(rr)<=2:
        with open("base.txt", "r",encoding='utf-8') as reg:
            rr=reg.readlines()
            x=0
            while x<len(rr):
                rr[x]=rr[x].replace("\n","")
                x+=1
            
