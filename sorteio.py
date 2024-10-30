#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 10 23:25:47 2024

@author: jomaia
"""
import random

def sorte():
    cap = random.randint(1, 24)

    if cap == 1 or cap == 20:
        ponto = random.randint(1, 7)
    elif cap == 2 or cap == 4 or cap == 9:
        ponto = random.randint(1, 12)
    elif cap == 3 or cap == 11 or cap == 24:
        ponto = random.randint(1, 14)
    elif cap == 5 or cap == 7 or cap == 12 or cap == 15 or cap == 22:
        ponto = random.randint(1, 10)
    elif cap == 6 or cap == 8 or cap == 14 or cap == 19:
        ponto = random.randint(1, 9)
    elif cap == 10 or cap == 18:
        ponto = random.randint(1, 6)
    elif cap == 13 or cap == 23:
        ponto = random.randint(1, 8)
    elif cap == 16:
        ponto = random.randint(1, 11)
    elif cap == 17 or cap == 21:
        ponto = random.randint(1, 15)
    sorteado = f'capitulo {cap}, {ponto}'
    return sorteado
