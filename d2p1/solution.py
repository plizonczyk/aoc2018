from itertools import cycle
from collections import Counter

lines = []
with open('input') as fp:
    lines = fp.readlines()

twos = 0
threes = 0
for line in lines:
    counts = Counter(line)
    twos += 1 if any(filter(lambda x: x == 2, counts.values())) else 0
    threes += 1 if any(filter(lambda x: x == 3, counts.values())) else 0

print(twos * threes)
