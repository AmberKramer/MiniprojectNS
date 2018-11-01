import os
import tkinter
top=tkinter.Tk()

def helloCallBack():
    os.system('python GuidosCode.py')

B=tkinter.Button(top,text="hello",command= helloCallBack)
B.pack()
top.mainloop()