file = 'input.txt'

def to_priority(letter):
    return ord(letter) - ord('a') + 1 + letter.isupper() * (ord('a') - ord('A') + 26)

with open(file) as f:
    rucksacks = f.read().splitlines() 
    
badges = [(set(rucksacks[i]) & set(rucksacks[i+1]) & set(rucksacks[i+2])).pop() for i in range(0, len(rucksacks), 3)]
priority_sum = sum(map(to_priority, badges))
        
print(f'Solution: {priority_sum}')