file = 'input.txt'

overlapping_chores = 0
with open(file) as f:
    for pair in f.read().splitlines():
        chores = [chores.split('-') for chores in pair.split(',')]
        chores1, chores2 = list(map(lambda x: range(int(x[0]), int(x[1])+1), chores))
        if any(chore in chores2 for chore in chores1):
            overlapping_chores += 1 
            
print(f'Solution: {overlapping_chores}')