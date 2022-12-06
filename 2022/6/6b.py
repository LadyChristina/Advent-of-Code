file = 'input.txt'

with open(file) as f:
    buffer = f.read().strip()    

marker_size = 14
characters = ''

for c in buffer:
    characters += c
    if c not in characters[-marker_size+1:-1]:
        if len(set(characters[-marker_size:])) == marker_size:
            break  
        
print(f'Solution: {len(characters)}')