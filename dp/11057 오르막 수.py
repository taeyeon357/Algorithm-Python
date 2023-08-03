n = int(input())

dp = [[0] * 10 for _ in range(n+1)]

dp[1] = [1,1,1,1,1,1,1,1,1,1] #i로 시작하는 오르막 수의 개수

if n>=2:
    for i in range(2,n+1):
        #dp[i][0] = sum(dp[i-1][1:10])
        for j in range(10):
            dp[i][j] = sum(dp[i-1][j:])
print(sum(dp[n]))