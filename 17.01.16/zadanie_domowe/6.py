#! /usr/bin/python3
from pprint import pprint as pp
import star_wars_planets

data = star_wars_planets.data
data_6 = list(filter(lambda a: a['diameter'] != 'unknown' and a['orbital_period'] != 'unknown' and a['diameter'] != '0' and a['orbital_period'] != '0', data))
for i in range(len(data_6)):
	data_6[i]['Diameter_OrbPeriodRatio'] = int(data_6[i]['diameter'])/int(data_6[i]['orbital_period'])


def min_ratio(lst):
    minRatio = min(lst, key=lambda a:a['Diameter_OrbPeriodRatio'])
    pp(minRatio)

def max_ratio(lst):
    maxRatio = max(lst, key=lambda a:a['Diameter_OrbPeriodRatio'])
    pp(maxRatio)

min_ratio(data_6)
max_ratio(data_6)
