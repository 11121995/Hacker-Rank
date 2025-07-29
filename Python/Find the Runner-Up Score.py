# -*- coding: utf-8 -*-
"""
Created on Tue Jul  1 14:40:55 2025

@author: subah
"""

if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    
    unique_score = list(set(arr))
    unique_score.sort(reverse=True)

print(unique_score[1])