### ### ### Co jest złego w kodzie:

### L = [3, 5, 4] ; L = L.sort()
# L będzie równe None, ponieważ funkcja sort() zwraca None.

### x, y = 1, 2, 3
# Nie możnna przypisać większej liczby literałów do mniejszej liczby zmiennych.

### X = 1, 2, 3 ; X[1] = 4
# Nie można zmienić elementów krotki po jej utworzeniu.

### X = [1, 2, 3] ; X[3] = 4
# Próba przypisania wartości do nieistniejącego elementu tablicy.

### X = "abc" ; X.append("d")
# Nie można użyć funkcji append() na łańcuchu.

### L = list(map(pow, range(8)))
# Funkcja pow() wymaga co najmniej dwóch argumentów.