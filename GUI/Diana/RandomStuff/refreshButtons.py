from tkinter import *
def deletelabel():
    label2.destroy()
    label=Label(root,text="Plz")
    label.place(x=300, y=400)
def changebutton():
    but.destroy()
    global label2
    label2=Label(root,text="changed")
    label2.place(x=300, y=400)
    deletelabel()
if __name__=='__main__':
    root=Tk()
    global but

    but= Button(root,text="button",command=changebutton)
    but.place(x=100, y=200)
    root.mainloop()
