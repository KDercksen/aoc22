#!/usr/bin/env python3
# -*- coding: utf-8 -*-

convert = {"A": 1, "B": 2, "C": 3, "X": 1, "Y": 2, "Z": 3}
scores = [[3, 6, 0], [0, 3, 6], [6, 0, 3]]

total = 0
with open("input.txt") as f:
    for line in f:
        one, two = list(map(str.strip, line.split()))
        total += convert[two] + scores[convert[one] - 1][convert[two] - 1]

print(total)
