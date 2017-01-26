#! /usr/bin/python3
# Funkcja sprawdzająca czy dana liczba jest 'brzydka'.

def ugly(num):
    if num == 1:
        print(True)
    elif num % 2 == 0 or num % 3 == 0 or num % 5 == 0:
        print(True)
    else:
        print(False)

running = True
while running:
    while True:
        try:
            number = int(input('\nWpisz liczbe: '))
            ugly(number)
            break
        except ValueError:
            print('Musisz wpisac liczbe (calkowita).')
    dalej = input('\nKontynuować? (t/n): ')
    if dalej.lower().startswith('n'):
        running = False
