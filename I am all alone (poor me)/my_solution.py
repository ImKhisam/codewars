def all_alone(house):
    for i in range(len(house)):
        if 'X' in house[i]:
            xs = i
            xc = house[i].index('X')
    next_point = [(xs,xc)]
    while next_point:
        a, b = next_point.pop(0)
        for x, y in (((a,b+1),(a,b-1),(a+1,b),(a-1,b))):
            if house[x][y] == ' ':
                house[x][y] = '1'
                next_point.append((x,y))
            elif house[x][y] == 'o':
                return True
    return False

house = [
            list("  o                o        #######"),
            list("###############             #     #"),
            list("#             #        o    #     #"),
            list("#  X          ###############     #"),
            list("#                                 #"),
            list("###################################")
        ]
