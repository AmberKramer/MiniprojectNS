#importeerd de benodigde extra onderdelen
import requests
import xmltodict

def treintijden(): #vraagt alle informatie op vanuit de API
    #Eerste wordt er om input gevraagd voor het gewenste station.
    #Vervolgens word er met deze input de informatie van dit staion opgevraagd bij de NS en dit word opgeschreven in vertrektijden.xml
        station = input("Geef de stationsnaam op:")
        auth_details = ('amber.kramer@student.hu.nl', 'vKHIYFtiDBbycMlRcAUsdstrme5Bo4iL76YTBJivyKkio-XWM6QiQA')
        api_url = ('http://webservices.ns.nl/ns-api-avt?station='+station)
        response = requests.get(api_url, auth=auth_details)
        with open('vertrektijden.xml', 'w') as myXMLFile:
            myXMLFile.write(response.text)

#De functie word gerund om de file te updaten en aan te passen met de informatie van het opgevraagde station.
treintijden()

def processXML(filename):#vertrektijden.xml wordt uitgelezen en alle informatie uit de file wordt overgezet in de dictionary: xmldictionary.
    with open(filename) as myXMLFile:
        filestring= myXMLFile.read()
        xmldictionary= xmltodict.parse(filestring)
        return xmldictionary


def Tijd(info):#returnd VertrekTijd waarde
    #De informatie die over de vertrektijd gaat wordt uit de dictionairy gehaald
    #De tijd waarde word in stukken geknipt om er voor te zorgen dat alleen de nuttige informatie overblijft, namelijk alleen de vertrektijd in uren en minuten.
    tijd = (info['VertrekTijd']).split('T')
    TijdNet = tijd[1].split('+')
    #Vervolgens wordt deze waarde teruggegeven
    return TijdNet

def Bestemming(info): #returnd EIndBestemmings waarde
    #De waarde van de eindbestemming word uit de dictionairy gehaald en aan een variabele toegekend
    if info['EindBestemming'] is not None:
        Bestemming=info['EindBestemming']
    #Als er niets in het xml bestand stond en deze plek in het de dictionairy leeg is wordt de waarde van de variabele een placeholder
    else:
        Bestemming="'Eindbestemming onbekent'"
    #De nieuwe waarde van Bestemming wordt teruggegeven
    return Bestemming

def Spoor(info): #Returnd VertrekSpoor waarde
    #De waarde van het vertrekspoor word uit de dictionairy gehaald en aan een variabele toegekend
    try:
        Spoor=(info['VertrekSpoor'])['#text']
    #Als er geen waarde te vinden is in de dictiorairy zal er een KeyError verschijnen. Zodra did gebeurd zal er een placeholder in de plaats komen van het eigenlijke spoor.
    except KeyError:
        Spoor="'Onbekend'"
    #De nieuwe waarde van Spoor wordt teruggegeven
    return Spoor

def Trein(info): #Returnd TreinSoort waarde
    #De waarde van de treinsoort word uit de dictionairy gehaald en aan een variabele toegekend, zolang deze niet leeg is
    if info['TreinSoort'] is not None:
        Trein=info['TreinSoort']
    #Als er niets in het xml bestand stond en deze plek in het de dictionairy leeg is wordt de waarde van de variabele een placeholder
    else:
        Trein="trein"
    #De nieuwe waarde van trein wordt teruggegeven
    return Trein

def Vertraging(info):#Returnd de mogelijke Vertragings waarde
    #De waarde van het vertraging word uit de dictionairy gehaald en aan een variabele toegekend
    try:
        Vertraging= " "+info['VertrekVertragingTekst']
    # Als er geen waarde te vinden is in de dictiorairy zal er een KeyError verschijnen. Dit betekend dat er geen vertraging is en zal er dus een lege waarde aan de variabele worden toegekend.
    except KeyError:
        Vertraging= ""
    #De nieuwe waarde van vertraging wordt teruggegeven
    return Vertraging

def Wijziging(info):#Returnd de mogelijke Wijzigingen
    #De waarde van de wijzigingen word uit de dictionairy gehaald en aan een variabele toegekend
    try:
        Wijziging="Let op!: "+info['Opmerkingen']['Opmerking']
    # Als er geen waarde te vinden is in de dictiorairy zal er een KeyError verschijnen. Dit betekend dat er geen wijzigingen zijn en dus  zal er een lege waarde aan de variabele worden toegekend.
    except KeyError:
        Wijziging = ""
    #De nieuwe waarde van wijziging zal worden teruggegeven
    return Wijziging

def ActueleVertrekInformatie():#Zet alle gevraagde informatie netjes achter elkaar
    try:
        #Alle informatie uit vertrektijden wordt omgezet tot een dictiorairy
        stationdict = processXML('vertrektijden.xml')
        #De variabele informatie krijg de waarde van alles in de dictionairry binnen de ActueleVertrekTijden en binnen VertrekkendeTrein.
        informatie = stationdict['ActueleVertrekTijden']['VertrekkendeTrein']
        #Voor iedere trein die in de dictionairy staat word het volgende uitgevoerd:
        for info in informatie:
            #Zet alle gevraagde informatie netjes achter elkaar in een zin in de juiste volgorde
            EindText=("De {} naar {} vertrekt om {}{} vanaf spoor {} {}".format(Trein(info),Bestemming(info),((Tijd(info))[0])[0:5],Vertraging(info),Spoor(info),Wijziging(info)))
            #De zin met alle informatie wordt geprint
            print(EindText)
    except KeyError:#Als er een verkeerd station wordt ingevoerd zal de file leeg zijn, en zal er dus niets in de dictionairy geplaatst kunnen worden. Dit zal dan een KeyError geven.
        #Als er een KeyError is moet er worden weergegeven dat er een geldig station moet worden ingevoerd.
        print("Geef een geldige stations naam")

#Runt het vollegide programme, behalve het updaten van het bestand.
ActueleVertrekInformatie()
