import requests
import xmltodict

def treintijden(): #vraagt alle informatie op vanuit de API
    auth_details = ('amber.kramer@student.hu.nl', 'vKHIYFtiDBbycMlRcAUsdstrme5Bo4iL76YTBJivyKkio-XWM6QiQA')
    api_url = 'http://webservices.ns.nl/ns-api-avt?station=ut'
    response = requests.get(api_url, auth=auth_details)
    with open('vertrektijden.xml', 'w') as myXMLFile:
        myXMLFile.write(response.text)
treintijden()

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
    for vertrektijd in vertrektijden:
        if vertrektijd['EindBestemming'] is not None:
            if vertrektijd['VertrekTijd'] is not None:
                tijd=(vertrektijd['VertrekTijd'])
                info = tijd.split('T')
                info2 = info[1].split('+')
                print ("De trein naar",vertrektijd['EindBestemming'],"vertrekt om",info2[0])




Bestemming()
#processXML('vertrektijden.xml')


#infile = open('vertrektijden.xml', 'r')
#info= infile.readlines()
#treintijden()
#for regels in info:
#    tekst= regels.strip()
#    print(tekst)