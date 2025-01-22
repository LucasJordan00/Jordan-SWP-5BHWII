class Essen:
    def __init__(self, name, kalorien):
        # Neuer Fehler und nicht behebar (c)
        if name is None or kalorien is None:
            raise ValueError("Name und Kalorien dürfen nicht None sein.")
        self.name = name
        self.kalorien = kalorien

    def beschreibung(self):
        return f"{self.name} hat {self.kalorien} Kalorien."

class Obst(Essen):
    def __init__(self, name, kalorien, vitamine):
        super().__init__(name, kalorien)
        # Neuer Fehler und behebar (a)
        if not vitamine:
            vitamine = ["keine bekannten Vitamine"]
        self.vitamine = vitamine

    def beschreibung(self):
        return super().beschreibung() + f" Es enthält viele Vitamine: {', '.join(self.vitamine)}."

class FastFood(Essen):
    def __init__(self, name, kalorien, herkunft):
        super().__init__(name, kalorien)
        # Hochgeblubberter Fehler und behebar (b)
        try:
            if not herkunft:
                raise ValueError("Herkunft darf nicht leer sein.")
        except ValueError:
            herkunft = "unbekannt"
        self.herkunft = herkunft

    def beschreibung(self):
        return super().beschreibung() + f" Es ist typisches Fast Food aus {self.herkunft}."

class Dessert(Essen):
    def __init__(self, name, kalorien, zuckergehalt):
        super().__init__(name, kalorien)
        self.zuckergehalt = zuckergehalt

    def beschreibung(self):
        return super().beschreibung() + f" Es enthält {self.zuckergehalt}g Zucker."

# Hauptprogramm
try:  # Hochgeblubberter Fehler und nicht behebar (d)
    apfel = Obst("Apfel", 52, ["Vitamin C", "Vitamin K"])
    burger = FastFood("Burger", 300, "USA")
    kuchen = Dessert("Schokoladenkuchen", 450, 35)

    print(apfel.beschreibung())
    print(burger.beschreibung())
    print(kuchen.beschreibung())
except Exception as e:
    print(f"Ein unerwarteter Fehler ist aufgetreten: {e}")
