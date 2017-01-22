#! /usr/bin/python3
from pprint import pprint as pp
import star_wars_planets

data = star_wars_planets.data

def no_water_planets(lst):
    noWaterPlanets = list(filter(lambda a:a.get('surface_water') == '0', lst))
    pp(noWaterPlanets)

no_water_planets(data)
