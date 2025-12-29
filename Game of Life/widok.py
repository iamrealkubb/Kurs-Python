import pygame
import ustawienia as ust
from logika import Siatka

class OknoGry:

    def __init__(self, konfiguracja):
        pygame.init()

        self.szerokosc = konfiguracja["szerokosc"]
        self.wysokosc = konfiguracja["wysokosc"]
        self.fps = konfiguracja["fps"]

        self.ekran = pygame.display.set_mode((self.szerokosc, self.wysokosc))
        pygame.display.set_caption(ust.NAZWA_OKNA)
        self.zegar = pygame.time.Clock()

        self.czcionka = pygame.font.SysFont("Arial", 18)
        self.licznik_krokow = 0

        self.siatka = Siatka(self.szerokosc, self.wysokosc, ust.ROZMIAR_KOMORKI)

        if konfiguracja["losowy_start"]:
            self.siatka.generuj_losowa_plansze()
            self.pauza = False
        else:
            self.pauza = True

        self.czy_dziala = True

    def rysuj_info(self):
        tekst_fps = self.czcionka.render(f"Prędkość: {self.fps} FPS", True, ust.KOLOR_TEKSTU)
        tekst_krok = self.czcionka.render(f"Iteracja: {self.licznik_krokow}", True, ust.KOLOR_TEKSTU)

        self.ekran.blit(tekst_fps, (10, 10))
        self.ekran.blit(tekst_krok, (10, 35))

    def rysuj_siatke(self):
        self.ekran.fill(ust.KOLOR_MARTWEJ_KOMORKI)

        for x in range(0, self.szerokosc, self.siatka.rozmiar_komorki):
            pygame.draw.line(self.ekran, ust.KOLOR_SIATKI, (x, 0), (x, self.wysokosc))

        for y in range(0, self.wysokosc, self.siatka.rozmiar_komorki):
            pygame.draw.line(self.ekran, ust.KOLOR_SIATKI, (0, y), (self.szerokosc, y))

        wspolrzedne_x, wspolrzedne_y = self.siatka.obecny_stan.nonzero()

        rozmiar = self.siatka.rozmiar_komorki

        for x, y in zip(wspolrzedne_x, wspolrzedne_y):
            prostokat = pygame.Rect(x * rozmiar + 1, y * rozmiar + 1, rozmiar - 1, rozmiar - 1)
            pygame.draw.rect(self.ekran, ust.KOLOR_ZYWEJ_KOMORKI, prostokat)

        self.rysuj_info()
        pygame.display.flip()

    def zmien_predkosc(self, wartosc):
        self.fps += wartosc

        if self.fps < 1:
            self.fps = 1
        elif self.fps > 60:
            self.fps = 60

    def obslugiwanie_zdarzen(self):
        for zdarzenie in pygame.event.get():
            if zdarzenie.type == pygame.QUIT:
                self.czy_dziala = False
            elif zdarzenie.type == pygame.KEYDOWN:
                if zdarzenie.key == pygame.K_SPACE:
                    self.pauza = not self.pauza
                elif zdarzenie.key == pygame.K_ESCAPE:
                    self.czy_dziala = False
                elif zdarzenie.key == pygame.K_r:
                    if self.pauza:
                        self.siatka.reset_planszy()
                        self.licznik_krokow = 0
                        self.rysuj_siatke()
                elif zdarzenie.key == pygame.K_LEFT:
                    self.zmien_predkosc(-5)
                elif zdarzenie.key == pygame.K_RIGHT:
                    self.zmien_predkosc(5)
            elif zdarzenie.type == pygame.MOUSEBUTTONDOWN:
                if zdarzenie.button == 1:
                    mysz_x, mysz_y = pygame.mouse.get_pos()

                    kolumna = mysz_x // ust.ROZMIAR_KOMORKI
                    wiersz = mysz_y // ust.ROZMIAR_KOMORKI

                    self.siatka.zmien_stan_komorki(kolumna, wiersz)

                    self.rysuj_siatke()

    def petla_glowna(self):
        while self.czy_dziala:
            self.obslugiwanie_zdarzen()

            if not self.pauza:
                self.siatka.oblicz_nastepne_pokolenie()
                self.licznik_krokow += 1
                self.zegar.tick(self.fps)
            else:
                self.zegar.tick(60)

            self.rysuj_siatke()

        pygame.quit()