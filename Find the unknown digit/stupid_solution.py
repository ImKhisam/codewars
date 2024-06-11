def given_digits(runes, a, b, c):
    res = []
    if runes[runes.index("?")-1] == "+" or runes[runes.index("?")-1] == "-" or runes[runes.index("?")-1] == "*" \
            or runes.split('=')[1][0:2] == '??' or runes[0:2] == "??" \
            or (len(runes.split('=')[1]) > 1 and runes.split('=')[1][0] == '?') \
            or (a.split('+')[1][0:2] == '10' and len(a.split('+')[1]) - 1 > len(a.split('+')[0])) \
            or (b.split('+')[1][0:2] == '10' and len(b.split('+')[1]) - 1 > len(b.split('+')[0])):
        res.append(0)
    for x in runes:
        if x.isdigit():
            res.append(int(x))
    return res


def count_parts(a, b, c):
    res = ''
    for elem in [a, b, c]:
        if elem[0] == '-':
            elem_minus = 1
            elem = elem[1::]
        else:
            elem_minus = 0
        sum_num, sum_ques = 0, 0
        for k, s in enumerate(elem[::-1]):
            if s == '?':
                sum_ques += (10 ** k) if elem_minus == 0 else (-(10 ** k))
            else:
                sum_num += ((10 ** k) * int(s)) if elem_minus == 0 else (-(10 ** k) * int(s))

        res += str(sum_num) + '+' + str(sum_ques) + 'x'
        res = res.replace('+0?', '')
        res += '/'
    res = res[:-1]
    a, b, c = res.split('/')
    return a, b, c


def check(a, b, c, op, used_digits):
    for i in range(0, 10):
        if i not in used_digits:
            res = []
            for elem in [a, b, c]:
                if '+' in elem:
                    elem = elem.replace('x', '')
                    res.append(int(elem.split('+')[0]) + int(elem.split('+')[1]) * i)
            if op == '*':
                s = res[0] * res[1]
            elif op == '+':
                s = res[0] + res[1]
            else:
                s = res[0] - res[1]
            if s == res[2]:
                return i
    return -1


def solve_runes(runes):
    l, c = runes.split('=')
    if '*' in l:
        op = '*'
        a, b = l.split('*')
    elif '+' in l:
        op = '+'
        a, b = l.split('+')
    else:
        op = '-'
        if '--' in l:
            y, x = l[::-1].split('--')
            a = x[::-1]
            b = '-' + y[::-1]
        else:
            a = ''
            if l[0] == '-':
                l = l[1::]
                a = '-'
            a += l.split('-')[0]
            b = l.split('-')[1]

    a, b, c = count_parts(a, b, c)
    print(a, b, c)
    used_digits = given_digits(runes, a, b, c)
    return check(a, b, c, op, used_digits)

print(solve_runes("123?45*?=?"))
