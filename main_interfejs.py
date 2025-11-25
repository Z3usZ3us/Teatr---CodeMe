
from klasy_i_przechowanie import Klient, MiejsceZwykle, MiejsceVIP, MiejsceDlaNiepelnosprawnych
from teatr_logika import Teatr

def wyswietl_menu():        # Wyświetla główne menu aplikacji
    print("\n" + "="*60)
    print("SYSTEM REZERWACJI MIEJSC W TEATRZE")
    print("="*60)
    print("1. Pokaż dostępne miejsca")
    print("2. Pokaż wszystkie miejsca")
    print("3. Dokonaj rezerwacji")
    print("4. Anuluj rezerwację")
    print("5. Pokaż moją historię rezerwacji")
    print("6. Pokaż statystyki teatru")
    print("7. Pokaż przychód z rezerwacji")
    print("0. Wyjście")
    print("="*60)