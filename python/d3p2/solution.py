from collections import defaultdict

lines = []
with open('input') as fp:
    lines = fp.readlines()

# dumb solution with bad space and time complexity, and dict as data structure cuz lazy
fabric_cells = defaultdict(set)
not_overlapping = set()

for line in lines:
    claim_id, _, offset, size = line.split(' ')
    claim_id = int(claim_id[1:])
    offset_x, offset_y = map(int, offset.strip(':').split(','))
    size_x, size_y = map(int, size.split('x'))
    not_overlapping.add(claim_id)

    for x in range(offset_x, offset_x + size_x):
        for y in range(offset_y, offset_y + size_y):
            fabric_cells[(x, y)].add(claim_id)
            if len(fabric_cells[(x, y)]) >= 2:
                not_overlapping -= fabric_cells[(x, y)]

print(not_overlapping)