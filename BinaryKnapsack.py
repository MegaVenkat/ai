
def binaryKnapsack():

    n = int(input("Enter no of items : "))
    w = int(input("Enter capacity of knapsack : "))
    value = list(
        map(int, input("Enter value of items separated by spaces : ").split()))
    weight = list(
        map(int, input("Enter weight of items separted by spaces : ").split()))

    dp = [[0 for x in range(w+1)] for y in range(n+1)]
    for i in range(n):
        for j in range(w+1):
            if dp[i][j] == 0:
                dp[i+1][j] = dp[i][j]
            if j >= weight[i]:
                dp[i+1][j] = max(dp[i][j], dp[i][j-weight[i]] + value[i])

    print("maximum profit that can be obtained is : ", dp[n][w])


binaryKnapsack()
