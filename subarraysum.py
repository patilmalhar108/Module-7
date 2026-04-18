def sub_array_sum(arr, n, sum):
    for i in range(n):
        current_sum = arr[i]
        j = i + 1
        while j <= n:
            if current_sum == sum:
                print("Sum found between: ")
                print("Indexs %d and %d"%(i, j - 1))
                return 1
            if current_sum > sum or j == n:
                break
            current_sum = current_sum + arr[j]
            j = j + 1
    print("No sub array found")
    return 0

arr = [3,5,1,2,9,8,-2]
n = len(arr)
sum = 6
sub_array_sum(arr, n, sum)