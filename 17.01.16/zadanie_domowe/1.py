#! /usr/bin/python3
from pprint import pprint as pp
import star_wars_planets

data = star_wars_planets.data

def sorted_rotation_period(lst):
    data_1 = list(filter(lambda a:a.get('rotation_period') != 'unknown', lst))
    sortedRotationPeriod = sorted(data_1, key=lambda a:int(a['rotation_period']))
    pp(sortedRotationPeriod)

sorted_rotation_period(data)
