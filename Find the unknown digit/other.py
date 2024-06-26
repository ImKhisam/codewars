def solve_runes(runes):
    for c in sorted(set('0123456789') - set(runes)):
        s = runes.replace('?', c).replace('-', ' - ').replace('+', ' + ').replace('*', ' * ').replace('=', ' == ')
        if not any(e[0] == '0' and e != '0' for e in s.split()) and eval(s): return int(c)
    return -1


def solve_runes(runes):
    # Sorted set subtraction returns a list of elements in the first set that weren't in the second
    for i in sorted(set('0123456789')-set(runes)):
        # Prepare string for eval
        eval_string = runes.replace('?', str(i)).replace('=','==')
        # Python 3 gives an error if an int starts with 0.
        # We use it for our advantage. Also check that result is not 00
        try:
            if eval(eval_string) and eval_string[-4:] != '==00':
                return int(i)
        except:
            continue
    return -1