from itertools import cycle
from collections import Counter

lines = []
with open('input') as fp:
    lines = fp.readlines()

lines = sorted(lines)

for line1, line2 in zip(lines[:-1], lines[1:]):
    diff = 0
    for letter1, letter2 in zip(line1, line2):
        diff += 1 if letter1 != letter2 else 0

    if diff == 1:
        print(line1, line2)
        break
