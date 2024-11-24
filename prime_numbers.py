
# Aufgabenbeschreibung
"""
Schreibe eine Klasse PrimeNumbers.
Die Instanzen dieser Klasse sollen Folgendes besitzen:
a. Eine Liste p_numbers (private)
    i. das Attribut beinhaltet die errechneten Primzahlen
b. Eine Funktion get_p_numbers() (Ausgabeformat: Liste)
    i. gibt die Liste der Primzahlen zurück
c. Eine Funktion get_summ() (Ausgabeformat: Ineger)
    i. gibt die Summe der gefundenen Primzahlen zurück
d. Eine Funktion get_average() (Ausgabeformat: float)
    i. gibt den Durchschnitt der gefundenen Primzahlen zurück
"""

class PrimeNumbers:
    def __init__(self):
        # a) Private Liste der Primzahlen
        self.__p_numbers = []

    def get_p_numbers(self):
        # b) Gibt die Liste der Primzahlen zurück
        return self.__p_numbers

    def get_summ(self):
        # c) Gibt die Summe der gefundenen Primzahlen zurück
        return sum(self.__p_numbers)

    def get_average(self):
        # d) Gibt den Durchschnitt der gefundenen Primzahlen zurück
        if len(self.__p_numbers) == 0:
            return 0.0
        return sum(self.__p_numbers) / len(self.__p_numbers)

    def _add_prime(self, prime):
        # Fügt eine Primzahl zur Liste hinzu (für abgeleitete Klassen)
        self.__p_numbers.append(prime)

        