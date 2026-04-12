def maximum(a, asize):
    counter = 0
    max1 = 0
    for i in range(0, asize):
        if (a[i] == 0):
            counter = 0
        else:
            counter = counter + 1
            max1 = max(max1, counter)
    return max1

a = [1,1,0,0,1,0,0,0,0,1,1,1,1,0,1,0,1,1,0]
asize = len(a)
print("Maximum 1 is =", maximum(a, asize))