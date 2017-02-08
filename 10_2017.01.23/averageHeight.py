#!/usr/bin/python
# -*- coding: UTF-8 -*-

from swDict import swDict
from pprint import pprint as pp

colorAndHeight = {}
for name, traits in swDict.items():
	if swDict[name]['eye_color'] not in colorAndHeight:
		colorAndHeight[swDict[name]['eye_color']] = [swDict[name]['height']]
	else:
		colorAndHeight[swDict[name]['eye_color']].append(swDict[name]['height'])

for color, height in colorAndHeight.items():
	print('Sredni wzrost osob z kolorem oczu {} wynosi {} cm.'.format(color, round(sum(colorAndHeight[color])/len(colorAndHeight[color]), 2)))
