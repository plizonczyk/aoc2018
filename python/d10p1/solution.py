with open('easy_input') as fp:
    data = fp.readlines()

positions = [tuple(map(int, line.split('<')[1].split('>', 1)[0].split(','))) for line in data]
velocities = [tuple(map(int, line.split('<')[-1].rstrip('>\n').split(','))) for line in data]

for pos, vel in zip(positions, velocities):
    print(pos, vel)

def advance_positions(positions, velocities, n):
    return [(pos[0] + vel[0] * n, pos[1] + vel[1] * n) for pos, vel in zip(positions, velocities)]

def print_message(positions):
    offset_x, offset_y = min(positions)[0], min(positions, key=lambda x: x[1])[1]
    minus_offset = [(x - offset_x, y - offset_y) for x, y in positions]

    size_x, size_y = max(minus_offset)[0], max(minus_offset, key=lambda x: x[1])[1]
    grid = [[' ' for _ in range(size_x + 1)] for _ in range(size_y + 1)]

    for x, y in minus_offset:
        grid[y][x] = '#'

    for line in grid:
        print(''.join(line))

    print('----------------------------------------------------------------')

print_message(advance_positions(positions, velocities, 0))
print_message(advance_positions(positions, velocities, 1))
print_message(advance_positions(positions, velocities, 2))
print_message(advance_positions(positions, velocities, 3))
print_message(advance_positions(positions, velocities, 4))