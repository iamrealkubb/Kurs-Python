def odwracanie(L, left, right):
    if not isinstance(L, list):
        raise ValueError("lista musi byc typu list")
    if not (0 <= left < len(L) and 0 <= right < len(L)):
        raise ValueError("indeksy poza zakresem")
    if left > right:
        raise ValueError("left nie moze byc wiekszy od right")

    while left < right:
        element = L[left]
        L[left] = L[right]
        L[right] = element
        left += 1
        right -= 1

def odwracanie_rek(L, left, right):
    if not isinstance(L, list):
        raise ValueError("lista musi byc typu list")
    if not (0 <= left < len(L) and 0 <= right < len(L)):
        raise ValueError("indeksy poza zakresem")
    if left >= right:
        return

    element = L[left]
    L[left] = L[right]
    L[right] = element

    odwracanie_rek(L, left + 1, right - 1)

L = [1, 2, 3, 4, 5, 6]
odwracanie(L, 1, 4)
assert L == [1, 5, 4, 3, 2, 6]

print("Wynik dla przykladowej listy")
print("Przed odwroceniem")

L = [1, 2, 3, 4, 5, 6]
print(L)

print("Po odwroceniu (L, 1, 4)")

odwracanie_rek(L, 1, 4)
print(L)
assert L == [1, 5, 4, 3, 2, 6]

print("OK")