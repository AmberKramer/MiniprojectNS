import requests
import xmltodict
import NS_StationTab
from tkinter import *
import os
import sys

#NS_StationTab.reply()
def Bart():
    def treintijden(): #vraagt alle informatie op vanuit de API
        station=input("Geef de stationsnaaam op:")
        #station='amsterdam'
        auth_details = ('amber.kramer@student.hu.nl', 'vKHIYFtiDBbycMlRcAUsdstrme5Bo4iL76YTBJivyKkio-XWM6QiQA')
        api_url = ('http://webservices.ns.nl/ns-api-avt?station='+station)
        response = requests.get(api_url, auth=auth_details)
        with open('vertrektijden.xml', 'w') as myXMLFile:
            myXMLFile.write(response.text)
    treintijden()
    def processXML(filename):
        with open(filename) as myXMLFile:
            filestring= myXMLFile.read()
            xmldictionary= xmltodict.parse(filestring)
            return xmldictionary

    def vertrektijd():
        stationdict = processXML('vertrektijden.xml')
        vertrektijden = stationdict['ActueleVertrekTijden']['VertrekkendeTrein']
        for vertrektijd in vertrektijden:
            if vertrektijd['VertrekTijd'] is not None:
                print(vertrektijd['VertrekTijd'])

    processXML('vertrektijden.xml')
    vertrektijd()
    return

from tkinter import *
import os
import sys

Root = Tk()
Root['background'] = '#ffc917'

#sys.path.append("C:/Users/gfjan/PycharmProjects/NS meuk/BartsXMLcode.py")

#tests=[['test','9:04' ], ['Utrecht CS', '9:05'],['test','9:06' ], ['test', '9:07'],['test','9:08' ], ['test', '9:09'],['Utrecht CS','9:09' ], ['test','9:10']]
def reply(name):
    testing = ""
    for naam in name:
        if naam[0] == name:
            testing += (name +" vertrekt om "+ naam[1] + "\n")
    label=Label(Root, bg = "#ffc917" , text=testing)
    label.place(x = 510 , y = 230)

def English():
    os.system('py NS_project.py')
    Root.destroy()

#def Stations():
#    os.system('py BartsXMLcode.py')
#    Root.destroy()

Label(Root, bg = "#ffc917" ,  text="Search your Station:").place(x =510 , y = 175)
blue = Label(Root, background="#003082", height = 3)
blue.pack(side = BOTTOM, fill = "x")

Button_1 = Button(Root, command = English , text="Back", bg="#003082", fg="white", width = 20, height = 4, anchor= "w", borderwidth = 0, font = ("", 9, "bold"))
Button_1.place(x = 10 , y = 10)
Test = Button(Root, command = Bart, text = "test")
Test.place(x = 100 , y = 100)

ent = Entry(Root, font = ("Calibri" , 18))
ent.place(x = 510 , y = 200, height = 30 , width = 300)
ent.bind("<Return>", (lambda event: (ent.get())))

Button_2=Button(Root, background="#003082",fg="white",text="Search",command=(lambda:reply(ent.get())))
Button_2.place(x=815, y=202)

ent = Entry(Root, font =("Calibri", 18))
ent.place(x=510, y=200, height=30, width = 300)
ent.bind("<Return>", (lambda event: reply(ent.get())))

Root.overrideredirect(True)
Root.geometry("{0}x{1}+0+0".format(Root.winfo_screenwidth(), Root.winfo_screenheight()))
Root.bind("<Escape>", lambda e: e.widget.quit())

Root.mainloop()