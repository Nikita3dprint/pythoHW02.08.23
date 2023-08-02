def mxdel(a):
    for x in range(a-1, 2, -1):
        if a % x == 0:
            return x
    return 0


def mndel(b):
    for y in range(2, b):
        if b % y == 0:
            return y
    return 0


z = 799999
n = 0
while n < 5:
    m = mxdel(z) - mndel(z)
    if (m != 0) and (m % 17 == 0):
        print(z, m)
        n += 1
    z -= 1
