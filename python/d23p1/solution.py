def manhattan(point1, point2):
    return sum(abs(coord1 - coord2) for coord1, coord2 in zip(point1, point2))


def solve(filename):
    points = []
    with open(filename) as fp:
        for line in fp.readlines():
            pos, r = line.split(' ')
            r_num = int(r.lstrip('r='))
            pos_nums = pos.lstrip('pos=<').rstrip('>,').split(',')
            point = list(map(int, pos_nums))
            point.append(r_num)
            points.append(point)

    max_range = max(points, key=lambda x: x[3])
    
    in_range = 0
    for point in points:
        in_range += 1 if manhattan(point[:3], max_range[:3]) <= max_range[3] else 0
    
    return in_range

assert solve('easy_input') == 7
print(solve('input'))
