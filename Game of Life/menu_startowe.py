import tkinter as tk
from tkinter import messagebox
import ustawienia as ust

class MenuKonfiguracyjne:

    def __init__(self):
        self.okno_glowne = tk.Tk()
        self.okno_glowne.title("Konfigurator Symulacji")

        self.okno_glowne.geometry("400x300")

        self.wybrana_szerokosc = tk.IntVar(value=ust.SZEROKOSC_OKNA)
        self.wybrana_wysokosc = tk.IntVar(value=ust.WYSOKOSC_OKNA)
        self.start_losowy = tk.BooleanVar(value=True)

        self.budowanie_interfejsu()
        self.czy_uruchomic_gre = False

    def budowanie_interfejsu(self):
        tk.Label(self.okno_glowne, text="Szerokość okna:").pack(pady=5)
        tk.Entry(self.okno_glowne, textvariable=self.wybrana_szerokosc).pack()

        tk.Label(self.okno_glowne, text="Wysokość okna:").pack(pady=5)
        tk.Entry(self.okno_glowne, textvariable=self.wybrana_wysokosc).pack()

        tk.Checkbutton(self.okno_glowne, text="Start z losową planszą", variable=self.start_losowy).pack(pady=10)

        tk.Button(self.okno_glowne, text="URUCHOM SYMULACJĘ", command=self.zatwierdz, bg="#dddddd").pack(pady=20, padx=50)

    def zatwierdz(self):
        try:
            szer = self.wybrana_szerokosc.get()
            wys = self.wybrana_wysokosc.get()

            if szer < 200 or wys < 200:
                raise ValueError("Rozmiar okna jest za mały")

            self.czy_uruchomic_gre = True
            self.okno_glowne.destroy()

        except Exception as e:
            messagebox.showerror("Błąd danych", f"Wprowadzono niepoprawne dane:\n{e}")

    def uruchom(self):
        self.okno_glowne.mainloop()

        if self.czy_uruchomic_gre:
            return {
                "szerokosc": self.wybrana_szerokosc.get(),
                "wysokosc": self.wybrana_wysokosc.get(),
                "losowy_start": self.start_losowy.get()
            }
        return None