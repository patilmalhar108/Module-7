def reverse(a, asize, n):
    temp = 0
    while temp < asize:
        start = temp
        end = min(temp + n - 1, asize - 1)
        while start < end:
            a[start], a[end] = a[end], a[start]
            start = start + 1
            end = end - 1
        temp = temp + n
    
a = [2,4,3,44,5,1,66,7,4,35]
n = 2
asize = len(a)
reverse(a, asize, n)
for i in range(0, asize):
    print(a[i], end = " ")