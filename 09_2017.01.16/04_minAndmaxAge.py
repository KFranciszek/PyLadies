#! /usr/bin/python3

from pprint import pprint as pp
import star_wars_characters

sw_data = star_wars_characters.sw_data
sw_data4 = list(filter(lambda a:a.get('birth_year') != 'unknown', sw_data))

def minAge(lst):
    min_age = min(lst, key=lambda a:float(a['birth_year'].strip('BBY')))
    pp(min_age)

def maxAge(lst):
    max_age = max(lst, key=lambda a:float(a['birth_year'].strip('BBY')))
    pp(max_age)

minAge(sw_data4)
maxAge(sw_data4)
