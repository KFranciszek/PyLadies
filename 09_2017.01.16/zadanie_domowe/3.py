#! /usr/bin/python3
from pprint import pprint as pp
import star_wars_planets

data = star_wars_planets.data
data_3 = list(filter(lambda a: a['surface_water'] != '0' and a['surface_water'] != 'unknown' and a['orbital_period'] != 'unknown', data))

def min_orbital_period(lst):
    minOrbitalPeriod = min(lst, key=lambda a:int(a['orbital_period']))
    pp(minOrbitalPeriod)

def max_orbital_period(lst):
    maxOrbitalPeriod = max(lst, key=lambda a:int(a['orbital_period']))
    pp(maxOrbitalPeriod)
    
min_orbital_period(data_3)
max_orbital_period(data_3)
