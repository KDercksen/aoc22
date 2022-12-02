#!/usr/bin/env python3
# -*- coding: utf-8 -*-

convert = {"A": 1, "B": 2, "C": 3, "X": 0, "Y": 3, "Z": 6}
scores = [[3, 6, 0], [0, 3, 6], [6, 0, 3]]

total = 0
with open("input.txt") as f:
    for line in f:
        one, two = list(map(str.strip, line.split()))
        aim = scores[convert[one] - 1].index(convert[two])
        total += (aim + 1) + convert[two]

print(total)
