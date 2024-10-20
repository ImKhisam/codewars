class Rectangle:
    def __init__(self, a, b, c, d):
        self.a = a
        self.b = b
        self.c = c
        self.d = d

def break_pieces(shape):
    res = []
    coords = []
    for i, x in enumerate(shape.split('\n')[1::]):
        for j, s in enumerate(x):
            if s == '+':
                coords.append((i, j))
    return coords
