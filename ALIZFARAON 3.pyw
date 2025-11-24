from tkinter import*
import random
import os
import shutil

com="";ent="...";fix=False;rr=[];rg="";el=0
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
    ir=[]
    while len(rr)>0:
        el=random.randint(0, len(rr)-1)
        ir.append(rr[el])
        rr.remove(rr[el])
    rr=ir
el=0;liss=str(rr)
while com!="x":
    pan="""
{
"""+liss+"""
}
[x]AlizFaraon
 +--------+------
 |[r]:ruta|{"""+ent+"""}
 +--------+------
 |[g]:bucar
 |[e]:explorar
 |[s]:randomisar
 |[f]:filtrar
	"""
    print(pan,el,"/",len(rr))
    liss=str(rr)
    com=input("ELIGE: ")
    if rg!="":
        m=os.listdir("boul")
        for i in m:
            print(i,":",rg)
            if i!=".comments" and i.count("html")==0:shutil.move("boul"+"/"+i, rg+"/"+i)
        rg=""
    if   com=="r":
        ent=input("Donde: ")
    if   com=="f":
        ojo=input("Cuales: ")
        liss=""
        for i in rr:
            if i.count(ojo):liss+=i+"\n"
        print(liss)
        com=input("[QUIERES BUSCAR(g)]")
        if com=="g":
            ll=liss.split("\n")
            ent=ll[random.randint(0, len(ll)-1)]   
    elif com=="s":
        with open("base.txt", "r",encoding='utf-8') as reg:
            rr=reg.readlines()
            x=0
            while x<len(rr):
                rr[x]=rr[x].replace("\n","")
                x+=1
            ir=[]
            while len(rr)>0:
                el=random.randint(0, len(rr)-1)
                ir.append(rr[el])
                rr.remove(rr[el])
            rr=ir
        el=0
    elif com=="g":
        if ent!="...":op(ent)
        ai=True
        for i in rr:
            if i.replace("\n","")==ent:ai=False
        if ai:
            with open("base.txt", "a",encoding='utf-8') as reg:
                reg.write("\n"+ent)
                print("-->Nueva ruata wardada<--")
            rr.append(ent)
        
        if len(rr):
            el+=1
            if el>=len(rr):el=0
            if fix:pass
            else:print(x);ent=rr[el]
    if len(rr)<=2:
        with open("base.txt", "r",encoding='utf-8') as reg:
            rr=reg.readlines()
            x=0
            while x<len(rr):
                rr[x]=rr[x].replace("\n","")
                x+=1
            
