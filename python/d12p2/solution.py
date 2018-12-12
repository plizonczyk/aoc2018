def solve(filename):
    with open(filename) as fp:
        lines = list(map(lambda x: x.strip(), fp.readlines()))
        state = lines[0]
        modifiers = set(lines[1:])

    added_to_left = 0
    for gen in range(125):
        while not state.startswith('...'):
            added_to_left += 1
            state = '.' + state

        while not state.endswith('...'):
            state += '.'

        new_state = '..'
        for i in range(2, len(state) - 2):
            new_state += '#' if state[i-2:i+3] in modifiers else '.'

        state = new_state

    # after ~125 gens there is stable +42 in plants sum every generation
    plants_sum = sum([i - added_to_left for i, symbol in enumerate(state) if symbol == '#']) + 42 * (50000000000 - 125)
    return plants_sum

print(solve('input'))
