import requests
import xmltodict
from tkinter import *
import os


Root = Tk()
Root['background'] = '#ffc917'

def treintijden(test):  # vraagt alle informatie op vanuit de API
    #station = input("Geef de stationsnaam op:")
    station=test
    label=Label(Root, text= station)
    label.pack()
    auth_details = ('amber.kramer@student.hu.nl', 'vKHIYFtiDBbycMlRcAUsdstrme5Bo4iL76YTBJivyKkio-XWM6QiQA')
    api_url = ('http://webservices.ns.nl/ns-api-avt?station=amsterdam')
    response = requests.get(api_url, auth=auth_details)
    with open('vertrektijden.xml', 'w') as myXMLFile:
        myXMLFile.write(response.text)
treintijden('')
def processXML(filename):
    with open(filename) as myXMLFile:
        filestring = myXMLFile.read()
        xmldictionary = xmltodict.parse(filestring)
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
    for vertrektijd in vertrektijden:
        if vertrektijd['EindBestemming'] is not None and vertrektijd['VertrekTijd'] is not None and vertrektijd[
            'TreinSoort'] is not None and vertrektijd['VertrekSpoor'] is not None:
            tijd = (vertrektijd['VertrekTijd'])
            info = tijd.split('T')
            info2 = info[1].split('+')
            Spoor = vertrektijd['VertrekSpoor']
            # print(Spoor)
        print("De {} naar {} vertrekt om {}".format(vertrektijd['TreinSoort'], vertrektijd['EindBestemming'],
                                                            (info2[0])[0:5]))
Bestemming()



def English():
    os.system('py NS_project.py')
    Root.destroy()

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

Button_2=Button(Root, background="#003082",fg="white",text="Search",command=(lambda:treintijden(ent.get())))
Button_2.place(x=815, y=202)

ent = Entry(Root, font =("Calibri", 18))
ent.place(x=510, y=200, height=30, width = 300)
ent.bind("<Return>", (lambda event: treintijden(ent.get())))

Root.overrideredirect(True)
Root.geometry("{0}x{1}+0+0".format(Root.winfo_screenwidth(), Root.winfo_screenheight()))
Root.bind("<Escape>", lambda e: e.widget.quit())

Root.mainloop()