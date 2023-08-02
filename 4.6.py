for s in range(10000):
    z = s
    n = 1
    while s >= 10:
        s = s - 10
        n = n * 3
    if n == 729:
        print(z - 1)
        break
