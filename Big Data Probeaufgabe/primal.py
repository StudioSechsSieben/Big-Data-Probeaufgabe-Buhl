from prime_numbers import PrimeNumbers

# Aufgabenbeschreibung
"""
Schreibe eine Klasse Primal, welche von der Klasse PrimeNumbers erbt.
Die Instanzen dieser Klasse sollen Folgendes besitzen:
a. Eine positive Zahl to_number (protected)
    i. Beinhaltet die Maximalzahl bis zur der berechnet werden soll.
b. Eine Funktion set_to_number(int) welche einen Integer wert als Übergabe Parameter erwartet.
    i. Speichert den übergebenen Wert in der to_number-Variable
c. Eine Funktion prozess() (private)
    i. Berechnet alle Primzahlen bis zum vorgegebenen Wert (to_number)
"""


class Primal(PrimeNumbers):
    def __init__(self):
        # a) Beinhaltet die Maximalzahl bis zur der berechnet werden soll
        super().__init__()
        self._to_number = 0  # a) Geschützte Maximalzahl

    def set_to_number(self, value: int):
        # Setzt die Maximalzahl und b) Speichert den übergebenen Wert in der to_number-Variable
        if value > 0:
            self._to_number = value
        else:
            # Fehlermeldung falls ein negativer Wert eingegeben wurde
            raise ValueError("Die Zahl muss positiv sein.")

    def __prozess(self):
        # c) Berechnet alle Primzahlen bis zum vorgegebenen Wert
        for num in range(2, self._to_number + 1):
            if all(num % i != 0 for i in range(2, int(num ** 0.5) + 1)):
                self._add_prime(num)