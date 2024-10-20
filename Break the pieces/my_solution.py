def print_pieces(x):
    res = ''
    h = x[0]
    l = x[1]
    for x in range(h):
        if x == 0:
            res += ('+' + l * '-' + '+' + '\n')
        elif x == h - 1:
            res += ('+' + l * '-' + '+')
        else:
            res += ('|' + l * ' ' + '|' + '\n')
    return res


def break_pieces(shape):
    res = []
    shapes_list = []
    l = 0
    h = len(shape.split('\n')) - 1
    for x in shape.split('\n'):
        for i, s in enumerate(x):
            if s == '+' and i == 0:
                k = 0
            elif s == '-':
                k += 1
            elif s == '+' and i == len(x) - 1:
                l = k
    shapes_list.append((h, l))
    for x in shapes_list:
        res.append(print_pieces(x))
    return res

s = '\n+------------+\n|            |\n|            |\n|            |\n+------------+'

print(break_pieces(s))
