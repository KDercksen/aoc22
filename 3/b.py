#!/usr/bin/env python3
# -*- coding: utf-8 -*-

total = 0
with open("input.txt") as f:
    lines = list(map(str.strip, f.readlines()))
    for i in range(0, len(lines), 3):
        first, second, third = lines[i : i + 3]
        common = list(set(first) & set(second) & set(third))[0]
        total += ord(common) - 96 if common.islower() else ord(common) - 38

print(total)
