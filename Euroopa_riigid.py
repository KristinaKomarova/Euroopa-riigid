from gtts import gTTS
import os
sonastik={}
riigid=[]
linnad=[]
file=open("riigid_pealinnad.txt",'r')
for line in fil:
    k, v=line.strip().split('-') 
    sonastik[k.strip()]=v.strip()#"Riik":"Pealinn"
    sonastik2[v.strip()]=k.strip()#"Pealinn":"Riik"
    riigid.append(k)
    linnad.append(sonastik[k.strip()])
file.close()
print(sonastik)
#print("Riigid:")
print(riigid)
#print("Pealinnad:")
print(linnad)
n=randit(0,50)
print(riigit)
s=gTTS(text=linnad[0],lang='et',slow=True).save("heli.mp3")
os.system("heli.mp3")



a=input()