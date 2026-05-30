#from tkinter import*
import random
import os
import shutil


com="";ent="...";fix=False;rr=[];rg="";el=0
def cr(d):
    if not os.path.exists(d):
        print("!!--FF:",d)
        print("Reajustando...",d)
        with open("base.txt", "r",encoding='utf-8') as reg:
            r=reg.read().replace(d,"").replace("\n\n","\n")
        with open("base.txt", "w",encoding='utf-8') as reg:
            reg.write(r)
        return False
    else:
        print("!!--:TT",d)
        print("El directorio ya existe")
        return True
def op(d):
   if     d.count("https://")>0:os.system("xdg-open "+d)
   elif   d.count(".")>0:os.system("xdg-open "+d)
   elif   d.count("/")>0:
    if cr(d):
        try:
                os.mkdir(d+"/boul")
                print("Directorio creado exitosamente")
        except FileExistsError:
                print("El directorio ya existe")
        m=os.listdir((d+"/boul").replace("//","/"))
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
                shutil.move((d+"/"+m[x]).replace("//","/"),(d+"/boul"+"/"+m[x]).replace("//","/"))
            y+=1
        print("!!--:",(d+"/boul").replace("//","/"))
        os.system("xdg-open "+(d+"/boul").replace("//","/"))
        global rg;rg=d
with open("base.txt", "r",encoding='utf-8') as reg:
    rr=reg.readlines()
    ir=[]
    while len(rr)>0:
        el=random.randint(0, len(rr)-1)
        ir.append(rr[el].replace("\n",""))
        rr.remove(rr[el])
    rl=ir
    rr=rl

el=-1;liss=str(rr)
while com!="x":
    for d in rr:
        if   d.count("https://")==0 and d.count(".")==0:
            try:
                print("...")
            except FileExistsError:
                print("El directorio ya existe")
                m=os.listdir((d+"/boul").replace("//","/"))
                for i in m:
                    shutil.move(d+"/boul"+"/"+i, d+"/"+i)
    pan="""
{
"""+liss+"""
}
[x]AlizFaraon
 +--------+------
 |[r]:ruta|{"""+ent+"""}
 +--------+------
 |[g]:bucar
 |[s]:randomisar
 |[f]:filtrar
	"""
    print(pan,el,"/",len(rr))
    liss=str(rr)
    com=input("ELIGE: ")
    #m=os.listdir("boul")
    #for i in m:
    #    print(i,":",rg)
    #    if i!=".comments" and i.count("html")==0:
    #        shutil.move(("boul"+"/"+i).replace("//","/"), (rg+"/"+i).replace("//","/"))
    rg=""
    if   com=="r":
        ent=input("Donde: ").replace(" ","")
    if   com=="f":
        ojo=input("Cuales: ")
        liss=""
        for i in rr:
            if i.count(ojo):liss+=i+"\n"
        print(liss)
        com=input("[QUIERES BUSCAR(g)]")
        if com=="g":
            ll=liss.split("\n")
            if ojo!="":rr=ll
            else: rr=rl
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
            rl=ir
            rr=rl
        el=0
    elif com=="g":
        if ent!="...":op(ent)
        ai=True
        for i in rr:
            if i==ent:ai=False;break
        if ai:
            com=input("¿Lo registramos?(g): ")
            if com=="g":
                with open("base.txt", "a",encoding='utf-8') as reg:
                    reg.write("\n"+ent)
                    print("-->Nueva ruata wardada<--")
                rr.append(ent)
        
        if len(rr):
            el+=1
            if el>=len(rr):el=0
            ent=rr[el]
            
