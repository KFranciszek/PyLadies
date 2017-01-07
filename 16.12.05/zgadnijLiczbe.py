from random import randint


def czyLiczbaJestOk(liczba, zakres):
    while True:
        try:
            liczba = int(liczba)
            if liczba in range(zakres[0], zakres[1]+1):
                return liczba
            else:
                print('Musisz podac liczbe w zakresie {} - {}.'.format(*zakres))
        except ValueError:
            print('Musisz podac liczbe (calkowita).')
        liczba = input('\nZgadnij liczbe: ')

def zgadnijLiczbe(opcja):
    if opcja == 1:
        liczby = (0, 100)
    else:
        liczby = (0, 1000)
    num = randint(liczby[0], liczby[1])
    licznik = 0
    while licznik < 5:
        print('\n\nLiczba prob: {}'.format(5 - licznik))
        guess = input('\nZgadnij liczbe: ')
        guess = czyLiczbaJestOk(guess, liczby)
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
    
    again = input('\nCzy chcesz zagrac jeszcze raz (t/n)? ')
    if again.lower().startswith('t'):
            start()

def start():
    print('\nWitaj w grze "Zgadnij liczbe w 5 probach".\n')
    for k, v in menu.items():
        print(k, v)
    wybor = ''
    while wybor not in ('1', '2', '3'):
        wybor = input('\nKtora opcje wybierasz? ')
    if wybor in ('1', '2'):
        zgadnijLiczbe(int(wybor))

menu = {1: 'Zakres od 1 do 100.', 2: 'Zakres od 1 do 1000.', 3: 'Wyjscie z gry.'}

start()
