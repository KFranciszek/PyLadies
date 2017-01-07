from random import randint


def zgadnijLiczbe(opcja):
    uruchomiony = True

    while uruchomiony:
        if opcja == 1:
            num = randint(0, 100)
        else:
            num = randint(0, 1000)
        licznik = 0
        while licznik < 5:
            guess = int(input('\nZgadnij liczbe: '))
            if guess != num:
                if guess < num:
                    print('Zle. Liczba jest większa')
                    licznik += 1
                elif guess > num:
                    print('Zle. Liczba jest mniejsza')
                    licznik += 1
            else:
                print('Zgadles! {} to moja liczba.\nPotrzebowales na to {} prob.'.format(num, licznik))
                licznik = 5
        if licznik == 5 and guess != num:
            print('\nPrzegrales. Skonczyly ci sie proby.\nSekretna liczba to {}.\n'.format(num))
            uruchomiony = False
    
        again = input('Czy chcesz zagrac jeszcze raz (t/n)? ')
        if again.lower().startswith('t'):
            start()

def start():
    print('\nWitaj w grze "Zgadnij liczbe".\n')
    for k, v in menu.items():
        print(k, v)
    wybor = ''
    while wybor not in ('1', '2', '3'):
        wybor = input('\nKtora opcje wybierasz? ')
    if wybor in ('1', '2'):
        zgadnijLiczbe(int(wybor))

menu = {1: 'Zakres od 1 do 100.', 2: 'Zakres od 1 do 1000.', 3: 'Wyjscie z gry.'}

start()
