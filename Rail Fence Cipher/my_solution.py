from itertools import tee, zip_longest


def encode_rail_fence_cipher(string, n):
    res = ['' for i in range(n)]
    direction = 1
    counter = 0
    for s in string:
        res[counter] += s
        if counter == n - 1:
            direction = -1
        elif counter == 0:
            direction = 1
        counter += direction

    return ''.join(res)


def decode_rail_fence_cipher(string, n):
    res = [[] for _ in range(n)]
    res += res[-2:0:-1]
    for t in zip_longest(*[iter(range(len(string)))]*len(res)):
        for a, b in zip(res, t):
            if b is None: break
            a.append(b)
    return "".join(v[1] for v in sorted(zip(sum(res, []), string)))


#def decode_rail_fence_cipher(string, n):
#    str_k = n * 2 - 2
#    lengths = [len(string[i::str_k]) for i in range(str_k)]
#    for i, l in enumerate(lengths):
#        if i == 0 or i == n - 1:
#            pass
#        else:
#            lengths[i] += lengths.pop(-1)
#    s = []
#    st_ind = 0
#    end_ind = 0
#    for i in range(len(lengths)):
#        end_ind += lengths[i]
#        s.append(string[st_ind:end_ind])
#        st_ind += lengths[i]
#    print(s)
#    for i in range(len(s) - 1):
#        if i == 0:
#            pass
#        else:
#            new_s = s[i][1::2]
#            s[i] = s[i][::2]
#            if i == 1:
#                s.append(new_s)
#            else:
#                s.insert((1 - i), new_s)
#    print(s)
#    lengths = [len(s[i]) for i in range(len(s))]
#
#    res = ''
#    for i in range(max(lengths)):       # 0 - 12
#        for j in range(len(s)):         # 0 - 3
#            if i < len(s[j]):
#                res += s[j][i]
#    return res
#print(encode_rail_fence_cipher("WEAREDISCOVEREDFLEEATONCE", 6))
print(decode_rail_fence_cipher("WVTEOEAOACRENRSEECEIDLEDF", 6))
'''
WEAREDISCOVEREDFLEEATONCE
W       E       C       R       L       T       E
  E   R   D   S   O   E   E   F   E   A   O   C  
    A       I       V       D       E       N    
WECRLTEERDSOEEFEAOCAIVDEN
Hello, World!   
Hoo!el,Wrdl l   3
H !e,Wdloollr   4
'''
