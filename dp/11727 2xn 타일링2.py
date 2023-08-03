n = int(input())

dp = [0 for _ in range(n+1)] 
#dp = [0,1] -> dp.append() 가 더 빠르고, 예외처리 안해도 돼서 편리

dp[1] = 1

if n >= 2: #1<=n<=1000 이므로
    dp[2] = 3
    for i in range(3,n+1):
        dp[i] = (dp[i-1] + dp[i-2] * 2) % 10007

    
print(dp[n])

