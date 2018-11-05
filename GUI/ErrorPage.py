from tkinter import *
from urllib.request import urlopen
import os

Root = Tk()
Root["background"] = "#ffc917"


def errorpage():
    """deze def stuurt de gebruiker van de engelse foutpagina naar het engelse hoofdmenu"""
    os.system("py NS_project.py")
    Root.destroy()


NS_logo = "https://orig00.deviantart.net/0517/f/2018/306/1/e/nslogo_by_xxdragonsartxx-dcr03n1.png"
NS_picture = PhotoImage(data=urlopen(NS_logo).read())
blue = Label(Root, bg="#003082", height=3)
blue.pack(side=BOTTOM, fill="x")
Not_Available = Label(Root, text="There aren't any tickets available yet!", fg="#003082", bg="#ffc917",
                      font=("", 50, "bold"))
Not_Available.place(x=80, y=190)
MainMenu = Button(Root, command=errorpage, text="Back", fg="white", bg="#003082", width=20, height=5,
                  font=("", 9, "bold"))
MainMenu.place(x=610, y=350)
NS_logo = Label(Root, image=NS_picture, borderwidth=0, height=140, width=340)
NS_logo.place(x=500, y=500)

Root.overrideredirect(True)
Root.geometry("{0}x{1}+0+0".format(Root.winfo_screenwidth(), Root.winfo_screenheight()))
Root.bind("<Escape>", lambda e: Root.destroy())

Root.mainloop()