dlugosc_miarki = int(input('Podaj dlugosc miarki: '))

miarka = '|'

for i in range(dlugosc_miarki):
    miarka += '....|'

miarka += "\n"

numery = '0'
for i in range(1, dlugosc_miarki + 1):
    odstep = 5 - len(str(i)) # tyle spacji trzeba wstawic przed liczba
    numery += ' ' * odstep + str(i)
miarka += numery

print(miarka)