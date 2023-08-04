from collections import deque

n, m = map(int, input().split())

arr = [list(map(int, input())) for _ in range(n)]

dx = [1,-1,0,0]
dy = [0,0,1,-1]
def inRange(x,y):
    return 0 <= x < n and 0 <= y < m

def bfs(x, y):
    q = deque()
    q.append((x,y))
    
    while q:
        r,c = q.popleft()

        for i in range(4):
           nx = r + dx[i]
           ny = c + dy[i]
            
           if inRange(nx, ny) and arr[nx][ny] == 1:
               arr[nx][ny] = arr[r][c] + 1
               q.append((nx, ny))


bfs(0,0)
print(arr[n-1][m-1])
