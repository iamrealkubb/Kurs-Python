def tworzenie_slownika_1():
    return {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}

def tworzenie_slownika_2():
    return dict([
        ('I', 1),
        ('V', 5),
        ('X', 10),
        ('L', 50),
        ('C', 100),
        ('D', 500),
        ('M', 1000)
    ])

def tworzenie_slownika_3():
    rzymskie = "IVXLCDM"
    arabskie = [1, 5, 10, 50, 100, 500, 1000]
    slownik = {}

    for i in range(len(rzymskie)):
        slownik[rzymskie[i]] = arabskie[i]

    return slownik

def roman2int(liczba_rzymska):
    slownik = tworzenie_slownika_3()
    liczba_arabska = 0
    poprzednia_wartosc = 0

    for znak in reversed(liczba_rzymska):
        aktualna_wartosc = slownik.get(znak)

        if aktualna_wartosc < poprzednia_wartosc:
            liczba_arabska -= aktualna_wartosc
        else:
            liczba_arabska += aktualna_wartosc

        poprzednia_wartosc = aktualna_wartosc

    return liczba_arabska

wynik = roman2int("MDCCCLXIV")
print(wynik)

assert wynik == 1864
print('OK')