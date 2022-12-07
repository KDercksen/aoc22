#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re

stack_idxs = [1, 5, 9, 13, 17, 21, 25, 29, 33]
stacks = [[] for _ in range(9)]
instructions = []

with open("input.txt") as f:
    for i, line in enumerate(f):
        if 0 <= i <= 7:
            for s, idx in enumerate(stack_idxs):
                if not (crate := line[idx]).isspace():
                    stacks[s].insert(0, line[idx])
        elif i >= 10:
            instructions.append([int(x) for x in re.findall(r"(\d+)", line)])

for num, src, dest in instructions:
    stacks[dest - 1].extend(stacks[src - 1][-num:])
    stacks[src - 1] = stacks[src - 1][:-num]

print("".join([x[-1] for x in stacks]))
