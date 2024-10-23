from itertools import chain


def fencer(what, n):
    lst = [[] for _ in range(n)]
    x, dx = 0, 1
    for c in what:
        lst[x].append(c)
        if x == n - 1 and dx > 0 or x == 0 and dx < 0: dx *= -1
        x += dx
    return chain.from_iterable(lst)


def encode_rail_fence_cipher(s, n): return ''.join(fencer(s, n))


def decode_rail_fence_cipher(s, n):
    lst = [''] * len(s)
    for c, i in zip(s, fencer(range(len(s)), n)):
        lst[i] = c
    return ''.join(lst)