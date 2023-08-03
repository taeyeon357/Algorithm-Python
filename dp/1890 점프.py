n = int(input())

board = []
for _ in range(n):
    board.append(list(map(int,input().split())))

dp = [[0]*n for _ in range(n)]

dp[0][0] = 1

for i in range(n):
    for j in range(n):
        if i == n-1 and j == n-1:
            print(dp[i][j])
            break
        if dp[i][j] > 0:
            x = board[i][j]
            if i + x < n:
                dp[i+x][j] += dp[i][j]
            if j + x < n:
                dp[i][j+x] += dp[i][j]
            

