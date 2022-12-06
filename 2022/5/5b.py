from collections import defaultdict
from math import ceil, floor
import re

file = 'input.txt'

stacks = defaultdict(list)
with open(file) as f:
    a = f.read().splitlines()
    
column_size = 4
num_stacks = ceil(len(a[0]) / column_size)
for line in a:
    if line.startswith(' ') or line.startswith('['):
        for i in range(0, len(line), column_size):
            if line[i] == '[':
                stack_num = floor(i/column_size) + 1
                stacks[stack_num].append(line[i+1])

    if line.startswith('m'):
        crates_to_move, move_from, move_to = [int(d) for d in re.findall(r'\d+', line)]
        for i in range(crates_to_move, 0, -1):
            stacks[move_to].insert(0, stacks[move_from].pop(i-1))
            
top_crates = ''.join([stacks[i][0] for i in range(1, len(stacks) + 1)])
print(f'Solution: {top_crates}')        