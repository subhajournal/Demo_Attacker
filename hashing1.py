import hashlib
import os
import numpy as np
import pandas as pd
import time

def hash_file(filename):
   """"This function returns the SHA-1 hash
   of the file passed into it"""
   # make a hash object
   h = hashlib.sha1()
   # open file for reading in binary mode
   with open(filename,'rb') as file:
       # loop till the end of the file
       chunk = 0
       while chunk != b'':
           # read only 1024 bytes at a time
           chunk = file.read(1024)
           h.update(chunk)
   # return the hex representation of digest
   return h.hexdigest()
dr="E:/As a Freelancer/1. Sphere Consultancy/November/SCNOV001/Rakesh/Solution-2-Virus/1/"
drlst=os.listdir(dr)
print(drlst)
allhash=[]
corrfile=[]
corrdir=[]
allsize=[]
createtime=[]
modtime=[]

for i in range(len(drlst)):
    os.chdir(dr+drlst[i]+"/")
    nowdrlst=os.listdir(dr+drlst[i]+"/")
    for j in nowdrlst:
        if os.path.isdir(dr+drlst[i]+"/"+j)==False:
            allhash.append(hash_file(dr+drlst[i]+"/"+j))
            #statinfo = os.stat(dr+drlst[i]+"/"+j)
            #allsize.append(statinfo.st_size)
            allsize.append(os.path.getsize(dr+drlst[i]+"/"+j))
            corrfile.append(j)
            corrdir.append(drlst[i])
            createtime.append(time.ctime(os.path.getatime(dr+drlst[i]+"/"+j)))
            modtime.append(time.ctime(os.path.getmtime(dr+drlst[i]+"/"+j)))
            
'''print("ALL HASH DATA: \n",allhash)
print("ALL FILE SIZES: \n",allsize)
print("CORRESPONDING FILES: \n",corrfile)
print("CORRESPONDING DIRECTORIES: \n",corrdir)
print("CREATION TIME: \n",createtime)
print("MODIFICATION TIME: \n",modtime)'''

dirdata=pd.DataFrame({
    'HASH':allhash,
    'FILE_SIZE':allsize,
    'FILE':corrfile,
    'DIRECTORY':corrdir,
    'CREATE_TIME':createtime,
    'LAST_MODIFIED':modtime
    })
print(dirdata.head())
dirdata.to_csv(dr[:-2]+"hashdata_after_attack-1.csv")
#message = hash_file("")
#print(message)
