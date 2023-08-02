a = [int(x) for x in open('17var3.txt')]
k = 0
mxsum = - 20002
for i in range(len(a)-1):
    if (a[i] % 3 == 0) and (a[i+1] % 3 == 0):
        k = k + 1
        if a[i] + a[i+1] > mxsum:
            mxsum = a[i] + a[i+1]
print(k, mxsum)
