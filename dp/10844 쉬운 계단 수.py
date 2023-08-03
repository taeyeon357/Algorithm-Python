n = int(input())

dp = [[0]*10 for _ in range(n+1)]

dp[1] = [0,1,1,1,1,1,1,1,1,1]

if n>=2:
    for i in range(2,n+1): #숫자 길이
        dp[i][0] = dp[i-1][1]
        for j in range(1,9): # j로 끝나는 계단 수 개수
            dp[i][j] = dp[i-1][j-1] + dp[i-1][j+1]
        dp[i][9] = dp[i-1][8]


print(sum(dp[n])%1000000000)