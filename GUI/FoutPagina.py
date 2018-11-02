from tkinter import *
from urllib.request import urlopen
import os

Root = Tk()
Root['background'] = '#ffc917'


def nederlands():
    """deze def stuurt de gebruiker terug van de nederlandse foutpagina naar het nederlandse hoofdmenu"""
    os.system("py NS_projectNL.py")
    Root.destroy()


help(nederlands)
NS_logo = "https://orig00.deviantart.net/0517/f/2018/306/1/e/nslogo_by_xxdragonsartxx-dcr03n1.png"
NS_picture = PhotoImage(data=urlopen(NS_logo).read())
blue = Label(Root, bg="#003082", height=3)
blue.pack(side=BOTTOM, fill="x")
Niet_Beschikbaar = Label(Root, text="Er zijn nog geen kaarten beschikbaar!", bg="#ffc917", fg="#003082",
                         font=("", 50, "bold"))
Niet_Beschikbaar.place(x=75, y=190)
HoofdMenu = Button(Root, command=nederlands, text="Terug", bg="#003082", fg="white", width=20, height=5,
                   font=("", 9, "bold"))
HoofdMenu.place(x=610, y=350)
NS_logo = Label(Root, image=NS_picture, borderwidth=0, height=140, width=340)
NS_logo.place(x=500, y=500)

Root.overrideredirect(True)
Root.geometry("{0}x{1}+0+0".format(Root.winfo_screenwidth(), Root.winfo_screenheight()))
Root.bind("<Escape>", lambda e: Root.destroy())

Root.mainloop()
