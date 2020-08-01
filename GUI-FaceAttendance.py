from tkinter import *

import os

#creating instance of TK
root = Tk()

root.configure(background = "white")

#root.geometry("300x300")

def function1():
    os.system("/Users/arnavmardia/Library/Preferences/PyCharmCE2018.3/scratches/scratch_12.py")


# title for the window
root.title("Facial recognition attendance system")


#creating a text label
Label(root, text="FACE RECOGNITION ATTENDANCE SYSTEM",font=("times new roman",20),fg="white",bg="maroon",height=2).grid(row=0,rowspan=2,columnspan=2,sticky=N+E+W+S,padx=5,pady=5)

#creating first button
Button(root,text="Create Dataset",font=("times new roman",20),bg="#0D47A1",fg='white',command=function1).grid(row=3,columnspan=2,sticky=W+E+N+S,padx=5,pady=5)