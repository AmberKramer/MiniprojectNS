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
    if vertrektijd['VertrekTijd'] is not None:
        try:
            Vertraging= " "+vertrektijd['VertrekVertragingTekst']
        except KeyError:
            Vertraging= ""
    return Vertraging

def Wijziging(vertrektijd):
        if vertrektijd is not None:
            try:
                Wijziging="Let op: "+vertrektijd['Opmerkingen']['Opmerking']
            except KeyError:
                Wijziging = ""
        return Wijziging

def Bestemming():
    try:
        stationdict = processXML('vertrektijden.xml')
        vertrektijden = stationdict['ActueleVertrekTijden']['VertrekkendeTrein']
        for vertrektijd in vertrektijden:
            EindText=("De {} naar {} vertrekt om {}{} vanaf spoor {} {}".format(Trein(vertrektijd),Plaats(vertrektijd),((Tijd(vertrektijd))[0])[0:5],Vertraging(vertrektijd),Spoor(vertrektijd),Wijziging(vertrektijd)))
            print(EindText)
    except KeyError:
        print("Geef een geldige stations naam")

Bestemming()
