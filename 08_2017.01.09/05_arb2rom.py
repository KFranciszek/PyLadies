#! /usr/bin/python3
# -*- coding: utf-8 -*-

# Convert numbers from arabic to roman notation

def arb_2_rom(arabic_number):
    arb2rom_conversion = [[1000, 'M'], [900, 'CM'], [500, 'D'], [400, 'CD'], [100, 'C'], [90, 'XC'], [50, 'L'], [40, 'XL'], [10, 'X'], [9, 'IX'], [5, 'V'], [4, 'IV'], [1, 'I']]

    roman_number = ''
    for arb_digit, rom_digit in arb2rom_conversion:
        while arabic_number >= arb_digit:
            roman_number += rom_digit
            arabic_number -= arb_digit
    return roman_number
