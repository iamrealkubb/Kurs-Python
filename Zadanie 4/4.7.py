def flatten(sekwencja):
    if not isinstance(sekwencja, (list, tuple)):
        raise ValueError("argument musi byc lista lub krotka")

    wynik = []

    for element in sekwencja:
        if isinstance(element, (list, tuple)):
            wynik.extend(flatten(element)) # jesli jest lista lub krotka
        else:
            wynik.append(element) # jesli jest liczba
    return wynik

print("Wynik dla przykladowej sekwencji [1,(2,3),[],[4,(5,6,7)],8,[9]]:", flatten([1,(2,3),[],[4,(5,6,7)],8,[9]]))

sequence = [1,(2,3),[],[4,(5,6,7)],8,[9]]
assert flatten(sequence) == [1, 2, 3, 4, 5, 6, 7, 8, 9]
print("OK")