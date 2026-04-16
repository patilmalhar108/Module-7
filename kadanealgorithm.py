print("Write a program to find maximum sub array sum")
def max_sub_arr(arr, arrsize):
    max = -99999999999
    cmax = 0
    for i in range(0, arrsize):
        cmax = cmax + arr[i]
        if max < cmax:
            max = cmax
        if cmax < 0:
            cmax = 0
    return max

arr = [1,2,3,-4,5,-22,-4,25,2,-9]
print(max_sub_arr(arr, len(arr)))