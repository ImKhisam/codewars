def solve_runes(runes):
    def solver(beginRange, endRange):
        for i in range(beginRange, endRange):
            if str(i) in runes: #pass when encountering an integer already in the equation
                continue
            tempRunes = str(runes.replace("?", str(i)))
            left = tempRunes[:tempRunes.index("=")]
            if str(eval(left)) == tempRunes[tempRunes.index("=")+1:]: #check for solution
                return i
    if runes[runes.index("?")-1] == "+" or runes[runes.index("?")-1] == "-" or runes[runes.index("?")-1] == "*" or runes[runes.index("?")-1] == "/" or runes[0] == "?":
        #prevent 0 as candidate for solution from conflicting with the equations, i.e. integer '0xxx' being treated as 'xxx'
        if solver(1, 10) == None:
            if solver(0, 1) == None: #try zero if no other solution
                return -1
            return solver(0, 1)
        return solver(1, 10)
    if solver(0, 10) == None:
        return -1
    else:
        return solver(0, 10)

print(solve_runes("??*??=302?"))
