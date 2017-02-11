#!/usr/bin/python
# -*- coding: UTF-8 -*-

from pprint import pprint as pp
import json

py_10_2File = open('py_10_2', 'r')
py_10_2Content = py_10_2File.read()
py_10_2AsPythonValue = json.loads(py_10_2Content)

sw_womenFile = open('sw_women.txt', 'w')
sw_menFile = open('sw_men.txt', 'w')

for i in range(len(py_10_2AsPythonValue)):
    if py_10_2AsPythonValue[i]['gender'] == 'female':
        sw_womenFile.write(py_10_2AsPythonValue[i]['name'] + '\n')
    elif py_10_2AsPythonValue[i]['gender'] == 'male':
        sw_menFile.write(py_10_2AsPythonValue[i]['name'] + '\n')

sw_womenFile.close()
sw_menFile.close()
py_10_2File.close()
