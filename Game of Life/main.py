from menu_startowe import MenuKonfiguracyjne
from widok import OknoGry

def main():
    aplikacja_startowa = MenuKonfiguracyjne()
    konfiguracja = aplikacja_startowa.uruchom()

    if konfiguracja:
        gra = OknoGry(konfiguracja)
        gra.petla_glowna()

if __name__ == "__main__":
    main()