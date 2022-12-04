file = 'input.txt'

fully_overlapping_chores = 0
with open(file) as f:
    for pair in f.read().splitlines():
        chores = [chores.split('-') for chores in pair.split(',')]
        chores1, chores2 = list(map(lambda x: range(int(x[0]), int(x[1])+1), chores))
        if all(chore in chores2 for chore in chores1) or all(chore in chores1 for chore in chores2):
            fully_overlapping_chores += 1 
            
print(f'Solution: {fully_overlapping_chores}')
    