from tkinter import *
import os
import webbrowser

Root = Tk()
Root['background'] = '#ffc917'


def hyperlink():
    webbrowser.open_new(r"https://www.pin.nl/consument/historie-pinnen/")


def hyperlink2():
    webbrowser.open_new(r"https://www.ovshop.nl/product-categorie/ov-chipkaart-opladen/")


def hyperlink3():
    webbrowser.open_new(r"https://www.mastercard.nl/nl-nl/consumers/find-card-products/debit-cards.html")


def mainmenu():
    os.system('py WelcomeGUI.py')
    Root.destroy()


def stationtab():
    os.system('py NS_StationTab.py')
    Root.destroy()


def english():
    os.system('py NS_project.py')
    Root.destroy()


def foutpagina():
    os.system("py FoutPagina.py")
    Root.destroy()


NL = PhotoImage(file="C:\\Users\\gfjan\\Pictures\\flag.png")
UK = PhotoImage(file="C:\\Users\\gfjan\\Pictures\\UK.png")
PinFoto = PhotoImage(file="C:\\Users\\gfjan\Pictures\\pin.png")
MaestroFoto = PhotoImage(file="C:\\Users\\gfjan\Pictures\\Maestro2.png")
NSlogo = PhotoImage(file="C:\\Users\\gfjan\Pictures\\NSlogo.png")

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
Nederlands = Button(Root, text="Nederlands", image=NL, fg="white", width=45, height=25, borderwidth=1.5)
English = Button(Root, command=english, text="English", image=UK, fg="white", width=45, height=25,
                 borderwidth=1.5)
Stop = Button(Root, command=mainmenu, text="Stoppen\nAlles wissen", justify=LEFT, bg="#fe0000", fg="white",
              width=20, height=2, anchor="w", borderwidth=0, font=("", 9, "bold"))
Pinnen = Button(Root, command=hyperlink, image=PinFoto, width=190, height=120, borderwidth=0)
Maestro = Button(Root, command=hyperlink3, image=MaestroFoto, width=190, height=120, borderwidth=0)

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
NSlabel = Label(Root, image=NSlogo, borderwidth=0, height=140, width=340)
NSlabel.place(x=480, y=260)

Root.overrideredirect(True)
Root.geometry("{0}x{1}+0+0".format(Root.winfo_screenwidth(), Root.winfo_screenheight()))
Root.bind("<Escape>", lambda e: Root.destroy())

Root.mainloop()
