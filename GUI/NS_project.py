from tkinter import *
import os
import webbrowser
from urllib.request import urlopen

Root = Tk()
Root['background'] = '#ffc917'


def pin_url():
    """Verwijst naar de website van www.pin.nl"""
    webbrowser.open_new(r"https://www.pin.nl/consument/historie-pinnen/")


help(pin_url)


def maestro_url():
    """verwijst naar de website van www.maestro.nl"""
    webbrowser.open_new(r"https://www.mastercard.nl/nl-nl/consumers/find-card-products/debit-cards.html")


help(maestro_url)


def startmenu():
    """met deze knop wordt de gebruiker terug gestuurd naar het welkom scherm"""
    os.system('py WelcomeGUI.py')
    Root.destroy()


help(startmenu)


def stationtab_uk():
    """met deze def wordt de gebruiker door gestuurd naar het scherm om een station te zoeken"""
    os.system('py NS_StationTabUK.py')
    Root.destroy()


help(stationtab_uk)


def nl():
    """met deze def wordt de huidige pagina verwijst naar een
    nederlandse versie om de schijn te wekken dat de pagina wordt vertaald"""
    os.system('py NS_projectNL.py')
    Root.destroy()


help(nl)


def errorpage():
    """met deze def wordt de gebruiker door gestuurd
    naar de error pagina voor delen die nog niet functioneel zijn"""
    os.system("py ErrorPage.py")
    Root.destroy()


help(errorpage)
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

Single = Button(Root, text="Single", bg="#003082", fg="white", width=20, height=4, anchor="w", borderwidth=0,
                command=errorpage, font=("", 9, "bold"))
Day_Return = Button(Root, text="Day Return", bg="#003082", fg="white", width=20, height=4, anchor="w", borderwidth=0,
                    command=errorpage, font=("", 9, "bold"))
Return_Ticket = Button(Root, text="5 Return Ticket", bg="#003082", fg="white", width=20, height=4, anchor="w",
                       borderwidth=0, command=errorpage, font=("", 9, "bold"))
Weekend_Return = Button(Root, text="Weekend Return", bg="#003082", fg="white", width=20, height=4, anchor="w",
                        borderwidth=0, command=errorpage, font=("", 9, "bold"))
Railrunner = Button(Root, text="Railrunner\n4-11 (incl) years", justify=LEFT,  bg="#003082", fg="white", width=20,
                    height=4, command=errorpage, anchor="w", borderwidth=0, font=("", 9, "bold"))
Other_Tickets = Button(Root, text="Other Tickets", bg="#003082", fg="white", width=20, height=3, anchor="w",
                       borderwidth=0, command=errorpage, font=("", 9, "bold"))
Via_Station = Button(Root, command=stationtab_uk, text="'Via' Station", bg="#003082", fg="white", width=20, height=3,
                     anchor="w", borderwidth=0, font=("", 9, "bold"))
Nederlands = Button(Root, command=nl, text="Nederlands", image=NL_picture, fg="white", width=45, height=25, borderwidth=1.5)
English = Button(Root, text="English", image=UK_picture, fg="white", width=45, height=25, borderwidth=1.5)
Stop = Button(Root, command=startmenu, text="Stop\nClear all", justify=LEFT, bg="#fe0000", fg="white", width=20,
              height=2, anchor="w", borderwidth=0, font=("", 9, "bold"))
Pinnen = Button(Root, command=pin_url,  image=Pin_picture, width=190, height=120, borderwidth=0)
Maestro = Button(Root, command=maestro_url, image=Maestro_picture, width=190, height=120, borderwidth=0)

Single.place(x=5, y=5)
Day_Return.place(x=5, y=80)
Return_Ticket.place(x=5, y=155)
Weekend_Return.place(x=5, y=230)
Railrunner.place(x=5, y=305)
Other_Tickets.place(x=5, y=660)
Via_Station.place(x=160, y=660)
Nederlands.place(x=20, y=720)
English.place(x=100, y=720)
Stop.place(x=1210, y=725)
Pinnen.place(x=1170, y=10)
Maestro.place(x=1170, y=300)

Pinnen.bind("<Button-1>")
Maestro.bind("<Button-1>")

NLlabel = Label(Root, text="Netherlands", bg="#003082", fg="white", borderwidth=0, font=("", 8, "bold"))
NLlabel.place(x=11, y=751)
UKlabel = Label(Root, text="English", bg="#003082", fg="white", borderwidth=0, font=("", 8, "bold"))
UKlabel.place(x=103, y=751)
NSlabel = Label(Root, image=NSpicture, borderwidth=0, height=140, width=340)
NSlabel.place(x=480, y=260)

Root.overrideredirect(True)
Root.geometry("{0}x{1}+0+0".format(Root.winfo_screenwidth(), Root.winfo_screenheight()))
Root.bind("<Escape>", lambda e: Root.destroy())

Root.mainloop()
