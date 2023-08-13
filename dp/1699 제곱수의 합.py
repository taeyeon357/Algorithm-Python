n = int(input())

dp = [i for i in range(n+1)]

for i in range(2, n+1):
    for j in range(1, i):
        if i < j*j:
            break
        
        if dp[i] > dp[i-j*j] + 1:
            dp[i] = dp[i-j*j] + 1

print(dp[n])