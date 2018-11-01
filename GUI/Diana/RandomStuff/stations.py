def getStations():
    try:
        stations=['Utrecht CS', 'Alkmaar CS']
        return (stations,"")
    except:
        return([], "Kan stations niet ophalen")

def toonMenu(lijst):
    return
def main():
    stations,fout=getStations()
    if len(stations)>0 and fout=='':
        toonMenu(stations)