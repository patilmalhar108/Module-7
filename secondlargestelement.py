def print_second_largest(a, size):
    largest = second_largest = -2147483648
    for i in range(size):
        if (a[i] > largest):
            second_largest = largest
            largest = a[i]
        elif (a[i] > second_largest and a[i] != largest):
            second_largest = a[i]
    print(second_largest)

a = [1,2,3,4,5,6,7,8,9]
size = len(a)
print_second_largest(a, size)