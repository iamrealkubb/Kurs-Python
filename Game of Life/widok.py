import pygame
import ustawienia as ust
from logika import Siatka

class OknoGry:

    def __init__(self, konfiguracja):
        pygame.init()

        self.szerokosc = konfiguracja["szerokosc"]
        self.wysokosc = konfiguracja["wysokosc"]

        self.ekran = pygame.display.set_mode((self.szerokosc, self.wysokosc))
        pygame.display.set_caption(ust.NAZWA_OKNA)
        self.zegar = pygame.time.Clock()

        self.siatka = Siatka(self.szerokosc, self.wysokosc, ust.ROZMIAR_KOMORKI)

        if konfiguracja["losowy_start"]:
            self.siatka.generuj_losowa_plansze()

        self.czy_dziala = True
        self.pauza = False

    def rysuj_siatke(self):
        self.ekran.fill(ust.KOLOR_TLA)

        wspolrzedne_x, wspolrzedne_y = self.siatka.obecny_stan.nonzero()

        rozmiar = self.siatka.rozmiar_komorki

        for x, y in zip(wspolrzedne_x, wspolrzedne_y):
            prostokat = pygame.Rect(x * rozmiar, y * rozmiar, rozmiar - 1, rozmiar - 1)
            pygame.draw.rect(self.ekran, ust.KOLOR_ZYWEJ_KOMORKI, prostokat)

        pygame.display.flip()

    def obslugiwanie_zdarzen(self):
        for zdarzenie in pygame.event.get():
            if zdarzenie.type == pygame.QUIT:
                self.czy_dziala = False
            elif zdarzenie.type == pygame.KEYDOWN:
                if zdarzenie.key == pygame.K_SPACE:
                    self.pauza = not self.pauza
                elif zdarzenie.key == pygame.K_ESCAPE:
                    self.czy_dziala = False

    def petla_glowna(self):
        while self.czy_dziala:
            self.obslugiwanie_zdarzen()

            if not self.pauza:
                self.siatka.oblicz_nastepne_pokolenie()

            self.rysuj_siatke()
            self.zegar.tick(ust.CZESTOTLIWOSC_ODSWIEZANIA)

        pygame.quit()