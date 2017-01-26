#! /usr/bin/python3

from pprint import pprint as pp
import star_wars_characters

sw_data = star_wars_characters.sw_data

def sortedHeight(lst):
    sorted_height = sorted(lst, key=lambda a: 0 if a['height'] == 'unknown' else int(a['height']))
    pp(sorted_height)

sortedHeight(sw_data)
