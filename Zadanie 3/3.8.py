sekwencja1 = input("Pierwsza sekwencja: ")
sekwencja2 = input("Druga sekwencja: ")

sekwencja1 = str(sekwencja1)
sekwencja2 = str(sekwencja2)

# zamieniam na zbiory i znajduje ich czesc wspolna oraz sume
s1_zbior = set(sekwencja1)
s2_zbior = set(sekwencja2)
czesc_wspolna = s1_zbior & s2_zbior
suma = s1_zbior | s2_zbior

wspolne = list(czesc_wspolna)
wszystkie = list(suma)

print("Wspolne:", wspolne)
print("Wsystkie:", wszystkie)