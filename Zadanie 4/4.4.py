def fibonacci(n):
    if not isinstance(n, int) or n < 0:
        raise ValueError("n musi byc nieujemna liczba calkowita")

    if n == 0:
        return 0
    if n == 1:
        return 1

    poprzedni = 0
    aktualny = 1

    for i in range(2, n + 1):
        nastepny = poprzedni + aktualny
        poprzedni = aktualny
        aktualny = nastepny

    return aktualny

print("Przykladowy wynik dla n = 8:", fibonacci(8))

assert fibonacci(0) == 0
assert fibonacci(8) == 21
print('OK')