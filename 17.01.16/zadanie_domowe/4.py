#! /usr/bin/python3
from pprint import pprint as pp
import star_wars_planets

data = star_wars_planets.data
data_4 = list(filter(lambda a: a['diameter'] != 'unknown', data))

def smallest_planet(lst):
    smallestPlanet = min(lst, key=lambda a:int(a['diameter']))
    pp(smallestPlanet)

def biggest_planet(lst):
    biggestPlanet = max(lst, key=lambda a:int(a['diameter']))
    pp(biggestPlanet)

smallest_planet(data_4)
biggest_planet(data_4)
