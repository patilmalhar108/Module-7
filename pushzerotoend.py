def push_zero(arr,arrsize):
    zero = 0
    nonzero = 0
    while nonzero != arrsize:
        if arr[nonzero] != 0:
            arr[nonzero], arr[zero] = arr[zero], arr[nonzero]
            zero = zero + 1
        nonzero = nonzero + 1

arr = [1,22,3,0,0,2,0,34,0,29,0,0,67]
arrsize = len(arr)
print(arr)
print("Array after pushing all 0's to end of array: ")
push_zero(arr, arrsize)
print(arr)