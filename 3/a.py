#!/usr/bin/env python3
# -*- coding: utf-8 -*-

total = 0
with open("input.txt") as f:
    for line in f:
        line = line.strip()
        first, second = line[: len(line) // 2], line[len(line) // 2 :]
        common = list(set(first) & set(second))[0]
        total += ord(common) - 96 if common.islower() else ord(common) - 38

print(total)
