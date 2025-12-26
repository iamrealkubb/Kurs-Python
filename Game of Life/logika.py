import numpy as np
import ustawienia as ust
from scipy.signal import convolve2d

class Siatka:

    def __init__(self, szerokosc, wysokosc, rozmiar_komorki):
        self.liczba_kolumn = szerokosc
        self.liczba_wierszy = wysokosc
        self.rozmiar_komorki = rozmiar_komorki

        self.obecny_stan = np.zeros((self.liczba_kolumn, self.liczba_wierszy))

    def generuj_losowa_plansze(self):
        self.obecny_stan = np.random.choice(
            [0, 1],
            size=(self.liczba_kolumn, self.liczba_wierszy),
            p=[1 - ust.PRAWDOPODOBIENSTWO_ZYCIA, ust.PRAWDOPODOBIENSTWO_ZYCIA]
        )

    def oblicz_nastepne_pokolenie(self):
        maska_sasiedztwa = np.array([
            [1, 1, 1],
            [1, 0, 1],
            [1, 1, 1]
        ])

        # splot macierzy
        liczba_sasiadow = convolve2d(
            self.obecny_stan,
            maska_sasiedztwa,
            mode='same', # macierz wynikowa ma takie same wymiary jak wejsciowa
            boundary='wrap' # pozwala na zapetlenie planszy
        )

        narodziny = (liczba_sasiadow == 3) & (self.obecny_stan == 0)
        przezycie = ((liczba_sasiadow == 2) | (liczba_sasiadow == 3) & (self.obecny_stan == 1))

        # reset planszy
        self.obecny_stan[:] = 0
        self.obecny_stan[narodziny | przezycie] = 1