import requests
import xmltodict
from tkinter import *
import os
import tkinter.messagebox
Root = Tk()
Root['background'] = '#ffc917'


def searching():
    """deze def zorgt ervoor dat de gebruiker een zoekbalk ziet,
    en dat deze gekoppeld is aan de def treintijden, waardoor er daadwerkelijk ook gezocht wordt
    op basis van de invoer van de gebruiker."""
    search = Button(Root, background="#003082", fg="white", text="Zoeken", command=lambda: treintijden(searchbar.get()))
    search.place(x=815, y=202)
    searchbar = Entry(Root, font=("Calibri", 18))
    searchbar.place(x=510, y=200, height=30, width=300)
    searchbar.bind("<Return>", lambda event: treintijden(searchbar.get()))


def treintijden(invoer):
    """door middel van deze def wordt alle gespecificeerde
        informatie opgevraagt uit het xml bestand van de api van de NS,
        als de invoer van de gebruiker niet overeenkomt met de gegevens in de api,
        wordt er een foutmelding weergegeven."""
    label = Label(Root, text="Zoekresultaten voor station: " + invoer, width=70, bg="#ffc917")
    label.place(x=368, y=230)
    auth_details = ('amber.kramer@student.hu.nl', 'vKHIYFtiDBbycMlRcAUsdstrme5Bo4iL76YTBJivyKkio-XWM6QiQA')
    api_url = ('http://webservices.ns.nl/ns-api-avt?station=' + invoer)
    response = requests.get(api_url, auth=auth_details)
    with open('vertrektijden.xml', 'w') as myXMLFile:
        myXMLFile.write(response.text)
    if not actuele_vertrek_informatie():
        Error.place(x=55, y=350)
    else:
        Error.place_forget()


def processxml(filename):
    """deze def opent de xml file, leest de file in,
    en zet de gegevens in een dictionary voor makkelijker gebruik"""
    with open(filename) as myXMLFile:
        filestring = myXMLFile.read()
        xmldictionary = xmltodict.parse(filestring)
        return xmldictionary


def tijd(info):
    """deze def vraagt de vertrektijd op van de dictionary die hier voor is gemaakt
    daarna returned hij deze tijd."""
    vertrektijd = (info['VertrekTijd']).split('T')
    tijdnet = vertrektijd[1].split('+')
    return tijdnet


def bestemming(info):
    """deze def vraagt de eindbestemming op uit de dictionary
    daarna returned hij de eindbestemming"""
    if info['EindBestemming'] is not None:
        eindbestemming = info['EindBestemming']
    else:
        eindbestemming = "'Eindbestemming onbekend'"
    return eindbestemming


def spoor(info):
    """deze def vraagt het spoor op waar de trein van vertrekt uit de gemaakte dictionary
    daarna returned hij het vertrek spoor, als er geen vertrek spoor is
    (als er bijvoorbeeld bussen rijden in plaats van treinen), dan wordt dat opgevangen in de except KeyError.
    >>> spoor({'VertrekSpoor' : {'#text' : 'Utrecht'}})
    'Utrecht'
    """
    try:
        vertrekspoor = (info['VertrekSpoor'])['#text']

    except KeyError:
        vertrekspoor = "'Onbekend'"
    return vertrekspoor


def trein(info):
    """Deze def vraagt op wat voor soort trein het is, een sprinter of een intercity
    maar geeft ook weer als er bussen in plaats van treinen rijden
    >>> trein({'TreinSoort' : 'Intercity' })
    'Intercity'
    """
    if info['TreinSoort'] is not None:
        treintype = info['TreinSoort']
    else:
        treintype = "trein"
    return treintype


def vertraging(info):
    """Deze def geeft de vertragingen weer van treinen die last hebben van een vertraging
    en returned de tijd als er vertraging is.
    Als er geen vertraging is wordt dit opgevangen in de except KeyError
    >>> vertraging ({'VertrekVertragingTekst': '+5 min'})
    ' +5 min'
    """

    try:
        vertragingstijd = " " + info['VertrekVertragingTekst']
    except KeyError:
        vertragingstijd = ""
    return vertragingstijd


def wijziging(info):
    """Deze def geeft aan of er meldingen zijn bijvoorbeeld: trein rijd niet of niet verder dan een bepaald punt,
    als er een extra trein wordt ingezet, of als er een storing is(bijv. sein of wissel storing), etc.
    Als er geen opmerkingen zijn dan wordt dit opgevangen in de except KeyError.
    >>> wijziging({'Opmerkingen': {'Opmerking': 'Trein rijdt niet'}})
    'Let op!: Trein rijdt niet'
    >>> wijziging({'Opmerkingen': {'Opmerking': 'Niet instappen'}})
    'Let op!: Niet instappen'
    >>> wijziging({'Opmerkingen': {'Opmerking': 'Extra trein'}})
    'Let op!: Extra trein'
    """
    try:
        wijzigingen = "Let op!: " + info['Opmerkingen']['Opmerking']
    except KeyError:
        wijzigingen = ""
    return wijzigingen


def on_click(text):
    """Deze def zorgt ervoor dat je een pop-up te zien krijgt,
    met hierin de opmerking die bij deze treinrit hoort."""
    tkinter.messagebox.showinfo("Mededeling", "Let op! " + text)


Tabellen = []


def actuele_vertrek_informatie():
    """Deze def voegt alle relevante informatie samen en
    voegt dit onder elkaar toe in de variabele eindtext.
    Niet elke trein heeft een wijziging of opmerking, dus daarom staat er een regel met een #
    als je de hashtag hiervoor weghaald, voeg je automatisch meerdere regels met opmerkingen toe.
    Dit is vooral handig om de wijzigingsfunctie uit te testen als er geen trajecten met meldingen beschikbaar zijn.
    De KeyError vangt op wanneer de invoer van de gebruiker niet overeenkomt met gegevens in de api,
    en geeft een False waarde door, wat zorgt voor een 'geef een geldig stationsnaam op' melding op het scherm
    (zie treintijden def). Bij de variabele 'regels' hebben we besloten om de regel te splitten op de 'q',
    als we het splitten op de \n dan komt de tweede regel met informatie op het label eronder te staan
    en dat is niet de bedoeling. Omdat de q niet voorkomt in de NS api, kunnen we hem zelf toevoegen waar wij willen,
    in dit geval dus waar de informatie per label moet ophouden.

    """
    for Tabel in Tabellen:
        Tabel.destroy()
    try:
        eindtext = ""
        stationdict = processxml('vertrektijden.xml')
        informatie = stationdict['ActueleVertrekTijden']['VertrekkendeTrein']
        for info in informatie:
            eindtext += ("De {} naar {} \nvertrekt om {}{} vanaf spoor {} {}".format(trein(info), bestemming(info),
                                                                                     ((tijd(info))[0])[0:5],
                                                                                     vertraging(info), spoor(info),
                                                                                     wijziging(info))+'\nq')

#            eindtext+="Dit is een test versie! Let op!: Dit is alleen maar een testq"
        global regels
        regels = eindtext.split('q')
        eindoutput(regels)

        return True
    except KeyError:
        return False


def eindoutput(regels):
    """splits de output van actuele_vertrek_informatie def op in regels,
    zodat per regel gecheckt kan worden of er een melding is
    (en dan een knop aanmaakt die stuurt naar on_click def, die een pop-up weergeeft van de melding).
    Per regel wordt er daarna een label aangemaakt zodat alle informatie netjes op een rijtje komt te staan.
    Verder hebben we de output verdeeld in 3 rijen om zo meer informatie weer te kunnen geven op het scherm.
    """
    aantal = 0
    posx = 250
    posy = 260

    for regel in regels:
        tabel = Label(Root, text=regel, justify=LEFT, anchor='nw', width=35, height=2, font=("",8,"bold"), fg="#003082")
        if "Let op" in regel:
            splitting = regel.split('Let op!:')

            tabel = Label(Root, text=(splitting[0]), justify=LEFT, anchor='nw', width=35, height=2, font=("",8,"bold"),
                          fg="#003082")
            button = tkinter.Button(Root, image=photo, command=lambda text=splitting[1]: on_click(text))
            button.place(x=posx + 220, y=posy + 5)
            Tabellen.append(button)

        tabel.place(x=posx, y=posy)
        posy += 45
        Tabellen.append(tabel)
        aantal += 1
        if aantal == 10:
            posx = 530
            posy = 260
        elif aantal == 20:
            posx = 810
            posy = 260
        elif aantal == 30:
            break


def nederlands():
    """"verwijst de gebruiker terug naar de nederlandse versie van het hoofdmenu
    en verwijdert het huidige scherm, zodat er geen onnodige schermen open blijven staan op de achtergrond"""
    os.system('py NS_projectNL.py')
    Root.destroy()


#NSlogo = PhotoImage(file="C:\\Users\\gfjan\Pictures\\NSlogo.png")
#NSlabel = Label(Root, image=NSlogo, borderwidth=0, height=140, width=340)
#NSlabel.place(x=1000, y=30)
searching()
photo = PhotoImage(file="C:\\Users\\Diana\\Pictures\\OpmerkingenKnop.png")
Label(Root, bg="#ffc917", text="Zoek uw station:").place(x=510, y=175)
blue = Label(Root, background="#003082", height=3)
blue.pack(side=BOTTOM, fill="x")

Error = Label(Root, text="Geef een geldige stationsnaam op!", font=("", 55, "bold"),
              bg="#ffc917", fg="black")

MainMenu = Button(Root, command=nederlands, text="Terug", bg="#003082", fg="white", width=20, height=4, anchor="w",
                  borderwidth=0, font=("", 9, "bold"))
MainMenu.place(x=10, y=10)

Root.overrideredirect(True)
Root.geometry("{0}x{1}+0+0".format(Root.winfo_screenwidth(), Root.winfo_screenheight()))
Root.bind("<Escape>", lambda e: e.widget.quit())

Root.mainloop()
