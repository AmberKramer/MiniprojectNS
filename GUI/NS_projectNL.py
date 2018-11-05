from urllib.request import urlopen
from tkinter import *
import os
import webbrowser

Root = Tk()
Root['background'] = '#ffc917'


def pin_url():
    """Verwijst naar de website van www.pin.nl"""
    webbrowser.open_new(r"https://www.pin.nl/consument/historie-pinnen/")


def maestro_url():
    """verwijst naar de website van www.maestro.nl"""
    webbrowser.open_new(r"https://www.mastercard.nl/nl-nl/consumers/find-card-products/debit-cards.html")


def startmenu():
    """met deze knop wordt de gebruiker terug gestuurd naar het welkom scherm"""
    os.system('py WelcomeGUI.py')
    Root.destroy()


def stationtab():
    """met deze def wordt de gebruiker door gestuurd naar het scherm om een station te zoeken"""
    os.system('py NS_StationTab.py')
    Root.destroy()


def english():
    """deze def verwijst naar de engelse pagina van het systeem"""
    os.system('py NS_project.py')
    Root.destroy()


def foutpagina():
    """met deze def wordt de gebruiker door gestuurd naar de
    fout pagina voor delen die nog niet functioneel zijn"""
    os.system("py FoutPagina.py")
    Root.destroy()


NL = "https://orig00.deviantart.net/ebb8/f/2018/306/8/f/nlflag_by_xxdragonsartxx-dcr03na.gif"
NL_picture = PhotoImage(data=urlopen(NL).read())
UK = "https://orig00.deviantart.net/3403/f/2018/306/b/1/ukflag_by_xxdragonsartxx-dcr03mm.png"
UK_picture = PhotoImage(data=urlopen(UK).read())
PinFoto="https://orig00.deviantart.net/5396/f/2018/306/c/0/pin_by_xxdragonsartxx-dcr03mw.png"
Pin_picture = PhotoImage(data=urlopen(PinFoto).read())
MaestroFoto="https://orig00.deviantart.net/b2d3/f/2018/306/4/f/maestro_by_xxdragonsartxx-dcr03nd.png"
Maestro_picture = PhotoImage(data=urlopen(MaestroFoto).read())
NSlogo="https://orig00.deviantart.net/0517/f/2018/306/1/e/nslogo_by_xxdragonsartxx-dcr03n1.png"
NSpicture = PhotoImage(data=urlopen(NSlogo).read())

blue = Label(Root, background="#003082", height=3)
blue.pack(side=BOTTOM, fill="x")

Enkele_Reis = Button(Root, command=foutpagina, text="Enkele reis", bg="#003082", fg="white", width=20, height=4,
                     anchor="w", borderwidth=0, font=("", 9, "bold"))
Dag_Retour = Button(Root, command=foutpagina, text="Dag retour", bg="#003082", fg="white", width=20, height=4,
                    anchor="w", borderwidth=0, font=("", 9, "bold"))
Retourkaart = Button(Root, command=foutpagina, text="5-Retourkaart", bg="#003082", fg="white", width=20, height=4,
                     anchor="w", borderwidth=0, font=("", 9, "bold"))
Weekendretour = Button(Root, command=foutpagina, text="Weekendretour", bg="#003082", fg="white", width=20, height=4,
                       anchor="w", borderwidth=0, font=("", 9, "bold"))
Railrunner = Button(Root, command=foutpagina, text="Railrunner\n4 t/m 11 jaar", justify=LEFT, bg="#003082",
                    fg="white", width=20, height=4, anchor="w", borderwidth=0, font=("", 9, "bold"))
Overig = Button(Root, command=foutpagina, text="Overige tickets", bg="#003082", fg="white", width=20, height=3,
                anchor="w", borderwidth=0, font=("", 9, "bold"))
Via_Station = Button(Root, command=stationtab, text="'Via' Station", bg="#003082", fg="white", width=20, height=3,
                     anchor="w", borderwidth=0, font=("", 9, "bold"))
Nederlands = Button(Root, text="Nederlands", fg="white", width=45, height=25, borderwidth=1.5, image=NL_picture)
English = Button(Root, command=english, text="English", image=UK_picture, fg="white", width=45, height=25,
                 borderwidth=1.5)
Stop = Button(Root, command=startmenu, text="Stoppen\nAlles wissen", justify=LEFT, bg="#fe0000", fg="white",
              width=20, height=2, anchor="w", borderwidth=0, font=("", 9, "bold"))
Pinnen = Button(Root, command=pin_url, image=Pin_picture, width=190, height=120, borderwidth=0)
Maestro = Button(Root, command=maestro_url, image=Maestro_picture, width=190, height=120, borderwidth=0)

Enkele_Reis.place(x=5, y=5)
Dag_Retour.place(x=5, y=80)
Retourkaart.place(x=5, y=155)
Weekendretour.place(x=5, y=230)
Railrunner.place(x=5, y=305)
Overig.place(x=5, y=660)
Via_Station.place(x=160, y=660)
Nederlands.place(x=20, y=720)
English.place(x=100, y=720)
Stop.place(x=1210, y=725)
Pinnen.place(x=1170, y=10)
Maestro.place(x=1170, y=300)

Pinnen.bind("<Button-1>")
Maestro.bind("<Button-1>")


NLlabel = Label(Root, text="Nederlands", bg="#003082", fg="white", borderwidth=0, font=("", 8, "bold"))
NLlabel.place(x=11, y=751)
UKlabel = Label(Root, text="English", bg="#003082", fg="white", borderwidth=0, font=("", 8, "bold"))
UKlabel.place(x=103, y=751)
NSlabel = Label(Root, image=NSpicture, borderwidth=0, height=140, width=340)
NSlabel.place(x=480, y=260)

Root.overrideredirect(True)
Root.geometry("{0}x{1}+0+0".format(Root.winfo_screenwidth(), Root.winfo_screenheight()))
Root.bind("<Escape>", lambda e: Root.destroy())

Root.mainloop()