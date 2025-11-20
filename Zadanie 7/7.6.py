import itertools
import random
#  iteratory nieskończone:
# (a) zwracający 0, 1, 0, 1, 0, 1, ...
it1 = itertools.cycle([0, 1])

# (b) zwracający przypadkowo jedną wartość z ("N", "E", "S", "W") [błądzenie przypadkowe na sieci kwadratowej 2D]
it2 = iter(lambda: random.choice(("N", "E", "S", "W")), None)

# (c) zwracający 0, 1, 2, 3, 4, 5, 6, 0, 1, 2, 3, 4, 5, 6, ... [numery dni tygodnia]
it3 = itertools.cycle(range(7))