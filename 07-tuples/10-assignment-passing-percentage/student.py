def  passing_percentage(grades):
    #als je tenminste 10 scoort ben je door
    #we moeten het slaagpercentage berekenen
    geslaagd = 0
    aantal_studenten = 0
    for i in range(len(grades)):
        aantal_studenten += 1
        if grades[i] >= 10:
            geslaagd += 1
        if aantal_studenten > 0:
            slaag_percentage = (geslaagd / aantal_studenten) * 100
    return slaag_percentage