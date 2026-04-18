def equal_point(arr):
    left_side_sum = 0
    right_side_sum = 0
    n = len(arr)
    for i in range(n):
        left_side_sum = 0
        right_side_sum = 0
        for j in range(i):
            left_side_sum = left_side_sum + arr[j]
        for j in range(i + 1, n):
            right_side_sum = right_side_sum + arr[j]
        if left_side_sum == right_side_sum:
            return i
    return -i

arr = [2,4,1,-4,5,3,-1]
print("Elements are =", equal_point(arr))