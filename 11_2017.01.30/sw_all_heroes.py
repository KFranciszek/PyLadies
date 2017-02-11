#!/usr/bin/python
# -*- coding: UTF-8 -*-

import json

py_10_2File = open('py_10_2', 'r')
py_10_2Content = py_10_2File.read()
swList = json.loads(py_10_2Content)
swListFiltered = list(filter(lambda a: a['name'] != 'unknown' and a['mass'] != 'unknown' and a['gender'] != 'unknown' and a['gender'] != 'n/a', swList))

with open('sw_all_heroes', 'w') as file:
	for character in swListFiltered:
		if character['gender'] == 'male':
			file.write('{} wazy {} kg i jest mezczyzna.\n'.format(character['name'], character['mass']))
		elif character['gender'] == 'female':
			file.write('{} wazy {} kg i jest kobieta.\n'.format(character['name'], character['mass']))
		else:
			file.write('{} wazy {} kg i jest hermafrodyta.\n'.format(character['name'], character['mass']))

py_10_2File.close()
