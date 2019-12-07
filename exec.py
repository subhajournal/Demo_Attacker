import os
from tkinter import *
import pandas as pd
from tkinter import messagebox
import numpy as np

dr="E:/As a Freelancer/1. Sphere Consultancy/November/SCNOV001/Rakesh/Solution-2-Virus/"

alldir=os.listdir(dr)
window = Tk()
window.title("Virus Scanner")
window.geometry('350x200')
lbl = Label(window,text="Virus Checker",font=("Times New Roman Bold",30)).pack()

def secure():
    window = Tk()
    window.title("Virus Scanner")
    window.geometry('350x200')
    lbl = Label(window,text="Remove Virus?",font=("Times New Roman Bold",30)).pack()
    def remov():
        l=os.listdir(dr+"1/")
        os.chdir(dr)
        for i in l:
            present=dr+"1/"+i
            pres_drl=os.listdir(present)
            for file in pres_drl:
                if ".com" in file or ".bat" in file or ".aes" in file:
                    os.remove(present+"/"+file)
        messagebox.showinfo('Message title', 'Virus Removed')
        
    btn = Button(window, text="Remove", command=remov)
    btn.place(x=140,y=100)
    window.mainloop()

def clicked():
    os.system("python hashing.py")
    os.system("python V4.py")
    os.system("python hashing1.py")
    bef=pd.read_csv(dr+"hashdata_before_attack-1.csv")
    aft=pd.read_csv(dr+"hashdata_after_attack-1.csv")
    bef_hash=np.array(bef['HASH'].tolist())
    aft_hash=np.array(aft['HASH'].tolist())
    res=bef_hash==aft_hash
    res_bool=np.unique(res)
    change=res.tolist().count(res_bool[0])
    if change>0:
        secure()

btn = Button(window, text="Check", command=clicked)
btn.place(x=140,y=100)
window.mainloop()




    
