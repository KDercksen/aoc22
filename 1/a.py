#!/usr/bin/env python3
# -*- coding: utf-8 -*-

with open("input.txt") as f:
    print(
        max(
            [
                sum([int(x) for x in y.split("\n")])
                for y in list(map(str.strip, f.read().split("\n\n")))
            ]
        )
    )
