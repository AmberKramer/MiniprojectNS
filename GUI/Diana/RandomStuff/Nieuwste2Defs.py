import requests
import xmltodict
from tkinter import *
import os
import tkinter.messagebox
Root = Tk()
Root['background'] = '#ffc917'

def searchbar():
    Search = Button(Root, background="#003082", fg="white", text="Zoeken", command=lambda: treintijden(SearchBar.get()))
    Search.place(x=815, y=202)

    SearchBar = Entry(Root, font=("Calibri", 18))
    SearchBar.place(x=510, y=200, height=30, width=300)
    SearchBar.bind("<Return>", lambda event: treintijden(SearchBar.get()))
searchbar()


def treintijden(input):
    label = Label(Root, text="Zoekresultaten voor station: " + input, width=70, bg="#ffc917")
    label.place(x=368, y=230)
    auth_details = ('amber.kramer@student.hu.nl', 'vKHIYFtiDBbycMlRcAUsdstrme5Bo4iL76YTBJivyKkio-XWM6QiQA')
    api_url = ('http://webservices.ns.nl/ns-api-avt?station=' + input)
    response = requests.get(api_url, auth=auth_details)
    with open('vertrektijden.xml', 'w') as myXMLFile:
        myXMLFile.write(response.text)
    if not ActueleVertrekInformatie():
        Error.place(x=55, y=350)
    else:
        Error.place_forget()

def processXML(filename):
    with open(filename) as myXMLFile:
        filestring = myXMLFile.read()
        xmldictionary = xmltodict.parse(filestring)
        return xmldictionary


def Tijd(info):
    tijd = (info['VertrekTijd']).split('T')
    TijdNet = tijd[1].split('+')
    return TijdNet


def Bestemming(info):
    if info['EindBestemming'] is not None:
        Bestemming = info['EindBestemming']
    else:
        Bestemming = "'Eindbestemming onbekent'"
    return Bestemming


def Spoor(info):
    """Dit is
    om meerdere docstrings
    te testen met een doctest hieronder
    >>> Spoor({'VertrekSpoor' : {'#text' : 'Utrecht'}})
    'Utrecht'
    """
    try:
       Spoor = (info['VertrekSpoor'])['#text']

    except KeyError:
        Spoor = "'Onbekend'"
    return Spoor



def Trein(info):
    if info['TreinSoort'] is not None:
        Trein = info['TreinSoort']
    else:
        Trein = "trein"
    return Trein


def Vertraging(info):
    try:
        Vertraging = " " + info['VertrekVertragingTekst']
    except KeyError:
        Vertraging = ""
    return Vertraging


def Wijziging(info):
    try:
        Wijziging = "Let op!: " + info['Opmerkingen']['Opmerking']
    except KeyError:
        Wijziging = ""
    return Wijziging


def onClick(text):
    tkinter.messagebox.showinfo("Mededeling", "Let op! " + text)


Tabellen = []
def ActueleVertrekInformatie():
    for Tabel in Tabellen:
        Tabel.destroy()
    try:
        EindText = ""
        stationdict = processXML('vertrektijden.xml')
        informatie = stationdict['ActueleVertrekTijden']['VertrekkendeTrein']
        for info in informatie:
            EindText += ("De {} naar {} \nvertrekt om {}{} vanaf spoor {} {}".format(Trein(info), Bestemming(info),
                                                                                     ((Tijd(info))[0])[0:5],
                                                                                     Vertraging(info), Spoor(info),
                                                                                     Wijziging(info))+'\nq')

            #EindText+="Dit is een test versie! Let op!: Dit is alleen maar een testq"
        global regel
        regel = EindText.split('q')
        eindoutput(regel)

        return True
    except KeyError:
        return False

def eindoutput(regel):
    aantal = 0
    posx = 250
    posy = 260

    for r in regel:
        Tabel = Label(Root, text=r, justify=LEFT, anchor='nw', width=35, height=2)
        if "Let op" in r:
            splitting = r.split('Let op!:')

            Tabel = Label(Root, text=(splitting[0]), justify=LEFT, anchor='nw', width=35, height=2)
            button = tkinter.Button(Root, image=photo, command=lambda text=splitting[1]: onClick(text))
            button.place(x=posx + 220, y=posy + 5)
            Tabellen.append(button)

        Tabel.place(x=posx, y=posy)
        posy += 45
        Tabellen.append(Tabel)
        aantal += 1
        if aantal == 10:
            posx = 530
            posy = 260
        elif aantal == 20:
            posx = 810
            posy = 260
        elif aantal == 30:
            break


def Nederlands():
    os.system('py NS_projectNL.py')
    Root.destroy()

#NSlogo = PhotoImage(file="C:\\Users\\gfjan\Pictures\\NSlogo.png")
#NSlabel = Label(Root, image=NSlogo, borderwidth=0, height=140, width=340)
#NSlabel.place(x=1000, y=30)
photo=PhotoImage(file="C:\\Users\\Diana\\Pictures\\OpmerkingenKnop.png")
Label(Root, bg="#ffc917", text="Zoek uw station:").place(x=510, y=175)
blue = Label(Root, background="#003082", height=3)
blue.pack(side=BOTTOM, fill="x")

Error = Label(Root, text="Geef een geldige stationsnaam op!", font=("", 55, "bold"),
              bg="#ffc917", fg="black")

MainMenu = Button(Root, command=Nederlands, text="Terug", bg="#003082", fg="white", width=20, height=4, anchor="w",
                  borderwidth=0, font=("", 9, "bold"))
MainMenu.place(x=10, y=10)

Root.overrideredirect(True)
Root.geometry("{0}x{1}+0+0".format(Root.winfo_screenwidth(), Root.winfo_screenheight()))
Root.bind("<Escape>", lambda e: e.widget.quit())

Root.mainloop()
