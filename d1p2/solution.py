from itertools import cycle

lines = []
with open('input') as fp:
    lines = fp.readlines()

freq = 0
freqs_found = set()
for line in cycle(lines):
    freq += (1 if line[0] == '+' else (-1)) * int(line.strip()[1:])
    if freq in freqs_found:
        break
    else:
        freqs_found.add(freq)

print(freq)
