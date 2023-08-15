from collections import deque
n = int(input())
m = int(input())

g = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    if b not in g[a]:
        g[a].append(b)

    if a not in g[b]:
        g[b].append(a)

q = deque()
q.append(1)

visited = [0] * (n+1)
visited[1] = 1
cnt = 0
while q:
    tmp = q.pop()
    
    for e in g[tmp]:
        if visited[e] == 0:
            q.append(e)
            visited[e] = 1
            cnt += 1

print(cnt)