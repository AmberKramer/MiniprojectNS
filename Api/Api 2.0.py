import requests
import xmltodict

def treintijden(): 
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
    tijd = (info['VertrekTijd']).split('T')
    TijdNet = tijd[1].split('+')
    return TijdNet

def Bestemming(info): 
    if info['EindBestemming'] is not None:
        Bestemming=info['EindBestemming']
    else:
        Bestemming="'Eindbestemming onbekent'"
    return Bestemming

def Spoor(info):
    try:
        Spoor=(info['VertrekSpoor'])['#text']
    except KeyError: 
        Spoor="'Onbekend'"
    return Spoor

def Trein(info): 
    if info['TreinSoort'] is not None:
        Trein=info['TreinSoort']
    else:
        Trein="trein"
    return Trein

def Vertraging(info):
    try:
        Vertraging= " "+info['VertrekVertragingTekst']
    except KeyError:
        Vertraging= ""
    return Vertraging

def Wijziging(info):
    try:
        Wijziging="Let op!: "+info['Opmerkingen']['Opmerking']
    except KeyError:
        Wijziging = ""
    return Wijziging

def ActueleVertrekInformatie():
    try:
        stationdict = processXML('vertrektijden.xml')
        informatie = stationdict['ActueleVertrekTijden']['VertrekkendeTrein']
        for info in informatie:
            EindText=("De {} naar {} vertrekt om {}{} vanaf spoor {} {}".format(Trein(info),Bestemming(info),((Tijd(info))[0])[0:5],Vertraging(info),Spoor(info),Wijziging(info)))
            print(EindText)
    except KeyError:
        print("Geef een geldige stations naam")

ActueleVertrekInformatie()
