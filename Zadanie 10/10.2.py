import tkinter as tk
import random

KAMIEN = "Kamień"
PAPIER = "Papier"
NOZYCE = "Nożyce"

WYGRANA = "Wygrałeś"
PRZEGRANA = "Przegrałeś"
REMIS = "Remis"

KOLOR_TLA = "#f0f0f0"
DUZA_CZCIONKA = ("Arial", 14, "bold")
SREDNIA_CZCIONKA = ("Arial", 12)

okno = tk.Tk()
okno.title("Papier | Kamień | Nożyce")
okno.geometry("500x400")
okno.config(bg=KOLOR_TLA)

naglowek = tk.Label(okno, text="Twój ruch:", font=DUZA_CZCIONKA, bg=KOLOR_TLA)
naglowek.pack(pady=20)

ramka_przyciski = tk.Frame(okno, bg=KOLOR_TLA)
ramka_przyciski.pack(pady=10)

etykieta_wybor_gracza = tk.Label(okno, text="Twój wybór: -", font=SREDNIA_CZCIONKA, bg=KOLOR_TLA)
etykieta_wybor_gracza.pack(pady=10)

etykieta_wybor_komputera = tk.Label(okno, text="Wybór komputera: -", font=SREDNIA_CZCIONKA, bg=KOLOR_TLA)
etykieta_wybor_komputera.pack(pady=5)

etykieta_wynik = tk.Label(okno, text="Wynik gry: -", font=SREDNIA_CZCIONKA, bg=KOLOR_TLA)
etykieta_wynik.pack(pady=20)

def wylosuj_wybor_komputera():
    opcje = [KAMIEN, PAPIER, NOZYCE]
    return random.choice(opcje)

def kto_wygral(wybor_gracza, wybor_komputera):

    if wybor_gracza == wybor_komputera:
        return REMIS

    if wybor_gracza == KAMIEN and wybor_komputera == NOZYCE:
        return WYGRANA
    elif wybor_gracza == PAPIER and wybor_komputera == KAMIEN:
        return WYGRANA
    elif wybor_gracza == NOZYCE and wybor_komputera == PAPIER:
        return WYGRANA
    else:
        return PRZEGRANA

def graj(wybor_gracza):
    wybor_komputera = wylosuj_wybor_komputera()
    wynik_tekst = kto_wygral(wybor_gracza, wybor_komputera)

    etykieta_wybor_gracza.config(text=f"Twój wybór: {wybor_gracza}")
    etykieta_wybor_komputera.config(text=f"Wybór komputera: {wybor_komputera}")
    etykieta_wynik.config(text=wynik_tekst, fg="blue")

przycisk_kamien = tk.Button(
    ramka_przyciski,
    text=KAMIEN,
    width=10,
    command=lambda: graj(KAMIEN)
)
przycisk_kamien.grid(row=0, column=0, padx=5)

przycisk_papier = tk.Button(
    ramka_przyciski,
    text=PAPIER,
    width=10,
    command=lambda: graj(PAPIER)
)
przycisk_papier.grid(row=0, column=1, padx=5)

przycisk_nozyce = tk.Button(
    ramka_przyciski,
    text=NOZYCE,
    width=10,
    command=lambda: graj(NOZYCE)
)
przycisk_nozyce.grid(row=0, column=2, padx=5)

okno.mainloop()