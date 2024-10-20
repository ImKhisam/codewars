def print_pieces(coords):
    res = ''
    
    return res


def break_pieces(shape):
    res = []
    coords = []
    for i, x in enumerate(shape.split('\n')[1::]):
        for j, s in enumerate(x):
            if s == '+':
                coords.append((i, j))
    return coords

s = '\n+------------+\n|            |\n|            |\n|            |\n+------------+'
'''
    +------------+
    |            |
    |            |
    |            |
    +------------+
'''

print(break_pieces(s))
