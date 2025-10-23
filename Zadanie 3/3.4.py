while True:
    wartosc = input("Podaj liczbe (lub 'stop' by przestac): ")
    if wartosc == "stop":
        break
    try:
        wartosc_float = float(wartosc)
        print(wartosc_float, wartosc_float ** 3)
    except ValueError:
        print("Blad: Nie podano liczby")