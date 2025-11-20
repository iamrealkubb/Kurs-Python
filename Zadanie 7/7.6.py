import itertools
import random
#  iteratory nieskończone:
# (a) zwracający 0, 1, 0, 1, 0, 1, ...
it1 = itertools.cycle([0, 1])

assert [next(it1) for _ in range(6)] == [0, 1, 0, 1, 0, 1] # sprawdzenie kilku pierwszych

# (b) zwracający przypadkowo jedną wartość z ("N", "E", "S", "W") [błądzenie przypadkowe na sieci kwadratowej 2D]
it2 = iter(lambda: random.choice(("N", "E", "S", "W")), None)

assert all(v in {"N", "E", "S", "W"} for v in [next(it2) for _ in range(10)]) # symboliczne sprawdzenie czy iterator daje dobre kierunki

# (c) zwracający 0, 1, 2, 3, 4, 5, 6, 0, 1, 2, 3, 4, 5, 6, ... [numery dni tygodnia]
it3 = itertools.cycle(range(7))

assert [next(it3) for _ in range(10)] == [0,1,2,3,4,5,6,0,1,2] # sprawdzenie kilku pierwszych

print('OK!')