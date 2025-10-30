def make_ruler(n):
    if not isinstance(n, int) or n < 0:
        raise ValueError("n musi byc nieujemna liczba calkowita")

    miarka = '|'

    for i in range(n):
        miarka += '....|'

    miarka += "\n"

    numery = '0'
    for i in range(1, n + 1):
        odstep = 5 - len(str(i))
        numery += ' ' * odstep + str(i)
    miarka += numery

    return miarka

def make_grid(rows, cols):
    if not isinstance(rows, int) or not isinstance(cols, int):
        raise ValueError("rows i cols musza byc liczbami calkowitymi")
    if rows <= 0 or cols <= 0:
        raise ValueError("rows i cols musza byc dodatnie")

    prostokat = ""

    for i in range(rows):
        prostokat += "+---" * cols + "+\n"
        prostokat += "|   " * cols + "|\n"

    prostokat += "+---" * cols + "+"

    return prostokat

print(make_ruler(3))
print(make_grid(2,3))

assert make_ruler(3) == ("|....|....|....|\n"
                         "0    1    2    3")
assert make_grid(2,3) == (
    "+---+---+---+\n"
    "|   |   |   |\n"
    "+---+---+---+\n"
    "|   |   |   |\n"
    "+---+---+---+"
)
print('OK')