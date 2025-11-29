
from datetime import datetime

#TODO Klasa bazowa - MiejsceTeatralne

class MiejsceTeatralne:     # klasa bazowa miejsca, reszta będzie dzieiczyć po tej klasie

    def __init__(self, numer_miejsca, cena):
        self.numer_miejsca = numer_miejsca
        self.cena = cena
        self.dostepne = True  # na początku musi być dostępne
        self.typ = "zwykle"

    def zarezerwuj(self):     # tutaj zazaczamy miejsce jako zajete czyli niedostępne   (działa)
        if self.dostepne:
            self.dostepne = False
            return True
        return False

    def zwolnij(self):      # przy rezygnacji z rezerwcji zwolni status na dostępne
        self.dostepne = True

    def get_info(self):     # napisze czy miesce jest dostepne czy nie
        status = "DOSTĘPNE" if self.dostepne else "ZAREZERWOWANE"
        return f"Miejsce {self.numer_miejsca} ({self.typ}) - {self.cena} zł - {status}"

class MiejsceZwykle(MiejsceTeatralne): #zwykle miejsca

    def __init__(self, numer_miejsca):
        super().__init__(numer_miejsca, cena=50)
        self.typ = "zwykle"

class MiejsceVIP(MiejsceTeatralne):    #  viposkie miejsce dla bogoli

    def __init__(self, numer_miejsca):
        super().__init__(numer_miejsca, cena=100)
        self.typ = "VIP"
        self.dodatkowe_uslugi = ["Poduszka", "Koc", "Darmowy napój"]

    def get_info(self):     #dodatki dla VIPa
        info_base = super().get_info()
        uslugi = ", ".join(self.dodatkowe_uslugi)       # dobiera z selfu dodatkowych usług     (jest ok, przeszło)
        return f"{info_base} | Usługi: {uslugi})"

class MiejsceDlaNiepelnosprawnych(MiejsceTeatralne):   # miejsca dla niepełnospr. tańsze i mają wcześniejszy dostęp

    def __init__(self, numer_miejsca):
         super().__init__(numer_miejsca, cena=30)
         self.typ = "DlaNiepelnosprawnych"
         self.dostep_wczesny = True

    def get_info(self):
         info_base = super().get_info()
         return f"{info_base} | Dostęp wczesny: TAK"


#TODO Klasa rezerwacja

class Rezerwacja:

    licznik_id = 1          # unikalny ID rezerwacji (sprawdzić)

    def __init__(self, klient, miejsce):
        self.id_rezerwacji = Rezerwacja.licznik_id
        Rezerwacja.licznik_id += 1

        self.klient = klient
        self.miejsce = miejsce
        self.data_rezerwacji = datetime.now()
        self.status = "aktywna"

    def anuluj(self):
        self.status = "anulowana"

#TODO zwraca info o rezerwacji
    def get_info(self):
        return f"""
        ID rezerwacji: {self.id_rezerwacji}
        Klient: {self.klient.imie} {self.klient.nazwisko}
        Miejsce: {self.miejsce.cena} zł
        Data rezerwacji: {self.data_rezerwacji.strftime("%Y-%m-%d %H:%M")}
        Status: {self.status.upper()}
        """

# print(datetime.now())
# print(datetime.now().strftime("%Y-%m-%d %H:%M"))
#TODO Klasa klient
class Klient:

    licznik_id = 1  # unikalny ID klienta (działa)

    def __init__(self, imie, nazwisko):
        self.identyfikator = Klient.licznik_id
        Klient.licznik_id += 1

        self.imie = imie
        self.nazwisko = nazwisko
        self.rezerwacje = []        # tutaj bedą zapisane lista rezerwacji tego klienta

    def dodaj_rezerwacje(self, rezerwacje): #dodawanie rezerwacji
        self.rezerwacje.append(rezerwacje)

    def usun_rezerwacje(self, id_rezerwacji):   #usuwanie rezerwacji
        for rez in self.rezerwacje:
            if rez.id_rezerwacji == id_rezerwacji:
                rez.anuluj()
                return True
        return False

    def get_historia(self):     # sprawdzenie czy pusta i histpria rezerwacji
        if not self.rezerwacje:
            return f"Klient {self.imie} {self.nazwisko} nie ma żadnych rezerwacji."

        historia = f"\n--- {self.imie} {self.nazwisko} nie ma żadnych rezerwacji ---\n "
        for rez in self.rezerwacje:
            historia += rez.get_info()
            historia += "\n"
        return historia

    def get_info(self):         # informacje o kliencie
        return f"ID: {self.identyfikator}, Imię: {self.imie}, Nazwisko: {self.nazwisko}"


