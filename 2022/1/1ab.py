from functools import reduce

file = 'input.txt'
with open(file) as f:
    calories = [[int(ll) for ll in l.split()] for l in f.read().split(sep='\n\n') ]
    
calories_by_elf = [reduce((lambda x, y: x + y), l) for l in calories]

# part 1
print(f'Part 1 solution: {max(calories_by_elf)}')

# part 2
n = 3
total_n_calories = 0

for i in range(n):
    max_c = max(calories_by_elf)
    total_n_calories += max_c
    calories_by_elf.remove(max_c)
print(f'Part 2 solution: {total_n_calories}')