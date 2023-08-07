n, k = map(int, input().split())

coins = [int(input()) for _ in range(n)]

dp = [10001 for _ in range(k+1)]
dp[0] = 0

for c in coins:
    for i in range(c, k+1):
        dp[i] = min(dp[i], dp[i-c] + 1)

if dp[k] == 10001:
    print(-1)
else:
    print(dp[k])


'''
정석적인 dp 방식대로 차례대로 채워나간다고 생각해서 
c가 크면 범위를 벗어날 수 있겠다는 생각에 try-except문을 사용
-> 틀림
생각을 전환하여 c를 기준으로 계산하는 방법을 생각하지 못함, 
항상 다양한 방향에서 생각해보자!
'''