# -*- coding: utf-8 -*-
"""
Created on Sat Jul 26 16:23:12 2025

@author: subah
"""

if __name__ == '__main__':
    students = []
    
    for _ in range(int(input())):
        name = input()
        score = float(input())
        students.append([name, score])   
        
    scores = [score for name, score in students]
    unique_scores = sorted(set(scores))
    second_lowest = unique_scores[1]

    result = [name for name, score in students if score == second_lowest]
    for name in sorted(result):
        print(name)