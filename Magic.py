class Auto:
    def __init__(self, ps):
        self.ps = ps

    def __add__(self, other):
        if isinstance(other, Auto):
            return self.ps + other.ps
        raise TypeError("Addition ist nur zwischen Auto-Objekten erlaubt.")

    def __sub__(self, other):
        if isinstance(other, Auto):
            return self.ps - other.ps
        raise TypeError("Subtraktion ist nur zwischen Auto-Objekten erlaubt.")

    def __mul__(self, other):
        if isinstance(other, Auto):
            return self.ps * other.ps
        raise TypeError("Multiplikation ist nur zwischen Auto-Objekten erlaubt.")

    def __eq__(self, other):
        if isinstance(other, Auto):
            return self.ps == other.ps
        raise TypeError("Vergleich ist nur zwischen Auto-Objekten erlaubt.")

    def __lt__(self, other):
        if isinstance(other, Auto):
            return self.ps < other.ps
        raise TypeError("Vergleich ist nur zwischen Auto-Objekten erlaubt.")

    def __gt__(self, other):
        if isinstance(other, Auto):
            return self.ps > other.ps
        raise TypeError("Vergleich ist nur zwischen Auto-Objekten erlaubt.")

    def __len__(self):
        return self.ps

# Testzeilen
auto1 = Auto(50)
auto2 = Auto(60)

# Addition
print(f"Addition: {auto1 + auto2}")  # Erwartet: 110

# Subtraktion
print(f"Subtraktion: {auto1 - auto2}")  # Erwartet: -10

# Multiplikation
print(f"Multiplikation: {auto1 * auto2}")  # Erwartet: 3000

# Vergleich
print(f"auto1 == auto2: {auto1 == auto2}")  # Erwartet: False
print(f"auto1 < auto2: {auto1 < auto2}")    # Erwartet: True
print(f"auto1 > auto2: {auto1 > auto2}")    # Erwartet: False

# Länge
print(f"Len von auto1: {len(auto1)}")  # Erwartet: 50
