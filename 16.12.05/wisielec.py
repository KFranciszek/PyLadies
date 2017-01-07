# Uproszczona wersja gry 'Wisielec'

from random import choice

words = ['KOT', 'PIES', 'PYTHON', 'KUBEK', 'MAMA', 'TATA', 'LAMPA', 'KOMPUTER', 'FOTEL', 'NOC', 'PARASOLKA', 'DESZCZ', 'SOBOTA', 'PIZZA', 'PIWO', 'WINO', 'BUKA', 'MARIO', 'KONSOLA', 'KEBAB']
theWord = choice(words)
exitCommand = 'EXIT'
hiddenWord = ''
count = 0

for letter in theWord:
    hiddenWord += letter.replace(letter, '*')

while hiddenWord != theWord:
    print('\nHaslo: {}'.format(hiddenWord))
    guess = input('Odgadnij litere: ').upper()
    if guess in theWord:
        for i in range(len(theWord)):
            if theWord[i] == guess:
                hiddenWord = hiddenWord[:i] + guess + hiddenWord[i +1:]
        count += 1
    elif guess == exitCommand:
        hiddenWord = theWord
    else:
        count += 1

if hiddenWord == theWord and guess != exitCommand:
    print('\nZgadles! Haslo to: {}\nLiczba wykorzystanych tur: {}\n'.format(hiddenWord, count))
else:
    print('\nPrzegrales. Haslo to: {}\nLiczba wykorzystanych tur: {}\n'.format(hiddenWord, count))
