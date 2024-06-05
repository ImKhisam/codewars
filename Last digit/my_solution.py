D = [(0,), (1,), (2, 4, 8, 6), (3, 9, 7, 1), (4, 6),
     (5,), (6,), (7, 9, 3, 1), (8, 4, 2, 6), (9, 1)]


def last_digit(a, b):
    if b == 0:
        return 1
    return D[a % 10][(b - 1) % 4]


print(last_digit(3, 10))
