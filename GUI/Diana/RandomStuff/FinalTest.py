import requests
import xmltodict
from tkinter import *
import os
import time

Root = Tk()
Root['background'] = '#ffc917'

def treintijden(testing): #vraagt alle informatie op vanuit de API
    label = Label(Root, text="Zoekresultaten voor station: " + testing, width=70, bg="#ffc917")
    label.place(x=1000, y=10)
    auth_details = ('amber.kramer@student.hu.nl', 'vKHIYFtiDBbycMlRcAUsdstrme5Bo4iL76YTBJivyKkio-XWM6QiQA')
    api_url = ('http://webservices.ns.nl/ns-api-avt?station='+testing)
    response = requests.get(api_url, auth=auth_details)
    with open('vertrektijden.xml', 'w') as myXMLFile:
        myXMLFile.write(response.text)
    Bestemming()


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
list=[]
def Bestemming():

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
                testEind += ("De {} naar {} vertrekt om {}{} vanaf spoor {}".format(trein, bestemming, (tijd[0])[0:5],vertraging, spoor) + '\n')
            #if counting == 10:
            #    testEind += ("De {} naar {} vertrekt om {}{} vanaf spoor {}".format(trein, bestemming, (tijd[0])[0:5], vertraging, spoor))
            #if counting>10:
            #    break
        label2 = Label(Root, text=testEind, justify=LEFT, anchor='w', width=70, bg="#ffc917", borderwidth=1,relief="solid", font=("", 9, "bold"))
        label2.place(x=1000, y=40)
        regel=testEind.split('\n')
        aantal=0
        tesy=300
        tesx=10
        for r in regel:
            fancy=Label(Root,text=r,  anchor='w', width = 70, height='3')
            fancy.place(x=tesx,y=tesy)
            tesy+=55
            list.append(fancy)
            aantal+=1
            if aantal>11:
                tesx=800
                tesy-=660
                for r in regel:
                    fancy2 = Label(Root, text=r, anchor='w', width=70, height='3')
                    fancy2.place(x=tesx, y=tesy)
                    list.append(fancy2)




    except KeyError:
        label32=Label(Root,text=("Geef een geldige stationsnaam op!!"),font=("a dripping marker",85,"bold"),bg="black",fg="#c00")
        label32.place(x=100, y=350)
        #for label2 in list:
        #    label2.destroy()
        for fancy in list:
            fancy.destroy()


def English():
    os.system('py NS_project.py')
    Root.destroy()


Label(Root, bg = "#ffc917" ,  text="Search your Station:").place(x =510 , y = 175)
blue = Label(Root, background="#003082", height = 3)
blue.pack(side = BOTTOM, fill = "x")

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
