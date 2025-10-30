def suma_sek(sekwencja):
    if not isinstance(sekwencja, (list, tuple)):
        raise ValueError("argument musi byc lista lub krotka")

    suma = 0
    for element in sekwencja:
        if isinstance(element, (list, tuple)):
            suma += suma_sek(element)
        else:
            suma += element
    return suma

print("Wynik dla przykladowej sekwencji [1, 2, [3, 4], (5, 6)]:", suma_sek([1, 2, [3, 4], (5, 6)]))

assert suma_sek([1, 2, [3, 4], (5, 6)]) == 21
assert suma_sek((1, (2, 3), [4, [5]])) == 15
print("OK")