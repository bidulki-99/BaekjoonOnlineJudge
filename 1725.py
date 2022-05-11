import sys
input = sys.stdin.readline

n = int(input())
hist = []
for i in range(n):
    hist.append(int(input()))
stack = []
ans = 0
for i in range(n):
    while stack and hist[stack[-1]] > hist[i]:
        check = stack.pop()

        if stack:
            ans = max(ans, hist[check] * (i - stack[-1] - 1))
        else:
            ans = max(ans, hist[check] * i)
    stack.append(i)

while stack:
    temp = stack.pop()

    if stack:
        ans = max(ans, hist[temp] * (n - stack[-1] - 1))
    else:
        ans = max(ans, hist[temp] * n)

print(ans)
