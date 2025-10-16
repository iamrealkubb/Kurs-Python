# 2.10
line = """jakis      ciag
    znakow   ktory
jest dlugi GvR"""
lista_wyrazow = line.split()
liczba_wyrazow = len(lista_wyrazow)

print("2.10: Liczba wyrazow -", liczba_wyrazow)
assert liczba_wyrazow == 7, "Blad w 2.10"

# 2.11
word = "slowo"
rozdzielony = '_'.join(word)

print("2.11:", rozdzielony)
assert rozdzielony == "s_l_o_w_o", "Blad w 2.11"

# 2.12
pierwsze = ''.join(w[0] for w in lista_wyrazow)
ostatnie = ''.join(w[-1] for w in lista_wyrazow)

print("2.12: Z pierwszych:", pierwsze, ", Z ostatnich:", ostatnie)
assert pierwsze == "jczkjdG", "Blad w 2.12"
assert ostatnie == "sgwytiR", "Blad w 2.12"

# 2.13
dlugosc = sum(len(w) for w in lista_wyrazow)

print("2.13: Dlugosc:", dlugosc)
assert dlugosc == 32, "Blad w 2.13"

# 2.14
najdluzszy = max(lista_wyrazow, key=len)
dlugosc_najdluzszego = len(najdluzszy)

print("2.14: Najdluzszy:", najdluzszy, ", Dlugosc najdluzszego:", dlugosc_najdluzszego)
assert najdluzszy == "znakow", "Blad w 2.14"
assert dlugosc_najdluzszego == 6, "Blad w 2.14"

# 2.15
L = [12, 367, 1, 75, 7, 983, 33]
ciag = ''.join(str(x) for x in L)

print("2.15:", ciag)
assert ciag == "12367175798333", "Blad w 2.15"

# 2.16
line = line.replace("GvR", "Guido van Rossum")

print("2.16: Po zamianie -", line)
assert "Guido van Rossum" in line, "Blad w 2.16"

# 2.17
alfabetycznie = sorted(lista_wyrazow)
wzgledem_dlugosci = sorted(lista_wyrazow, key=len)

print("2.17: Alfabetycznie:", alfabetycznie, ", Wzgledem dlugosci:", wzgledem_dlugosci)
assert alfabetycznie == ['GvR', 'ciag', 'dlugi', 'jakis', 'jest', 'ktory', 'znakow'], "Blad w 2.17"
assert wzgledem_dlugosci == ['GvR', 'ciag', 'jest', 'jakis', 'ktory', 'dlugi', 'znakow'], "Blad w 2.17"

# 2.18
liczba = 10329490109012900
liczba_zer = str(liczba).count("0")

print("2.18: Liczba zer -", liczba_zer)
assert liczba_zer == 6, "Blad w 2.18"

# 2.19
wynikowy_lancuch = ''.join(str(x).zfill(3) for x in L)

print("2.19: Wynikowy lancuch -", wynikowy_lancuch)
assert wynikowy_lancuch == "012367001075007983033", "Blad w 2.19"

print("Wszystko OK!")