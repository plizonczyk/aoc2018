from collections import defaultdict
from datetime import datetime

with open('input') as fp:
    original_line = fp.readline()

ASCII_DIFF = ord('a') - ord('A')

def react_polymer(line):
    index = 0
    while index + 1 < len(line):
        if abs(ord(line[index+1]) - ord(line[index])) == ASCII_DIFF:
            del line[index+1]
            del line[index]
            if index > 0:
                index -= 1
        else:
            index += 1
    
    return len(line)

results = dict()
for lower in 'abcdefghijklmnopqrstuvwxyz':
    results[lower] = react_polymer([letter for letter in original_line.replace(lower, '').replace(lower.upper(), '')])

print(min(results.items(), key=lambda x: x[1]))
