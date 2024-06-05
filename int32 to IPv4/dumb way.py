def int32_to_ip(int32):
    result = ''
    number = int32
    if int32 == 0:
        result = '0'
    elif int32 == 1:
        result = '1'
    else:
        while number != 1:
            if (number % 2) == 0:
                result += '0'
            else:
                result += '1'
            number = number // 2

        result = result[::-1]

        result = '1' + result


    while len(result) != 32:
        result = '0' + result

    p1 = result[0:8]
    p2 = result[8:16]
    p3 = result[16:24]
    p4 = result[24:33]

    return str(int(p1, 2)) + "." + str(int(p2, 2)) + "." + str(int(p3, 2)) + "." + str(int(p4, 2))


x = 2154959208
y = 0
z = 2149583361

print(int32_to_ip(x))
print(int32_to_ip(y))
print(int32_to_ip(z))
