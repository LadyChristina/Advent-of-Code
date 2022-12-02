def let2num(letter):
    if letter in ['A', 'X']:
        return 1
    if letter in ['B', 'Y']:
        return 2
    if letter in ['C', 'Z']:
        return 3
    raise ValueError('Invalid input')
    
def winning_move(move):
    return move % 3 + 1

def calculate_points(moves):
    opponent_move, my_move = moves
    loss, draw, win = 0, 3, 6
    if opponent_move == my_move:
        return my_move + draw
    if opponent_move == winning_move(my_move):
        return my_move + loss
    return my_move + win
    
file = 'input.txt'    
with open(file) as f:
    rounds = [l.split() for l in f.read().split(sep='\n') ]
    
rounds = [tuple(map(let2num, r)) for r in rounds]
points = (list(map(calculate_points, rounds)))

print(f'Solution: {sum(points)}')