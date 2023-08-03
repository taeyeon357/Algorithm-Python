n = int(input())

# 1
# 10
# 101 100
# 1010 1001 1000
# 10101 10100 10010 10000 10001

dp = [[0]*2 for _ in range(n+1)]

dp[1][1] = 1 #한자리 1로 끝나는 이친수

if n > 1:
    dp[2][0] = 1 

    for i in range(3, n+1):
        dp[i][0] = dp[i-1][1] + dp[i-1][0]
        dp[i][1] = dp[i-1][0]

print(sum(dp[n]))