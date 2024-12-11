class Person:
    def __init__(self, name: str, geschlecht: str):
        self.name = name
        self.geschlecht = geschlecht


class Mitarbeiter(Person):
    def __init__(self, name: str, geschlecht: str, abteilung=None):
        super().__init__(name, geschlecht)
        self.abteilung = abteilung


class Abteilungsleiter(Mitarbeiter):
    def __init__(self, name: str, geschlecht: str, abteilung):
        super().__init__(name, geschlecht, abteilung)


class Abteilung:
    def __init__(self, name: str, leiter: Abteilungsleiter = None):
        self.name = name
        self.leiter = leiter
        self.mitarbeiter = []

    def add_mitarbeiter(self, mitarbeiter: Mitarbeiter):
        self.mitarbeiter.append(mitarbeiter)
        mitarbeiter.abteilung = self

    def get_mitarbeiter_anzahl(self):
        return len(self.mitarbeiter)


class Firma:
    def __init__(self, name: str):
        self.name = name
        self.abteilungen = []

    def add_abteilung(self, abteilung: Abteilung):
        self.abteilungen.append(abteilung)

    def get_mitarb_anz(self):
        return sum(abt.get_mitarbeiter_anzahl() for abt in self.abteilungen)

    def get_abtLeit_anz(self):
        return sum(1 for abt in self.abteilungen if abt.leiter is not None)

    def get_abt_anz(self):
        return len(self.abteilungen)
    # elemente der liste zusammen zählen 

    def get_groess_abt(self):
        return max(self.abteilungen, key=lambda abt: abt.get_mitarbeiter_anzahl(), default=None)
    # vergleich "alle" abt und auf grund der mitarbeiter anzahl (key)

    def get_geschl_vert(self):
        gesamt_maenner = 0
        gesamt_frauen = 0
        # Schleifen um alle mitarbeiter in alln abteilungen durchzugehen
        # --> wenn m/w dann parameter +
        for abt in self.abteilungen:
            for mitarbeiter in abt.mitarbeiter:
                if mitarbeiter.geschlecht == "m":
                    gesamt_maenner += 1
                elif mitarbeiter.geschlecht == "w":
                    gesamt_frauen += 1
           # gesamt um dann die % auszurechnen.
        gesamt = gesamt_maenner + gesamt_frauen

        if gesamt == 0:
            return {"maenner": 0, "frauen": 0}
        return {
            "maenner": (gesamt_maenner / gesamt) * 100,
            "frauen": (gesamt_frauen / gesamt) * 100,
        }



firma = Firma("Jordan")


entwicklung = Abteilung("Entwicklung")
marketing = Abteilung("Marketing")


leiter_entwicklung = Abteilungsleiter("Berkan", "w", entwicklung)
entwicklung.leiter = leiter_entwicklung
leiter_marketing = Abteilungsleiter("Tobi", "m", marketing)
marketing.leiter = leiter_marketing


mitarbeiter1 = Mitarbeiter("Fabian", "m")
mitarbeiter2 = Mitarbeiter("Luisa", "w")
mitarbeiter3 = Mitarbeiter("Emma", "w")


entwicklung.add_mitarbeiter(mitarbeiter1)
entwicklung.add_mitarbeiter(mitarbeiter2)
marketing.add_mitarbeiter(mitarbeiter3)


firma.add_abteilung(entwicklung)
firma.add_abteilung(marketing)


print("Gesamtanzahl Mitarbeiter:", firma.get_mitarb_anz())
print("Gesamtanzahl Abteilungsleiter:", firma.get_abtLeit_anz())
print("Gesamtanzahl Abteilungen:", firma.get_abt_anz())
print("Größte Abteilung:", firma.get_groess_abt().name)
print("Geschlechterverteilung:", firma.get_geschl_vert())
