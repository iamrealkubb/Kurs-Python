import numpy as np
import ustawienia as ust
from scipy.signal import convolve2d

class Siatka:

    def __init__(self, szerokosc, wysokosc, rozmiar_komorki):
        self.liczba_kolumn = szerokosc // rozmiar_komorki
        self.liczba_wierszy = wysokosc // rozmiar_komorki
        self.rozmiar_komorki = rozmiar_komorki

        self.obecny_stan = np.zeros((self.liczba_kolumn, self.liczba_wierszy))

    def generuj_losowa_plansze(self):
        self.obecny_stan = np.random.choice(
            [0, 1],
            size=(self.liczba_kolumn, self.liczba_wierszy),
            p=[1 - ust.PRAWDOPODOBIENSTWO_ZYCIA, ust.PRAWDOPODOBIENSTWO_ZYCIA]
        )

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
            boundary='wrap' # pozwala na zapetlenie planszy
        )

        narodziny = (liczba_sasiadow == 3) & (self.obecny_stan == 0)
        przezycie = ((liczba_sasiadow == 2) | (liczba_sasiadow == 3)) & (stan_binarnie == 1)

        nowy_stan = np.zeros_like(self.obecny_stan)
        nowy_stan[przezycie] = self.obecny_stan[przezycie] + 1
        nowy_stan[narodziny] = 1

        self.obecny_stan[:] = nowy_stan

    def zmien_stan_komorki(self, x, y):
        if 0 <= x < self.liczba_kolumn and 0 <= y < self.liczba_wierszy:
            if self.obecny_stan[x, y] > 0:
                self.obecny_stan[x, y] = 0
            else:
                self.obecny_stan[x, y] = 1

    def reset_planszy(self):
        self.obecny_stan[:] = 0