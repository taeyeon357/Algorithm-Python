import sys
sys.setrecursionlimit(10**8)
n, m = map(int, input().split())

map = [list(map(int,input().split())) for _ in range(n)]
dp = [[-1]*m for _ in range(n)]

dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]

def inMap(x, y):
    return 0 <= x < n and 0 <= y < m

def visit(x, y):
    if x == n-1 and y == m-1:
        return 1
    
    if dp[x][y] == -1:
        dp[x][y] = 0

        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]

            if inMap(nx, ny) and map[x][y] > map[nx][ny]:
                dp[x][y] += visit(nx, ny)
    return dp[x][y]


print(visit(0,0))