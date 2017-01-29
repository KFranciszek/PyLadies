#! /usr/bin/python3
# Funkcja zamieniająca czas na sekundy/minuty/godziny

timeDict = {'s': [3600, 60, 1], 'm': [60, 1, 0.016666666666666666], 'h': [1, 0.016666666666666666, 0.0002777777777777778]}

def get_time(time, char):
    splitTime = time.split(':')
    sumTotal = 0
    for i in range(len(splitTime)):
        sumTotal += int(splitTime[i]) * timeDict[char][i]
    print(sumTotal)

running = True
while running:
    exactTime = input('\nWpisz czas (format: xx:xx:xx): ')
    timeChar = ''
    while timeChar not in ['s', 'm', 'h']:
        timeChar = input('Na co chcesz zamienic (s/m/h)?: ')
    get_time(exactTime, timeChar)
    dalej = input('Chcesz konynuowac (t/n)?: ')
    if dalej.lower().startswith('n'):
        running = False
