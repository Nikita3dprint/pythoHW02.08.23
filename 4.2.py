for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                if ((not(not x or y) or w) or (not z or (y and w))) == 0:
                    print(x, y, z, w)
