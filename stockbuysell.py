def calculate_profit(arr, arrsize):
    profit = 0
    for i in range(1, arrsize):
        if arr[i] > arr[i -1 ]:
            profit = profit + arr[i] - arr[i - 1]
    return profit 

price = [7, 3, 4, 1, 11, 20, 21]
profit = calculate_profit(price, 7)
print("Maximam profit is =", profit)