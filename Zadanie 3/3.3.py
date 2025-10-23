lista = []
for i in range(31):
    if i % 3 != 0:
        lista.append(i)

print(lista)

assert lista == [1, 2, 4, 5, 7, 8, 10, 11, 13, 14, 16, 17, 19, 20, 22, 23, 25, 26, 28, 29]
print('OK')