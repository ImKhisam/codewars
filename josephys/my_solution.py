def josephus(items, k):
    index, res = 0, []
    while len(items) > 0:
        index = (index + k - 1) % len(items)
        res.append(items.pop(index))
    return res


l = [1,2,3,4,5,6,7,8,9,10]
print(josephus(l, 1))
