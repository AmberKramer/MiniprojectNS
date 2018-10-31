from tkinter import *
import os

Root = Tk()


def english():
    """deze def zorgt er voor dat er een nieuwe pagina gemaakt wordt en
    de oude verwijderd zodat er geen overige dingen achterblijven"""
    os.system('py NS_projectNL.py')
    Root.destroy()


help(english)


Root['background'] = '#ffc917'

blue = Label(Root, background="#003082", height=3)
blue.pack(side=BOTTOM, fill="x")

Welkomfoto = PhotoImage(file="C:\\Users\\gfjan\\Pictures\\Welkomknop.png")
Welkom = Label(Root, text="Welkom", bg='#ffc917', fg="#003082", font=("", 100, "bold"))
Welkomknop = Button(Root, image=Welkomfoto, bg="#003082", fg="white", command=english)

Welkomknop.place(x=38, y=150)
Welkom.place(x=382, y=10)

Root.overrideredirect(True)
Root.geometry("{0}x{1}+0+0".format(Root.winfo_screenwidth(), Root.winfo_screenheight()))
Root.bind("<Escape>", lambda e: Root.destroy())

Root.mainloop()
