import random

def ziehung():

    return random.sample(range(1, 46), 6)



def statistik(anz_ziehungen):

    zaehler = {i: 0 for i in range(1, 46)}

    for i in range(anz_ziehungen):

        gezogene_zahlen = ziehung()

        for zahl in gezogene_zahlen:
            zaehler[zahl] += 1

    return zaehler

def zeige_statistik(zaehler):

    for zahl, anzahl in zaehler.items():
        print(f" {zahl} ist {anzahl} mal gezogen worden.")

anz_ziehungen = 1000

stat = statistik(anz_ziehungen)

zeige_statistik(stat)
