import requests
import xmltodict

def treintijden(): #vraagt alle informatie op vanuit de API
        station = input("Geef de stationsnaam op:")
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


def Tijd(info):
    if info['VertrekTijd'] is not None:
        tijd1=info['VertrekTijd']
        tijd2 = tijd1.split('T')
        TijdNet = tijd2[1].split('+')
    return TijdNet

def Plaats(info):
    if info['EindBestemming'] is not None:
        Bestemming=info['EindBestemming']
    return Bestemming

def Spoor(info):
    if info['VertrekSpoor'] is not None:
        try:
            Spoor=(info['VertrekSpoor'])['#text']
        except KeyError:
            Spoor="'Onbekend'"
    return Spoor

def Trein(info):
    if info['TreinSoort'] is not None:
        Trein=info['TreinSoort']
    return Trein

def Vertraging(info):
    if info['VertrekTijd'] is not None:
        try:
            Vertraging= " "+info['VertrekVertragingTekst']
        except KeyError:
            Vertraging= ""
    return Vertraging

def Wijziging(info):
        if info is not None:
            try:
                Wijziging="Let op!: "+info['Opmerkingen']['Opmerking']
            except KeyError:
                Wijziging = ""
        return Wijziging

def Bestemming():
    try:
        stationdict = processXML('vertrektijden.xml')
        informatie = stationdict['ActueleVertrekTijden']['VertrekkendeTrein']
        for info in informatie:
            EindText=("De {} naar {} vertrekt om {}{} vanaf spoor {} {}".format(Trein(info),Plaats(info),((Tijd(info))[0])[0:5],Vertraging(info),Spoor(info),Wijziging(info)))
            print(EindText)
    except KeyError:
        print("Geef een geldige stations naam")

Bestemming()
