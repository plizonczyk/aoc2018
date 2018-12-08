from collections import defaultdict

lines = []
with open('input') as fp:
    lines = fp.readlines()

# dumb solution with bad space and time complexity, and dict as data structure cuz lazy
fabric_cells = defaultdict(int)

for line in lines:
    _, _, offset, size = line.split(' ')
    offset_x, offset_y = map(int, offset.strip(':').split(','))
    size_x, size_y = map(int, size.split('x'))

    for x in range(offset_x, offset_x + size_x):
        for y in range(offset_y, offset_y + size_y):
            fabric_cells[(x, y)] += 1

print(len(list(filter(lambda x: x >= 2, fabric_cells.values()))))