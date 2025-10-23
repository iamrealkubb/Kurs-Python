lista_sekwencji = [[], [4], (1, 2), [3, 4], (5, 6, 7)]

sumy_liczb = [sum(sekwencja) for sekwencja in lista_sekwencji]
print(sumy_liczb)

assert sumy_liczb == [0,4,3,7,18]
print('OK')