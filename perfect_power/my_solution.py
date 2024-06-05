from math import log, sqrt


def isPP(n):
    n = int(n)
    if n < 4:
        return None

    sr = round(sqrt(n), 6)
    print(sr)

    if sr == round(sr):
        return [int(sr), 2]

    for m in range(2, round(n/2)):
        k = round(log(n, m), 6)
        if k == round(k):
            return [int(m), int(k)]

    return None


x = 343

print(isPP(x))
