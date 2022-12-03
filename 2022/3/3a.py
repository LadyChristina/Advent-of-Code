file = 'input.txt'

def to_priority(letter):
    return ord(letter) - ord('a') + 1 + letter.isupper() * (ord('a') - ord('A') + 26)
    
priority_sum = 0
with open(file) as f:
    for rucksack in f.readlines():
        compartment1, compartment2 =  set(rucksack[:len(rucksack)//2]), set(rucksack[len(rucksack)//2:])
        priority_sum += to_priority((compartment1 & compartment2).pop())
        
print(f'Solution: {priority_sum}')