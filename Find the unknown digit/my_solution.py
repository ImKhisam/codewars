def solve_runes(runes):
    for i in sorted(set('0123456789') - set(runes)):
        s = runes.replace('?', i).replace('-', ' - ').replace('+', ' + ').replace('*', ' * ').replace('=', ' == ')
        if not any(x[0] == '0' and x != '0' for x in s.split()) and eval(s):
            return int(i)
    return -1

print(solve_runes("??*??=302?"))