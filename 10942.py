import sys
input = sys.stdin.readline

n = int(input())
s = list(map(int, input().split()))

dp = [[0] * n for _ in range(n)]

for i in range(n):
    dp[i][i] = 1

for i in range(n-1):
    if s[i] == s[i+1]:
        dp[i][i+1] = 1

for i in range(2, n):
    for j in range(n-i):
        if s[j] == s[j+i] and dp[j+1][j+i-1] == 1:
            dp[j][j+i] = 1

m = int(input())
for _ in range(m):
    a, b = map(int, input().split())
    print(dp[a-1][b-1])
