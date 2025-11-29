
# zarządzanie rezerwacjami i miejscami

from klasy_i_przechowanie import Rezerwacja

class Teatr:
    def __init__(self, nazwa):
        self.nazwa = nazwa
        self.miejsca = []
        self.rezerwacje = []
        self.klienci = {}       # słownik ID:Klient

#TODO zarządzanie miejscami, wypisać metody

    def dodaj_miejsce(self, miejsce):
        self.miejsca.append(miejsce)
        print(f" Dodano miejsce: {miejsce.get_info()}")

    def dodaj_wiele_miejsc(self, lista_miejsc):
        for miejsce in lista_miejsc:
            self.dodaj_miejsce(miejsce)

    def znajdz_miejsce(self, numer_miejsca):
        for miejsce in self.miejsca:
            if miejsce.numer_miejsca == numer_miejsca:
                return miejsce
        return None

    def pokaz_dostepne_miejsca(self):
        dostepne = [m for m in self.miejsca if m.dostepne]
        if not dostepne:
            print("Brak dostępnych miejsc.")
            return

        print("\n" + "=" * 60)
        print("DOSTĘPNE MIEJSCA")
        print("-" * 60)
        for miejsce in dostepne:
            print(f" • {miejsce.get_info()}")
        print("-" * 60)

    def pokaz_wszystkie_miejsca(self):
        if not self.miejsca:
            print("Brak miejsc w tearze.")
            return

        print("\n" + "=" * 60)
        print(f"WSZYSTKIE MIEJSCA TEATRU '{self.nazwa}'")
        print("-" * 60)
        for miejsce in self.miejsca:
            print(f" {miejsce.get_info()}")
        print("-" * 60)

#TODO zarządzanie rezerwacjami, metody

    def rezerwuj_miejsce(self, klient, numer_miejsca):
        miejsce = self.znajdz_miejsce(numer_miejsca)    # spr czy miejsce istnieje i czy jest wolen
        if not miejsce:
            print(f" BŁĄD: Miejsce {numer_miejsca} nie istnieje.")
            return False
        if not miejsce.dostepne:
            print(f" BŁĄD: Miejsce {numer_miejsca} jest już zarezerwowane.")
            return False
        miejsce.zarezerwuj()

        #TODO rezerwacja
        rezerwacja = Rezerwacja(klient, miejsce)
        self.rezerwacje.append(rezerwacja)
        klient.dodaj_rezerwacje(rezerwacja)

        print(f"\n REZERWACJA POTWIERDZONA")
        print(f"  Klient: {klient.imie} {klient.nazwisko}")
        print(f"  Miejsce: {numer_miejsca} ({miejsce.typ})")
        print(f"  Cena: {miejsce.cena} zł")
        print(f"  ID rezerwacji: {rezerwacja.id_rezerwacji}\n")

        return True

    #TODO Anulowanie po ID

    def anuluj_rezerwacje(self, id_rezerwacji):

