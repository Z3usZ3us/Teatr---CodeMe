
from klasy_i_przechowanie import MiejsceZwykle, MiejsceVIP, MiejsceDlaNiepelnosprawnych, Klient


from teatr_logika import Teatr

def wyswietl_menu():        # Wyświetla główne menu aplikacji
    print("\n" + "-"*60)
    print("SYSTEM REZERWACJI MIEJSC W TEATRZE")
    print("-"*60)
    print("1. Pokaż dostępne miejsca")
    print("2. Pokaż wszystkie miejsca")
    print("3. Dokonaj rezerwacji")
    print("4. Anuluj rezerwację")
    print("5. Pokaż moją historię rezerwacji")
    print("6. Pokaż miejsca w tearze i aktywne rezerwacje")
    print("0. Wyjście")
    print("-"*60)

def inicjalizuj_teatr():
    teatr = Teatr("Teatr CodeMe")

    # zwykłe 1-10
    for i in range(1, 31):
        teatr.dodaj_miejsce(MiejsceZwykle(f"A{i}"))

    # VIP 11-15
    for i in range(1, 6):
        teatr.dodaj_miejsce(MiejsceVIP(f"B{i}"))

    # dla Niepełnosprawnych 16-18
    for i in range(1, 4):
        teatr.dodaj_miejsce(MiejsceDlaNiepelnosprawnych(f"C{i}"))

    print(f"\n Teatr '{teatr.nazwa}' został utworzony.")
    print(f" Dodano łącznie {len(teatr.miejsca)} miejsc.\n")

    return teatr

# dostepne miejsca
def opcja_dostepne_miejsca(teatr):
    teatr.pokaz_dostepne_miejsca()

# wszystkie miejsca
def opcja_wszystkie_miejsca(teatr):
    teatr.pokaz_wszystkie_miejsca()

# dokonywanie rezerwacji
def opcja_rezerwacja(teatr, klient):
    # najpierw pokazuje dostepne miejsca
    teatr.pokaz_dostepne_miejsca()

    # prosba o podanie nr miejsca
    try:
        numer_miejsca = input("Podaj numer miejsca do zarezerwowania (np: A1): ").strip().upper()
        teatr.rezerwuj_miejsce(klient, numer_miejsca)

    except Exception as e:
        print(f" Błąd: {e}")

    # anulowanie rezerwacji
def opcja_anuluj(teatr, klient):

    # pokazuje historię
    teatr.historia_rezerwacji(klient)

    if not klient.rezerwacje:
        print("Nie masz żadnych rezerwacji do anulowania.")
        return

    try:
        id_rez = int(input("Podaj ID rezerwacji do anulowania: "))
        teatr.anuluj_rezerwacje(id_rez)
    except ValueError:
        print(" Błąd: Podaj prawidłowy numer ID. ")

    # pokaz historię rezerwacji klienta
def opcja_historia(teatr, klient):
    teatr.historia_rezerwacji(klient)

    # statyski teatru
def opcja_statystyki(teatr):
    teatr.pokaz_statystyki()

    # tworzenie klienta
def stworz_klienta():
    print("\n -- Rejestracja Klienta --")

    #TODO kontrola błędów

    # Pętla dla imienia
    while True:
        imie = input("Podaj imię: ").strip()

        if not imie:
            print(" Imię nie może być puste!")
            continue

        if imie.isalpha():
            break
        else:
            print(" Błędne imię! Wpisz tylko litery (bez cyfr i znaków).")

    # Pętla dla nazwiska (tylko po wpisaniu POPRAWNEGO imienia)
    while True:
        nazwisko = input("Podaj nazwisko: ").strip()

        if not nazwisko:
            print(" Nazwisko nie może być puste!")
            continue

        if nazwisko.isalpha():
            break
        else:
            print(" Błędne nazwisko! Wpisz tylko litery (bez cyfr i znaków).")

    # utworzenie
    klient = Klient(imie, nazwisko)
    print(f"\n Klient zarejestrowany: {klient.get_info()}\n")
    return klient

#TODO pętla programu, główna funkcja

def main():
    teatr = inicjalizuj_teatr()
    klient = None

    # główna pętla
    while True:
        # jeśli klient nie zalogowany to poprosi o rezerwacje
        if klient is None:
            print("\n Musisz się zarejestrować, aby dokonać rezerwacji.")
            klient = stworz_klienta()
            if klient is None:
                continue

        # wyświetla menu
        wyswietl_menu()

        # prosi o wybór
        wybor = input("Wybierz opcję (0-7): ").strip()

        # obsługa wyboru opcji
        if wybor == "1":
            opcja_dostepne_miejsca(teatr)

        elif wybor == "2":
            opcja_wszystkie_miejsca(teatr)

        elif wybor == "3":
            opcja_rezerwacja(teatr, klient)

        elif wybor == "4":
            opcja_anuluj(teatr, klient)

        elif wybor == "5":
            opcja_historia(teatr, klient)

        elif wybor == "6":
            opcja_statystyki(teatr)

        elif wybor == "0":
            print("\n Dziękujemy za korzystanie z naszego systemu!")
            print("  Do widzenia!\n")
            break

        else:
            print(" Nieprawidłowy wybór, Spróbuj ponownie.")

if __name__ ==  "__main__":
    main()