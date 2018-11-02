from tkinter import *
import os
from urllib.request import urlopen

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

Welkomfoto = "https://img00.deviantart.net/aae2/i/2018/306/3/8/welkomknop_by_xxdragonsartxx-dcr03m8.png"
Welkompicture = PhotoImage(data=urlopen(Welkomfoto).read())
Welkom = Label(Root, text="Welkom", bg='#ffc917', fg="#003082", font=("", 100, "bold"))
Welkomknop = Button(Root, image=Welkompicture, bg="#003082", fg="white", command=english, width=1000, heigh =400)

Welkomknop.place(x=175, y=150)
Welkom.place(x=430, y=5)

Root.overrideredirect(True)
Root.geometry("{0}x{1}+0+0".format(Root.winfo_screenwidth(), Root.winfo_screenheight()))
Root.bind("<Escape>", lambda e: Root.destroy())

Root.mainloop()
