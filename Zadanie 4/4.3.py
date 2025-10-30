def factorial(n):
    if not isinstance(n, int) or n < 0:
        raise ValueError("n musi byc nieujemna liczba calkowita")

    wynik = 1

    for i in range(2, n + 1):
        wynik *= i

    return wynik

print("Przykladowy wynik dla n = 5:", factorial(5))

assert factorial(0) == 1
assert factorial(5) == 120
print('OK')