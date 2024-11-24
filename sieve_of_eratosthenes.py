from prime_numbers import PrimeNumbers

# Aufgabenbeschreibung
"""
Schreibe eine Klasse SieveOfEratosthenes, welche von der Klasse PrimeNumbers erbt.
Die Instanzen dieser Klasse sollen Folgendes besitzen:
a. Eine positive Zahl to_number (protected)
    i. Beinhaltet die Maximalzahl bis zur der berechnet werden soll.
b. Eine Funktion set_to_number(int), welche einen Integerwert als Übergabeparameter erwartet.
    i. Speichert den übergebenen Wert in der to_number-Variable
c. Eine Funktion prozess() (private)
    i. Berechnet alle Primzahlen bis zum vorgegebenen Wert (to_number)
    ii. Nutze zu diesem Zweck den Algorithmus: Sieb des Eratosthenes iii. https://de.wikipedia.org/wiki/Sieb_des_Eratosthenes
"""


class SieveOfEratosthenes(PrimeNumbers):
    def __init__(self):
        # a) Beinhaltet die Maximalzahl bis zu der berechnet werden soll
        super().__init__()
        self._to_number = 0  # Geschützte Maximalzahl

    def set_to_number(self, value: int):
        # Setzt die Maximalzahl und b) Speichert den übergebenen Wert in der to_number-Variable
        if value > 0:
            self._to_number = value
        else:
            raise ValueError("Die Zahl muss positiv sein.")

    def __prozess(self):
        # Berechnet alle Primzahlen bis zum vorgegebenen Wert (to_number)
        # Nutzt zu diesem Zweck den Algorithmus: Sieb des Eratosthenes
        sieve = [True] * (self._to_number + 1)
        sieve[0] = sieve[1] = False  # 0 und 1 sind keine Primzahlen

        for i in range(2, int(self._to_number ** 0.5) + 1):
            if sieve[i]:
                for multiple in range(i * i, self._to_number + 1, i):
                    sieve[multiple] = False

        # Füge alle Primzahlen in die Liste ein
        for i, is_prime in enumerate(sieve):
            if is_prime:
                self._add_prime(i)