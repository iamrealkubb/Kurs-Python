import numpy as np
import ustawienia as ust
from scipy.signal import convolve2d
import pickle

class Siatka:

    def __init__(self, szerokosc, wysokosc, rozmiar_komorki, tryb_torus=True):
        self.widoczne_kolumny = szerokosc // rozmiar_komorki
        self.widoczne_wiersze = wysokosc // rozmiar_komorki
        self.rozmiar_komorki = rozmiar_komorki

        self.margines = 10

        self.liczba_kolumn = self.widoczne_kolumny + 2 * self.margines
        self.liczba_wierszy = self.widoczne_wiersze + 2 * self.margines

        self.licznik_czyszczenia = 0

        if tryb_torus:
            self.ograniczanie = 'wrap'
        else:
            self.ograniczanie = 'fill'

        self.obecny_stan = np.zeros((self.liczba_kolumn, self.liczba_wierszy))

    def generuj_losowa_plansze(self):
        self.obecny_stan = np.random.choice(
            [0, 1],
            size=(self.liczba_kolumn, self.liczba_wierszy),
            p=[1 - ust.PRAWDOPODOBIENSTWO_ZYCIA, ust.PRAWDOPODOBIENSTWO_ZYCIA]
        )
        self.wyczysc_marginesy()

    def oblicz_nastepne_pokolenie(self):
        stan_binarnie = (self.obecny_stan > 0).astype(int)

        maska_sasiedztwa = np.array([
            [1, 1, 1],
            [1, 0, 1],
            [1, 1, 1]
        ])

        # splot macierzy
        liczba_sasiadow = convolve2d(
            stan_binarnie,
            maska_sasiedztwa,
            mode='same', # macierz wynikowa ma takie same wymiary jak wejsciowa
            boundary=self.ograniczanie,
            fillvalue=0
        )

        narodziny = (liczba_sasiadow == 3) & (self.obecny_stan == 0)
        przezycie = ((liczba_sasiadow == 2) | (liczba_sasiadow == 3)) & (stan_binarnie == 1)

        nowy_stan = np.zeros_like(self.obecny_stan)
        nowy_stan[przezycie] = self.obecny_stan[przezycie] + 1
        nowy_stan[narodziny] = 1

        self.obecny_stan[:] = nowy_stan

        if self.ograniczanie == 'fill':
            self.licznik_czyszczenia += 1
            if self.licznik_czyszczenia >= 10:
                self.wyczysc_marginesy()
                self.licznik_czyszczenia = 0

    def wyczysc_marginesy(self):
        m = self.margines
        self.obecny_stan[:m, :] = 0
        self.obecny_stan[-m:, :] = 0
        self.obecny_stan[:, :m] = 0
        self.obecny_stan[:, -m:] = 0

    def zmien_stan_komorki(self, x, y):
        x += self.margines
        y += self.margines
        if 0 <= x < self.liczba_kolumn and 0 <= y < self.liczba_wierszy:
            if self.obecny_stan[x, y] > 0:
                self.obecny_stan[x, y] = 0
            else:
                self.obecny_stan[x, y] = 1

    def reset_planszy(self):
        self.obecny_stan[:] = 0

    def wstaw_wzor(self, x, y, wzor):
        x += self.margines
        y += self.margines
        wzor_np = np.array(wzor).T
        szer_wzoru, wys_wzoru = wzor_np.shape

        if x + szer_wzoru <= self.liczba_kolumn and y + wys_wzoru <= self.liczba_wierszy:
            self.obecny_stan[x : x + szer_wzoru, y : y + wys_wzoru] = wzor_np

    def zapisz_stan(self, nazwa_pliku="zapis_gry.dat"):
        with open(nazwa_pliku, 'wb') as plik:
            pickle.dump(self.obecny_stan, plik)
        print(f"Zapisano stan do {nazwa_pliku}")

    def wczytaj_stan(self, nazwa_pliku="zapis_gry.dat"):
        try:
            with open(nazwa_pliku, 'rb') as plik:
                wczytana_tablica = pickle.load(plik)

                if wczytana_tablica.shape == self.obecny_stan.shape:
                    self.obecny_stan = wczytana_tablica
                    print(f"Wczytano stan z {nazwa_pliku}")
                else:
                    print("Błąd: Zapisany stan ma inne wymiary niż obecne okno")
        except FileNotFoundError:
            print("Błąd: Brak pliku")