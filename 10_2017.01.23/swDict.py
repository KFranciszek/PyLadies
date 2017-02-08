#!/usr/bin/python
# -*- coding: UTF-8 -*-
from pprint import pprint as pp

sw_dataFile = open('sw_data.txt', 'r')
sw_list = sw_dataFile.readlines()
sw_dict = {}

for i in range(len(sw_list)):
	sw_dict[sw_list[i][sw_list[i].find(' '):sw_list[i].find('has')].strip(' ')] = {}
	sw_dict[sw_list[i][sw_list[i].find(' '):sw_list[i].find('has')].strip(' ')]['eye_color'] = sw_list[i][sw_list[i].find('has')+3:sw_list[i].find('and')].strip(' ')
	sw_dict[sw_list[i][sw_list[i].find(' '):sw_list[i].find('has')].strip(' ')]['height'] = int(sw_list[i][sw_list[i].find(' is ')+3:sw_list[i].find('cm')].strip(' '))

pp(sw_dict)
