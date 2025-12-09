import tkinter as tk
from tkinter import messagebox, simpledialog

from klasy_i_przechowanie import (
    MiejsceZwykle,
    MiejsceVIP,
    MiejsceDlaNiepelnosprawnych,
    Klient,
)
from teatr_logika import Teatr


def inicjalizuj_teatr():
    teatr = Teatr("Teatr CodeMe")

    # zwykłe miejsca A1-A19
    for i in range(1, 20):
        teatr.dodaj_miejsce(MiejsceZwykle(f"A{i}"))

    # VIP B1-B5
    for i in range(1, 6):
        teatr.dodaj_miejsce(MiejsceVIP(f"B{i}"))

    # dla niepełnosprawnych C1-C3
    for i in range(1, 4):
        teatr.dodaj_miejsce(MiejsceDlaNiepelnosprawnych(f"C{i}"))

    return teatr

class AplikacjaTeatr(tk.Tk):
    def __init__(self):
        super().__init__()


    #TODO dodać definicje
    self.title("System rezerwacji miejsc w teatrze")
    self.geometry("800x500")

    # model
    self.teatr = inicjalizuj_teatr()
    self.klient = None

    # GUI
    self._zbuduj_gui()