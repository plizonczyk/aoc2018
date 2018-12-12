def solve(filename):
    with open(filename) as fp:
        lines = list(map(lambda x: x.strip(), fp.readlines()))
        state = lines[0]
        modifiers = set(lines[1:])

    added_to_left = 0
    print(state)
    for _ in range(20):
        while not state.startswith('...'):
            added_to_left += 1
            state = '.' + state

        while not state.endswith('...'):
            state += '.'

        new_state = '..'
        for i in range(2, len(state) - 2):
            new_state += '#' if state[i-2:i+3] in modifiers else '.'

        state = new_state
        print(state)    

    plants_sum = sum([i - added_to_left for i, symbol in enumerate(state) if symbol == '#'])
    return plants_sum

assert solve('easy_input') == 325
print(solve('input'))
