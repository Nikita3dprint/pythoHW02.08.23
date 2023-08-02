for s in range(1000000):
    z = s
    n = 1
    while s >= 20:
        s = s - 20
        n = n * 2
    if n == 1024:
        print(z - 1)
        break
