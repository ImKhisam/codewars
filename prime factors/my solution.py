def sum_for_list(lst):
    prime_factors = []
    mod_lst = [abs(x) for x in lst]
    for n in mod_lst:
        if n < 4:
            if n not in prime_factors:
                prime_factors.append(n)
        arr = []
        while n > 1:
            for i in range(2, int(2 + n // 2)):
                if i == (1 + n // 2):
                    arr.append(n)
                    n = n // n
                if n % i == 0:
                    arr.append(i)
                    n = n // i
                    break
        for x in arr:
            if x not in prime_factors:
                prime_factors.append(x)
    res = []

    prime_factors = sorted(prime_factors)

    for elem in prime_factors:
        res.append([elem, sum([x for x in lst if x % elem == 0])])

    return res

l = [-29804, -4209, -28265, -72769, -31744]

print(sum_for_list(l))
