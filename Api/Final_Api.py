#importeerd de benodigde extra onderdelen
import requests
import xmltodict

def treintijden():
    """Vraagt alle informatie op vanuit de API.
    Eerste wordt er om input gevraagd voor het gewenste station.
    Vervolgens word er met deze input de informatie van dit staion opgevraagd bij de NS en dit word opgeschreven in vertrektijden.xml"""
    station = input("Geef de stationsnaam op:")
    auth_details = ('amber.kramer@student.hu.nl', 'vKHIYFtiDBbycMlRcAUsdstrme5Bo4iL76YTBJivyKkio-XWM6QiQA')
    api_url = ('http://webservices.ns.nl/ns-api-avt?station='+station)
    response = requests.get(api_url, auth=auth_details)
    with open('vertrektijden.xml', 'w') as myXMLFile:
        myXMLFile.write(response.text)


def processXML(filename):
    """Vertrektijden.xml wordt uitgelezen
    en alle informatie uit de file wordt overgezet in de dictionary: xmldictionary."""
    with open(filename) as myXMLFile:
        filestring= myXMLFile.read()
        xmldictionary= xmltodict.parse(filestring)
        return xmldictionary


def Tijd(info):
    """De informatie die over de vertrektijd gaat wordt uit de dictionairy gehaald
    De tijd waarde word in stukken geknipt om er voor te zorgen dat alleen de nuttige informatie overblijft, namelijk alleen de vertrektijd in uren en minuten.
    Vervolgens wordt deze waarde teruggegeven"""
    tijd = (info['VertrekTijd']).split('T')
    TijdNet = tijd[1].split('+')
    return TijdNet


def Bestemming(info):
    """De waarde van de eindbestemming word uit de dictionairy gehaald en aan een variabele toegekend.
    Als er niets in het xml bestand stond en deze plek in het de dictionairy leeg is wordt de waarde van de variabele een placeholder
    De nieuwe waarde van Bestemming wordt teruggegeven"""
    if info['EindBestemming'] is not None:
        Bestemming=info['EindBestemming']
    else:
        Bestemming="'Eindbestemming onbekent'"
    return Bestemming


def Spoor(info):
    """De waarde van het vertrekspoor word uit de dictionairy gehaald en aan een variabele toegekend
     Als er geen waarde te vinden is in de dictiorairy zal er een KeyError verschijnen. Zodra did gebeurd zal er een placeholder in de plaats komen van het eigenlijke spoor.
     Vervolgens wordtb de nieuwe waarde van Spoor teruggegevem
    >>> Spoor({'VertrekSpoor' : {'#text' : 'Utrecht'}})
    'Utrecht'
    """
    try:
        Spoor=(info['VertrekSpoor'])['#text']
    except KeyError:
        Spoor="'Onbekend'"
    return Spoor


def Trein(info):
    """De waarde van de treinsoort word uit de dictionairy gehaald en aan een variabele toegekend, zolang deze niet leeg is.
    Als er niets in het xml bestand stond en deze plek in het de dictionairy leeg is wordt de waarde van de variabele een placeholder
    De nieuwe waarde van trein wordt teruggegeven
    >>> Trein({'TreinSoort' : 'Intercity' })
    'Intercity'
    """
    if info['TreinSoort'] is not None:
        Trein=info['TreinSoort']
    else:
        Trein="trein"
    return Trein


def Vertraging(info):
    """De waarde van het vertraging word uit de dictionairy gehaald en aan een variabele toegekend
    Als er geen waarde te vinden is in de dictiorairy zal er een KeyError verschijnen.
    Dit betekend dat er geen vertraging is en zal er dus een lege waarde aan de variabele worden toegekend.
    De nieuwe waarde van vertraging wordt teruggegeven
    >>> Vertraging ({'VertrekVertragingTekst': '+5 min'})
    ' +5 min'
    """
    try:
        Vertraging= " "+info['VertrekVertragingTekst']
    except KeyError:
        Vertraging= ""
    return Vertraging


def Wijziging(info):
    """De waarde van de wijzigingen word uit de dictionairy gehaald en aan een variabele toegekend
    Als er geen waarde te vinden is in de dictiorairy zal er een KeyError verschijnen.
    Dit betekend dat er geen wijzigingen zijn en dus  zal er een lege waarde aan de variabele worden toegekend.
    De nieuwe waarde van wijziging zal worden teruggegeven
    >>> Wijziging({'Opmerkingen': {'Opmerking': 'Trein rijdt niet'}})
    'Let op!: Trein rijdt niet'
    >>> Wijziging({'Opmerkingen': {'Opmerking': 'Niet instappen'}})
    'Let op!: Niet instappen'
    >>> Wijziging({'Opmerkingen': {'Opmerking': 'Extra trein'}})
    'Let op!: Extra trein'
    """
    try:
        Wijziging="Let op!: "+info['Opmerkingen']['Opmerking']
    except KeyError:
        Wijziging = ""
    return Wijziging


def ActueleVertrekInformatie():
    """Zet alle gevraagde informatie netjes achter elkaar
    Alle informatie uit vertrektijden wordt omgezet tot een dictiorairy
    De variabele informatie krijg de waarde van alles in de dictionairry binnen
    de ActueleVertrekTijden en binnen VertrekkendeTrein.
    Voor iedere trein die in de dictionairy staat word het volgende uitgevoerd:
    Zet alle gevraagde informatie netjes achter elkaar in een zin in de juiste volgorde
    De zin met alle informatie wordt geprint
    Als er een verkeerd station wordt ingevoerd zal de file leeg zijn, en zal er dus niets in de dictionairy geplaatst kunnen worden. Dit zal dan een KeyError geven.
    Als er een KeyError is moet er worden weergegeven dat er een geldig station moet worden ingevoerd."""
    try:
        treintijden()
        stationdict = processXML('vertrektijden.xml')
        informatie = stationdict['ActueleVertrekTijden']['VertrekkendeTrein']
        for info in informatie:
            EindText=("De {} naar {} vertrekt om {}{} vanaf spoor {} {}".format(Trein(info),Bestemming(info),((Tijd(info))[0])[0:5],Vertraging(info),Spoor(info),Wijziging(info)))
            print(EindText)
    except KeyError:
        print("Geef een geldige stations naam")


ActueleVertrekInformatie()
