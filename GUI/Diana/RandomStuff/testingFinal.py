import requests
import xmltodict
from tkinter import *
import os
import time

Root = Tk()
Root['background'] = '#ffc917'
list=[]
def treintijden(testing): #vraagt alle informatie op vanuit de API
    label = Label(Root, text="Zoekresultaten voor station: " + testing, width=70, bg="#ffc917")
    label.place(x=1000, y=10)
    auth_details = ('amber.kramer@student.hu.nl', 'vKHIYFtiDBbycMlRcAUsdstrme5Bo4iL76YTBJivyKkio-XWM6QiQA')
    api_url = ('http://webservices.ns.nl/ns-api-avt?station='+testing)
    response = requests.get(api_url, auth=auth_details)
    with open('vertrektijden.xml', 'w') as myXMLFile:
        myXMLFile.write(response.text)
    if not Bestemming():
        label32.place(x=200, y=500)
    else:
        label32.place_forget()


def processXML(filename):
    with open(filename) as myXMLFile:
        filestring= myXMLFile.read()
        xmldictionary= xmltodict.parse(filestring)
        return xmldictionary


def Tijd(vertrektijd):
    if vertrektijd['VertrekTijd'] is not None:
        test=vertrektijd['VertrekTijd']
        tijd = test.split('T')
        TijdNet = tijd[1].split('+')
    return TijdNet

def Plaats(vertrektijd):
    if vertrektijd['EindBestemming'] is not None:
        Bestemming=vertrektijd['EindBestemming']
    return Bestemming

def Spoor(vertrektijd):
    if vertrektijd['VertrekSpoor'] is not None:
        try:
            Spoor=(vertrektijd['VertrekSpoor'])['#text']
        except KeyError:
            Spoor="X"
    return Spoor

def Trein(vertrektijd):
    if vertrektijd['TreinSoort'] is not None:
        Trein=vertrektijd['TreinSoort']
    return Trein

def Vertraging(vertrektijd):
    stationdict= processXML('vertrektijden.xml')
    vertrektijden = stationdict['ActueleVertrekTijden']['VertrekkendeTrein']
    try:
        if vertrektijd['VertrekTijd'] is not None:
            vertraging= " " + vertrektijd['VertrekVertragingTekst']
    except KeyError:
        vertraging= ""

    return vertraging

def Bestemming():
    for fancy in list:
        fancy.destroy()

    try:
        counting=0
        testEind = ""
        stationdict = processXML('vertrektijden.xml')
        vertrektijden = stationdict['ActueleVertrekTijden']['VertrekkendeTrein']
        for vertrektijd in vertrektijden:
            trein=Trein(vertrektijd)
            bestemming=Plaats(vertrektijd)
            spoor=Spoor(vertrektijd)
            tijd=Tijd(vertrektijd)
            vertraging=Vertraging(vertrektijd)
            counting+=1
            if counting >0:
                testEind += ("De {} naar {} \nvertrekt om {}{} vanaf spoor {}".format(trein, bestemming, (tijd[0])[0:5],vertraging, spoor) + '\nq')
            #if counting == 10:
            #    testEind += ("De {} naar {} vertrekt om {}{} vanaf spoor {}".format(trein, bestemming, (tijd[0])[0:5], vertraging, spoor))
            #if counting>10:
            #    break
        regel=testEind.split('q')
        aantal=0
        tesy=300
        tesx=80
        print(testEind)
        for r in regel:
            fancy=Label(Root,text=r,  justify=LEFT, anchor='nw', width = 70, height='3')
            fancy.place(x=tesx,y=tesy)
            tesy+=55
            list.append(fancy)
            aantal+=1
            if aantal==12:
                tesx=670
                tesy=300
            if aantal==24:
                tesx=1270
                tesy=300
            if aantal==36:
                break
        return True
    except KeyError:
        return False

def English():
    os.system('py NS_project.py')
    Root.destroy()


Label(Root, bg = "#ffc917" ,  text="Search your Station:").place(x =510 , y = 175)
blue = Label(Root, background="#003082", height = 3)
blue.pack(side = BOTTOM, fill = "x")

label32 = Label(Root, text="Geef een geldige stationsnaam op!", font=("", 60, "bold"), bg="black", fg="#db0029")


Button_1 = Button(Root, command = English , text="Back", bg="#003082", fg="white", width = 20, height = 4, anchor= "w", borderwidth = 0, font = ("", 9, "bold"))
Button_1.place(x = 10 , y = 10)

Button_2=Button(Root, background="#003082",fg="white",text="Search",command=lambda: treintijden(ent.get()))
Button_2.place(x=815, y=202)

ent = Entry(Root, font =("Calibri", 18))
ent.place(x=510, y=200, height=30, width = 300)
ent.bind("<Return>", lambda event: treintijden(ent.get()))


Root.overrideredirect(True)
Root.geometry("{0}x{1}+0+0".format(Root.winfo_screenwidth(), Root.winfo_screenheight()))
Root.bind("<Escape>", lambda e: e.widget.quit())

Root.mainloop()
