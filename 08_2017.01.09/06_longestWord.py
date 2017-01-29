#! /usr/bin/python3

def longest_word(senten):
    splitSentence = senten.split(' ')
    return(max(splitSentence, key=len))

sentence = input('\nWpisz zdanie: ')
print('Najdluzsze slowo w zdaniu: {}\n'.format(longest_word(sentence)))
