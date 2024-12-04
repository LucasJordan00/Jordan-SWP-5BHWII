class Essen:
    def __init__(self, name, kalorien):
        self.name = name
        self.kalorien = kalorien

    def beschreibung(self):
        return f"{self.name} hat {self.kalorien} Kalorien."

class Obst(Essen):
    def __init__(self, name, kalorien, vitamine):
        super().__init__(name, kalorien)
        self.vitamine = vitamine

    def beschreibung(self):
        return super().beschreibung() + f" Es enthält viele Vitamine: {', '.join(self.vitamine)}."

class FastFood(Essen):
    def __init__(self, name, kalorien, herkunft):
        super().__init__(name, kalorien)
        self.herkunft = herkunft

    def beschreibung(self):
        return super().beschreibung() + f" Es ist typisches Fast Food aus {self.herkunft}."

class Dessert(Essen):
    def __init__(self, name, kalorien, zuckergehalt):
        super().__init__(name, kalorien)
        self.zuckergehalt = zuckergehalt

    def beschreibung(self):
        return super().beschreibung() + f" Es enthält {self.zuckergehalt}g Zucker."

apfel = Obst("Apfel", 52, ["Vitamin C", "Vitamin K"])
burger = FastFood("Burger", 300, "den USA")
kuchen = Dessert("Schokoladenkuchen", 450, 35)


print(apfel.beschreibung())
print(burger.beschreibung())
print(kuchen.beschreibung())
