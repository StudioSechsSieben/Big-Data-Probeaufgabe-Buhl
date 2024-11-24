# Big Data Probeaufgabe Buhl

## Umsetzung
Die untenstehende Aufgabe wurde in Python umgesetzt und in diesem GitHub hochgeladen.
Die einzelnen .py Dateien enthalten ebenfalls Kommentare, die den Code beschreiben.
Die Main Datei kann wie gewohnt ausgeführt werden, es sind keine Besonderheiten zu beachten.
Für Rückfragen: marcel_nitsche@web.de.
© Marcel Nitsche 24.11.2024

## Aufgabe:
Schreibe ein Programm zur Berechnung von Primzahlen.
Das Programm soll aus 3 Klassen und einer main-Datei bestehen.
##### 1. Schreibe eine Klasse PrimeNumbers. Die Instanzen dieser Klasse sollen Folgendes besitzen:
- a. Eine Liste p_numbers (private)
  - i. das Attribut beinhaltet die errechneten Primzahlen
 - b. Eine Funktion get_p_numbers() (Ausgabeformat: Liste)
    - i. gibt die Liste der Primzahlen zurück
- c. Eine Funktion get_summ() (Ausgabeformat: Ineger)
  - i. gibt die Summe der gefundenen Primzahlen zurück
- d. Eine Funktion get_average() (Ausgabeformat: float)
  - i. gibt den Durchschnitt der gefundenen Primzahlen zurück
##### 2. Schreibe eine Klasse Primal, welche von der Klasse PrimeNumbers erbt. Die Instanzen dieser Klasse sollen Folgendes besitzen:
- a. Eine positive Zahl to_number (protected)
  - i. Beinhaltet die Maximalzahl bis zur der berechnet werden soll.
- b. Eine Funktion set_to_number(int) welche einen Integer wert als Übergabe Parameter erwartet.
  - i. Speichert den übergebenen Wert in der to_number-Variable
- c. Eine Funktion prozess() (private)
  - i. Berechnet alle Primzahlen bis zum vorgegebenen Wert (to_number)
##### 3. Schreibe eine Klasse SieveOfEratosthenes, welche von der Klasse PrimeNumbers erbt. Die Instanzen dieser Klasse sollen Folgendes besitzen:
- a. Eine positive Zahl to_number (protected)
  - i. Beinhaltet die Maximalzahl bis zur der berechnet werden soll.
- b. Eine Funktion set_to_number(int), welche einen Integerwert als Übergabeparameter erwartet.
  - i. Speichert den übergebenen Wert in der to_number-Variable
- c. Eine Funktion prozess() (private)
  - i. Berechnet alle Primzahlen bis zum vorgegebenen Wert (to_number)
    - ii. Nutze zu diesem Zweck den Algorithmus: Sieb des Eratosthenes iii. https://de.wikipedia.org/wiki/Sieb_des_Eratosthenes
##### 4. Schreibe eine main-Datei, welche die beiden Klassen Primal und SieveOfEratosthenes instanziiert.
  - a. Setze den Wert der beiden für beide Instanzen auf 1.000 und vergleiche die Ergebnisse.
  - b. Setze den Wert der beiden Instanzen auf 10.000 und stoppe die Bearbeitungszeit für jede Instanz bei 100 Durchläufen.
  - c. Bestimme den Zeitunterschied in der Bearbeitung der beiden Instanzen bei 100 Durchläufen.


