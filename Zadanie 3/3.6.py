wiersze = int(input('Ile wierszy: '))
kolumny = int(input('Ile kolumn: '))

prostokat = ""

for i in range(wiersze):
    prostokat += "+---" * kolumny + "+\n" # pierwsza linia powtarzajacej sie czesci
    prostokat += "|   " * kolumny + "|\n" # druga linia powtarzajacej sie czesci

prostokat += "+---" * kolumny + "+" # ostatnia linia

print(prostokat)