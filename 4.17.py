a = [int(x) for x in open('17var4.txt')]
k = 0
mnsum = 20001
for i in range(len(a)-1):
    if (a[i] % 5 == 0) and (a[i+1] % 5 == 0):
        k += 1
        if a[i] + a[i+1] < mnsum:
            mnsum = a[i] + a[i+1]
print(k, mnsum)
