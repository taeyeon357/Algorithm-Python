from collections import deque
n = int(input())

arr = [list(map(int, input())) for _ in range(n)]

dx = [1,-1,0,0]
dy = [0,0,1,-1]

def inRange(a,b):
    return 0<=a<n and 0<=b<n

v = [[0]*n for _ in range(n)]
result = []
q = deque()
for i in range(n):
    for j in range(n):
        if arr[i][j] == 0:
            continue
        if v[i][j] == 0:
            q.append((i,j))
            v[i][j] = 1
        
        cnt = 0
        while q:
            a, b = q.pop()
            cnt += 1
            for k in range(4):
                nx = a + dx[k]
                ny = b + dy[k]

                if inRange(nx, ny) and arr[nx][ny] == 1 and v[nx][ny] == 0:
                    q.append((nx,ny))
                    v[nx][ny] = 1
        if cnt > 0: 
            result.append(cnt)

result.sort()
print(len(result))
for r in result:
    print(r)