import requests
import xmltodict
from tkinter import *
import os
import tkinter.messagebox

Root = Tk()
Root['background'] = '#ffc917'


def treintijden(input):
    """doormiddel van deze def wordt alle gespecificeerde

    >>>label = Label(Root, text="Results for station: " + input, width=70, bg="#ffc917")
    >>>label.place(x=368, y=230)
    informatie opgevraagt uit het xml bestand van de api van de NS"""
    auth_details = ('amber.kramer@student.hu.nl', 'vKHIYFtiDBbycMlRcAUsdstrme5Bo4iL76YTBJivyKkio-XWM6QiQA')
    api_url = ('http://webservices.ns.nl/ns-api-avt?station=' + input)
    response = requests.get(api_url, auth=auth_details)
    with open('vertrektijden.xml', 'w') as myXMLFile:
        myXMLFile.write(response.text)
    if not actuelevertrekinformatie():
        Error.place(x=55, y=350)
    else:
        Error.place_forget()


help(treintijden)


def processxml(filename):
    """deze def opend de xml file, leest de file en zet ze in een dictionairy voor makkelijker gebruik"""
    with open(filename) as myXMLFile:
        filestring = myXMLFile.read()
        xmldictionary = xmltodict.parse(filestring)
        return xmldictionary


help(processxml)


def Tijd(info):
    """deze def vraagt de vertrektijd op van de dictionairy die hier voor is gemaakt"""
    tijd = (info['VertrekTijd']).split('T')
    TijdNet = tijd[1].split('+')
    return TijdNet


help(Tijd)


def bestemming(info):
    """deze def vraagt de eindbestemming op uit de dictionairy"""
    if info['EindBestemming'] is not None:
        bestemming = info['EindBestemming']
    else:
        bestemming = "'Eindbestemming onbekent'"
    return bestemming


help(bestemming)


def Spoor(info):
    """Deze def vraagt het vertrek spoor op waar de trein op komt te staan uit de gemaakte dictionairy"""
    try:
        Spoor = (info['VertrekSpoor'])['#text']

    except KeyError:
        Spoor = "'Onbekend'"
    return Spoor


help(Spoor)


def Trein(info):
    """Deze def vraagt op wat voor soort trein het is, een sprinter of een intercity bijvoorbeeld"""
    if info['TreinSoort'] is not None:
        Trein = info['TreinSoort']
    else:
        Trein = "trein"
    return Trein


help(Trein)


def Vertraging(info):
    """Deze def geeft de vertragingen aan van treinen die last hebben van een vertraging"""
    try:
        Vertraging = " " + info['VertrekVertragingTekst']
    except KeyError:
        Vertraging = ""
    return Vertraging


help(Vertraging)


def Wijziging(info):
    """Deze def geeft aan of er meldingen zijn bijvoorbeeld: trein rijd niet of niet verder dan/ sein storing"""
    try:
        Wijziging = "Let op!: " + info['Opmerkingen']['Opmerking']
    except KeyError:
        Wijziging = ""
    return Wijziging


help(Wijziging)
Tabellen = []


def onclick(text):
    """Deze def maakt een knop aan die er voor zorgt dat er een notificatie
    verschijnt bij de trein waarin de melding komt te staan"""
    tkinter.messagebox.showinfo("Notifications", "Let op! " + text)


help(onclick)


def actuelevertrekinformatie():
    """Deze def geeft de meest relevante informatie over de treinen weer,
    zorgt dat alles in tabellen komen te staan en zorgt
    dat alle defs van hier voor gebruikt worden als duidelijke tekst"""
    for Tabel in Tabellen:
        Tabel.destroy()
    try:
        counting = 0
        EindText = ""
        stationdict = processxml('vertrektijden.xml')
        informatie = stationdict['ActueleVertrekTijden']['VertrekkendeTrein']
        for info in informatie:
            counting += 1
            if counting > 0:

                EindText += ("The {} to {} \ndeparts at {}{} from platform {} {}".format(Trein(info), bestemming(info),
                                                                                         ((Tijd(info))[0])[0:5],
                                                                                         Vertraging(info), Spoor(info),
                                                                                         Wijziging(info))+'\nq')
#            #EindText += "Dit is een test versie! Let op!: Dit is alleen maar een testq"
        regel = EindText.split('q')
        aantal = 0
        posx = 250
        posy = 260

        for r in regel:

            Tabel = Label(Root, text=r, justify=LEFT, anchor='nw', width=35, height=2)
            if "Let op" in r:
                splitting = r.split('Let op!:')
                Tabel = Label(Root, text=(splitting[0]), justify=LEFT, anchor='nw', width=35, height=2)
                button = tkinter.Button(Root, image=WarningLogo,
                                        command=lambda text=splitting[1]: onclick(text))
                button.place(x=posx+220, y=posy+5)
                Tabellen.append(button)
            Tabel.place(x=posx, y=posy)
            posy += 45
            Tabellen.append(Tabel)
            aantal += 1
            if aantal == 10:
                posx = 530
                posy = 260
            if aantal == 20:
                posx = 810
                posy = 260
            if aantal == 30:
                break
        return True
    except KeyError:
        return False


help(actuelevertrekinformatie)


def english():
    """verwijst de gebruiker terug naar de Engelse versie van het hoofdmenu"""
    os.system('py NS_project.py')
    Root.destroy()


help(english)
WarningLogo = PhotoImage(file="C:\\Users\\gfjan\\Pictures\\Warning.png")
NSlogo = PhotoImage(file="C:\\Users\\gfjan\Pictures\\NSlogo.png")
NSlabel = Label(Root, image=NSlogo, borderwidth=0, height=140, width=340)
NSlabel.place(x=1000, y=30)

Label(Root, bg="#ffc917", text="Enter your station:").place(x=510, y=175)
blue = Label(Root, background="#003082", height=3)
blue.pack(side=BOTTOM, fill="x")

Error = Label(Root, text="Enter a valid station!", font=("", 55, "bold"),
              bg="#ffc917", fg="black")

MainMenu = Button(Root, command=english, text="Back", bg="#003082", fg="white", width=20, height=4, anchor="w",
                  borderwidth=0, font=("", 9, "bold"))
MainMenu.place(x=10, y=10)

Search = Button(Root, background="#003082", fg="white", text="Search", command=lambda: treintijden(SearchBar.get()))
Search.place(x=815, y=202)

SearchBar = Entry(Root, font=("Calibri", 18))
SearchBar.place(x=510, y=200, height=30, width=300)
SearchBar.bind("<Return>", lambda event: treintijden(SearchBar.get()))

Root.overrideredirect(True)
Root.geometry("{0}x{1}+0+0".format(Root.winfo_screenwidth(), Root.winfo_screenheight()))
Root.bind("<Escape>", lambda e: e.widget.quit())


Root.mainloop()
