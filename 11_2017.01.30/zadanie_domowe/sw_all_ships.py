#!/usr/bin/python
# -*- coding: UTF-8 -*-

import json

with open('py_10_zd', 'r') as py_10_zdFile:
    py_10_zdContent = py_10_zdFile.read()
    swList = json.loads(py_10_zdContent)

swListFiltered = list(filter(lambda a: a['name'] != 'unknown' and a['cost_in_credits'] != 'unknown', swList))
swListFilteredSorted = sorted(swListFiltered, key=lambda a: int(a['cost_in_credits']), reverse=True)

with open('sw_all_ships', 'w') as file:
    for ship in swListFilteredSorted:
        file.write('{} kosztuje {} credits.\n'.format(ship['name'], ship['cost_in_credits']))
