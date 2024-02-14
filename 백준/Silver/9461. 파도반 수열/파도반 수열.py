def padovan(n):
    dp = [0] * (n + 1)
    dp[1] = 1
    if n >= 2:
        dp[2] = 1
    if n >= 3:
        dp[3] = 1

    for i in range(4, n + 1):
        dp[i] = dp[i - 2] + dp[i - 3]

    return dp[n]

for _ in range(int(input())):
    print(padovan(int(input())))