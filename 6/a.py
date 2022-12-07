#!/usr/bin/env python3
# -*- coding: utf-8 -*-

with open("input.txt") as f:
    data = f.read().strip()
    seen = set()
    count = 0
    for i, char in enumerate(data):
        if char in seen:
            seen = set(char)
            count = 1
        else:
            seen.add(char)
            count += 1

        if count == 4:
            print(i + 1)
            break
