#! /usr/bin/python3

from pprint import pprint as pp
import star_wars_characters

sw_data = star_wars_characters.sw_data

#Określam, jak wyglądają dane odbiegające od reguły.
filteredInvalidBMI = list(filter(lambda a: not a['mass'].isdigit() or not a['height'].isdigit(), sw_data))

def dataPrep(lst):
    sw_data3 = list(filter(lambda a: a['mass'] != 'unknown' and a['height'] != 'unknown', lst))
    for a in range(len(sw_data3)):
        if ',' in sw_data3[a]['mass']:
            sw_data3[a]['mass'] = sw_data3[a]['mass'].replace(',', '')
    for i in range(len(sw_data3)):
        sw_data3[i]['bmi'] = round((float(sw_data3[i]['mass'])/float(sw_data3[i]['height'])**2) * 10000, 2)
    return sw_data3


def minBMI(lst):
    min_BMI = min(dataPrep(lst), key=lambda a:a['bmi'])
    pp(min_BMI)

def maxBMI(lst):
    max_BMI = max(dataPrep(lst), key=lambda a:a['bmi'])
    pp(max_BMI)

minBMI(sw_data)
maxBMI(sw_data)
