def kwadraten_som(lijst):
    som=0
    for getal in lijst:
        if getal >=0:
            som+=getal**2
    return som

grondgetallen = [ 4, 5, 3, -81 ]
print(kwadraten_som(grondgetallen))
