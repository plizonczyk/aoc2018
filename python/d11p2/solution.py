import numpy as np
from scipy.signal import convolve2d
from functools import partial

def cell_power_level(x, y, serial_number):
    rack_id = x + 1 + 10
    power_level = ((rack_id * (y + 1)) + serial_number) * rack_id
    hundreds = power_level // 100 - (power_level // 1000) * 10
    return hundreds - 5

assert cell_power_level(3 - 1, 5 - 1, 8) == 4
assert cell_power_level(122 - 1, 79 - 1, 57) == -5
assert cell_power_level(217 - 1, 196 - 1, 39) == 0
assert cell_power_level(101 - 1, 153 - 1, 71) == 4

def get_grid(serial_number):
    fn = partial(cell_power_level, serial_number=serial_number)
    return np.fromfunction(fn, (300, 300))

def get_max_cell_square(serial_number):
    grid = get_grid(serial_number)
    # brute lol, using reasonably written sliding window would be much faster for large sizes
    maxes = []
    for size in range(1, 301):
        if size % 30 == 0:
            print ('Size {} of 300'.format(size))
        summed = convolve2d(grid, np.ones((size, size)), mode='valid')
        max_x, max_y = np.unravel_index(summed.argmax(), summed.shape)
        maxes.append((summed[max_x, max_y], max_x + 1, max_y + 1, size))
        
    return max(maxes)[1:]

# assert get_max_cell_square(18) == (90, 269, 16)
# assert get_max_cell_square(42) == (232, 251, 12)

print(get_max_cell_square(1718))