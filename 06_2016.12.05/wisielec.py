# Uproszczona wersja gry 'Wisielec'
#! /usr/bin/python3

from random import choice

words = ['KOT', 'PIES', 'PYTHON', 'KUBEK', 'MAMA', 'TATA', 'LAMPA', 'KOMPUTER', 'FOTEL', 'NOC', 'PARASOLKA', 'DESZCZ', 'SOBOTA', 'PIZZA', 'PIWO', 'WINO', 'BUKA', 'MARIO', 'KONSOLA', 'KEBAB']
theWord = choice(words)
exitCommand = 'EXIT'
hiddenWord = ''
count = 0
guessedLetters = []

def oneLetterGuess(letter):
    global guessedLetters, theWord, count, hiddenWord
    if letter not in guessedLetters:
        if letter in theWord:
            count += 1
            for i in range(len(theWord)):
                if theWord[i] == letter:
                    hiddenWord = hiddenWord[:i] + letter + hiddenWord[i +1:]
        else:
            count += 1
        guessedLetters += letter
    else:
        print('Juz probowales ta litere.')

for letter in theWord:
    hiddenWord += letter.replace(letter, '*')

while hiddenWord != theWord:
    print('\n')
    print('-' * 20)
    print('Wykorzystane tury: {}'.format(count))
    print('Wykorzystane litery: {}'.format(guessedLetters))
    print('\nHaslo: {}'.format(hiddenWord))
    guess = input('Odgadnij litere/slowo: ').upper()
    if guess.isalpha():
        if guess == exitCommand:
            hiddenWord = theWord
        elif len(guess) == 1:
            oneLetterGuess(guess)
        elif guess == theWord:
            count += 1
            hiddenWord = theWord
    else:
        print('Musisz podac litere.')

if hiddenWord == theWord and guess != exitCommand:
    print('\n')
    print('-' * 20)
    print('Zgadles! Haslo to: {}\nLiczba wykorzystanych tur: {}\n'.format(hiddenWord, count))
else:
    print('\n')
    print('-' * 20)
    print('Przegrales. Haslo to: {}\nLiczba wykorzystanych tur: {}\n'.format(hiddenWord, count))
