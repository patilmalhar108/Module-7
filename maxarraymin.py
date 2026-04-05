def min_element(a, size):
    temp = a[0]
    for i in range(1, size):
        temp = min(temp, a[i])
    return temp

def max_element(a, size):
    temp = a[0]
    for i in range(1, size):
        temp = max(temp, a[i])
    return temp

a = [1,13,49,2,186,444,3902,32,666,45]
size = len(a)
print("Smallest element of array is =", min_element(a, size))
print("Largest element of array is =", max_element(a, size))