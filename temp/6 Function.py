# -*- coding: utf-8 -*-
"""
Created on Fri Jun 20 15:40:26 2025

@author: subah
"""

def is_leap(year):
    leap = False
    
    if (year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)):
      leap = True
    
    return leap

year = int(input())

print(is_leap(year))