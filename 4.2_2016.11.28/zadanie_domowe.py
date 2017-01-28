#!/usr/bin/python
# -*- coding: UTF-8 -*-

from import_this_data import txt
from pprint import pprint

#a)
def isSentences(lst):
    splitLst = lst.split('\n')
    is_sentences = []
    for i in splitLst:
        if 'is' in i:
            is_sentences.append(i)
    pprint(is_sentences)

#b)
def complexSentences(lst):
    splitLst = lst.split('\n')
    complex_sentences = []
    for i in splitLst:
        if ',' in i:
            complex_sentences.append(i)
    pprint(complex_sentences)

#c)
def titleWord2Python(lst):
    splitLst = lst.split('\n')
    python_sentences = []
    for sentence in splitLst:
        splitSentence = sentence.split(' ')
        for word in range(len(splitSentence)):
            if splitSentence[word].istitle():
                splitSentence[word] = 'Python'
        python_sentences.append(' '.join(splitSentence))
    pprint(python_sentences)

#d) Odniesienie do faktu, ze tworca Pythona jest Holender - Guido van Rossum."

isSentences(txt)
complexSentences(txt)
titleWord2Python(txt)
