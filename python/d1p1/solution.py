lines = []
with open('input') as fp:
    lines = fp.readlines()

freq = 0
for line in lines:
    freq += (1 if line[0] == '+' else (-1)) * int(line.strip()[1:])

print(freq)
