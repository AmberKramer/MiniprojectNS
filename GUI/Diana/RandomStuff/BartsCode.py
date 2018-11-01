import requests
import xmltodict

def treintijden(): #vraagt alle informatie op vanuit de API
    station=input("Geef de stationsnaaam op:")
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

#infile = open('vertrektijden.xml', 'r')
#info= infile.readlines()
#treintijden()
#for regels in info:
#    tekst= regels.strip()
#    print(tekst)


