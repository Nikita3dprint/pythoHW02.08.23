for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                if ((not(not x or y) or z) or (not w or (y and z))) == 0:
                    print(x, y, z, w)
        