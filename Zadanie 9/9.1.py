import pygame
import random

SZEROKOSC = 800
WYSOKOSC = 600
KOLOR_TLA = (20, 20, 50)
KOLOR_PLATKA = (255, 255, 255)
KOLOR_ZASPY = (200, 200, 200)
ROZMIAR_PLATKA = 35
PREDKOSC = 3

def gra():
    pygame.init()
    ekran = pygame.display.set_mode((SZEROKOSC, WYSOKOSC))
    zegar = pygame.time.Clock()

    czcionka = pygame.font.SysFont(None, 50)
    przegrana = False

    platki = []
    zaspa = []

    gra_wlaczona = True

    while gra_wlaczona:

        for zdarzenie in pygame.event.get():

            if zdarzenie.type == pygame.QUIT: # zamkniecie okna z gra
                gra_wlaczona = False

            if zdarzenie.type == pygame.KEYDOWN: # restart gry klawiszem 'R'
                if zdarzenie.key == pygame.K_r and przegrana:
                    platki.clear()
                    zaspa.clear()
                    przegrana = False

            if zdarzenie.type == pygame.MOUSEBUTTONDOWN and not przegrana: # klikniecie mysza
                pozycja_myszy = pygame.mouse.get_pos()

                for platek in platki[:]: # : iterujemy po kopii listy by prawidlowo usuwac z niej elementy

                    if platek.collidepoint(pozycja_myszy): # usuwanie platka jesli trafiono mysza
                        platki.remove(platek)

        if not przegrana:

            if random.randint(0, 20) == 0: # losowanie liczby od 0 do 20 i tworzymy nowy platek gdy wypadnie 0 (okolo 5% szans)
                os_x = random.randint(0, SZEROKOSC - ROZMIAR_PLATKA) # losowanie miejsca gdzie ma spasc platek
                nowy_platek = pygame.Rect(os_x, -20, ROZMIAR_PLATKA, ROZMIAR_PLATKA) # -20 by platek plynnie spadl znad okna
                platki.append(nowy_platek)

            for platek in platki[:]:
                platek.y += PREDKOSC # przesuwanie platka w dol

                if platek.bottom >= WYSOKOSC or platek.collidelist(zaspa) != -1: # sprawdzenie czy platek zderzyl sie z krawedzia lub zaspa
                    platki.remove(platek)
                    zaspa.append(platek)

                    if platek.top <= 0: # zaspa urosla ponad gorna czesc ekranu
                        print("Koniec gry")
                        przegrana = True

        # rysowanie
        ekran.fill(KOLOR_TLA)

        for platek in zaspa:
            pygame.draw.rect(ekran, KOLOR_ZASPY, platek)

        for platek in platki:
            pygame.draw.rect(ekran, KOLOR_PLATKA, platek)

        if przegrana:

            napis = czcionka.render("KONIEC GRY | RESTART R", True, (255, 50, 50))
            ramka_napisu = napis.get_rect(center=(SZEROKOSC / 2, WYSOKOSC / 2))
            ekran.blit(napis, ramka_napisu)

        pygame.display.flip()
        zegar.tick(60) # petla wykonuje sie 60 razy na sekunde

    pygame.quit()


if __name__ == "__main__":
    gra()