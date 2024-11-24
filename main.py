from primal import Primal
from sieve_of_eratosthenes import SieveOfEratosthenes
import time

# Aufgabenbeschreibung
"""
Schreibe eine main-Datei, welche die beiden Klassen Primal und SieveOfEratosthenes instanziiert.
a. Setze den Wert der beiden für beide Instanzen auf 1.000 und vergleiche die Ergebnisse.
b. Setze den Wert der beiden Instanzen auf 10.000 und stoppe die Bearbeitungszeit für jede Instanz bei 100 Durchläufen.
c. Bestimme den Zeitunterschied in der Bearbeitung der beiden Instanzen bei 100 Durchläufen.
"""

def main():
    # Ausgabe "Vergleich bei Maximalwert 1.000:"
    print("Vergleich bei Maximalwert 1.000:")
    
    # Instanziierung
    primal_instance = Primal()
    sieve_instance = SieveOfEratosthenes()

    # a) Setze den Wert der beiden für beide Instanzen auf 1.000 und vergleiche die Ergebnisse
    primal_instance.set_to_number(1000)
    sieve_instance.set_to_number(1000)

    # Prozesse (Berechnung) ausführen
    primal_instance._Primal__prozess()
    sieve_instance._SieveOfEratosthenes__prozess()

    # a) Ergebnisse vergleichen
    print("Primal-Algorithmus:")
    print("Gefundene Primzahlen:", primal_instance.get_p_numbers())
    print("Summe der Primzahlen:", primal_instance.get_summ())
    print("Durchschnitt der Primzahlen:", primal_instance.get_average())

    print("\nSieve of Eratosthenes:")
    print("Gefundene Primzahlen:", sieve_instance.get_p_numbers())
    print("Summe der Primzahlen:", sieve_instance.get_summ())
    print("Durchschnitt der Primzahlen:", sieve_instance.get_average())

    # b) Setze den Wert der beiden Instanzen auf 10.000
    print("\nVergleich der Bearbeitungszeit bei Maximalwert 10.000:")
    
    primal_instance.set_to_number(10000)
    sieve_instance.set_to_number(10000)

    # b) und stoppe die Bearbeitungszeit für jede Instanz bei 100 Durchläufen
    # Zeitmessung für Primal
    start_time = time.time()
    for _ in range(100):    # Zeit stoppen bei 100
        primal_instance._Primal__prozess()
    primal_time = (time.time() - start_time) / 100  # Durchschnittszeit

    # Zeitmessung für Sieve of Eratosthenes
    start_time = time.time()
    for _ in range(100):     # Zeit stoppen bei 100
        sieve_instance._SieveOfEratosthenes__prozess()
    sieve_time = (time.time() - start_time) / 100  # Durchschnittszeit

    # Zeitunterschied berechnen
    time_difference = primal_time - sieve_time
    # c) Bestimme den Zeitunterschied in der Bearbeitung der beiden Instanzen bei 100 Durchläufen.
    print(f"Durchschnittszeit Primal: {primal_time:.6f} Sekunden")
    print(f"Durchschnittszeit Sieve: {sieve_time:.6f} Sekunden")
    print(f"Zeitunterschied: {time_difference:.6f} Sekunden")

if __name__ == "__main__":
    main()