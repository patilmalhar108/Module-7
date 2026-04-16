print("Write a program to find the maximum contigues circular sum. This is an advanced version of Kadane algorithm. Max so far is equal to final best answer. Max end here is eqaul to current running sum")
def kadone(a):
    n = len(a)
    max = 0
    cmax = 0
    for i in range(0, n):
        cmax = cmax + a[i]
        if cmax < 0:
            cmax = 0
        if max < cmax:
            max = cmax
    return max

def circular_sum(a):
    n = len(a)
    max_kadone = kadone(a)
    max_wrap = 0
    for i in range(0,n):
        max_wrap = max_wrap + a[i]
        a[i] = -a[i]
    max_wrap = max_wrap + kadone(a)
    if max_wrap > max_kadone:
        return max_wrap
    else:
        return max_kadone
    
a = [11,10,-20,5,-3,-5,8,-13,10]
print("Maximum circular sum is =", circular_sum(a))