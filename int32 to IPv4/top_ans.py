from ipaddress import IPv4Address

def int32_to_ip(int32):
    return str(IPv4Address(int32))


x = 2154959208
y = 0
z = 2149583361

print('bla')
print(int32_to_ip(x))
print(int32_to_ip(y))
print(int32_to_ip(z))
