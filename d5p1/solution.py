from collections import defaultdict
from datetime import datetime

with open('input') as fp:
    line = [letter for letter in fp.readline()]

ASCII_DIFF = ord('a') - ord('A')

index = 0
while index + 1 < len(line):
    if abs(ord(line[index+1]) - ord(line[index])) == ASCII_DIFF:
        del line[index+1]
        del line[index]
        if index > 0:
            index -= 1
    else:
        index += 1

print(len(line))
