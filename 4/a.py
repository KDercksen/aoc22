#!/usr/bin/env python3
# -*- coding: utf-8 -*-

pairs = 0
with open("input.txt") as f:
    for line in f:
        one, two = line.split(",")
        one_start, one_end = map(int, one.split("-"))
        two_start, two_end = map(int, two.split("-"))
        first, second = (
            set(range(one_start, one_end + 1)),
            set(range(two_start, two_end + 1)),
        )
        if first.issubset(second) or second.issubset(first):
            pairs += 1

print(pairs)
