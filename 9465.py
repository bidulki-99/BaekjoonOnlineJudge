import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    dp = [list(map(int, input().split())) for _ in range(2)]
    score = 0

    if len(dp[0]) >= 2:
        dp[0][1] += dp[1][0]
        dp[1][1] += dp[0][0]

        for i in range(2, n):
            dp[0][i] += max(dp[1][i-1], dp[1][i-2])
            dp[1][i] += max(dp[0][i-1], dp[0][i-2])

        print(max(dp[0][n-1], dp[1][n-1]))

    else:
        print(max(dp[0][0], dp[1][0]))