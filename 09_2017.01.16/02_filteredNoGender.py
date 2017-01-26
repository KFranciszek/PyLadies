#! /usr/bin/python3

from pprint import pprint as pp
import star_wars_characters

sw_data = star_wars_characters.sw_data

def filteredNoGender(lst):
    no_gender = list(filter(lambda a: a['gender'] == 'none' or a['gender'] == 'n/a', lst))
    pp(no_gender)

filteredNoGender(sw_data)
