import requests
import xmltodict
from tkinter import *
import os


Root = Tk()
Root['background'] = '#ffc917'

def treintijden(testing):  # vraagt alle informatie op vanuit de API
    #station = input("Geef de stationsnaam op:")

    label=Label(Root, text="Zoekresultaten voor station: "+testing, width=70, bg="#ffc917")
    #label.pack()
    label.place(x=1000,y=10)
    auth_details = ('amber.kramer@student.hu.nl', 'vKHIYFtiDBbycMlRcAUsdstrme5Bo4iL76YTBJivyKkio-XWM6QiQA')
    api_url = ('http://webservices.ns.nl/ns-api-avt?station='+testing)
    response = requests.get(api_url, auth=auth_details)
    with open('vertrektijden.xml', 'w') as myXMLFile:
        myXMLFile.write(response.text)
    Bestemming()
#treintijden()

def processXML(filename):
    with open(filename) as myXMLFile:
        filestring= myXMLFile.read()
        xmldictionary= xmltodict.parse(filestring)
        return xmldictionary

def Tijd():
    stationdict = processXML('vertrektijden.xml')
    vertrektijden = stationdict['ActueleVertrekTijden']['VertrekkendeTrein']
    for vertrektijd in vertrektijden:
        if vertrektijd['VertrekTijd'] is not None:
            print(vertrektijd['VertrekTijd'])

def Bestemming():
    stationdict = processXML('vertrektijden.xml')
    vertrektijden = stationdict['ActueleVertrekTijden']['VertrekkendeTrein']
    testEind=""
    for vertrektijd in vertrektijden:
        if vertrektijd['EindBestemming'] is not None and vertrektijd['VertrekTijd'] is not None and vertrektijd['TreinSoort'] is not None and vertrektijd['VertrekSpoor'] is not None:
            tijd = (vertrektijd['VertrekTijd'])
            info = tijd.split('T')
            info2 = info[1].split('+')
            Spoor=(vertrektijd['VertrekSpoor'])['#text']
            #print(Spoor)
            #if SpoorReal is not None:
            #EindText=("De {} naar {} vertrekt om {} vanaf spoor {}".format(vertrektijd['TreinSoort'], vertrektijd['EindBestemming'], (info2[0])[0:5], Spoor))
            testEind += ("De {} naar {} vertrekt om {} vanaf spoor {}".format(vertrektijd['TreinSoort'], vertrektijd['EindBestemming'],(info2[0])[0:5], Spoor)+'\n')
    #label2 = Label(Root, text=testEind+'\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n', width=70, bg="#ffc917")
    #label2 = Label(Root, text=testEind, justify=LEFT, width=70, bg="#c0ff3e", borderwidth=2,relief="solid")
    label2 = Label(Root, text=testEind, justify=LEFT, width=70, bg="#ffc917", borderwidth=2, relief="solid")
    #label2.pack()
    label2.place(x=1000,y=40)


#Bestemming()


def English():
    os.system('py NS_project.py')
    Root.destroy()

def reply(test):
    testing=test
    treintijden(testing)

Label(Root, bg = "#ffc917" ,  text="Search your Station:").place(x =510 , y = 175)
blue = Label(Root, background="#003082", height = 3)
blue.pack(side = BOTTOM, fill = "x")

Button_1 = Button(Root, command = English , text="Back", bg="#003082", fg="white", width = 20, height = 4, anchor= "w", borderwidth = 0, font = ("", 9, "bold"))
Button_1.place(x = 10 , y = 10)
#Test = Button(Root, command = Bart, text = "test")
#Test.place(x = 100 , y = 100)

ent = Entry(Root, font = ("Calibri" , 18))
ent.place(x = 510 , y = 200, height = 30 , width = 300)
ent.bind("<Return>", (lambda event: (ent.get())))

#Button_2=Button(Root, background="#003082",fg="white",text="Search",command=lambda event: reply(ent.get()))
#Button_2.place(x=815, y=202)
#button klaagt over lambda event...


ent = Entry(Root, font =("Calibri", 18))
ent.place(x=510, y=200, height=30, width = 300)
ent.bind("<Return>", lambda event: reply(ent.get()))


Root.overrideredirect(True)
Root.geometry("{0}x{1}+0+0".format(Root.winfo_screenwidth(), Root.winfo_screenheight()))
Root.bind("<Escape>", lambda e: e.widget.quit())

Root.mainloop()