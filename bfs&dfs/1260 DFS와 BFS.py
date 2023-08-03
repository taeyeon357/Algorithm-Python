from collections import deque

#정점의 개수(n), 간선의 개수(m), 탐색 시작(v)
n, m, v = map(int, input().split())

graph = [[] for _ in range(n+1)]

for i in range(m):
    a,b = map(int, input().split())
    if b not in graph[a]:
        graph[a].append(b)
        graph[b].append(a)

for i in range(1,n+1):
    graph[i].sort()


visited = [-1] * (n+1)
def dfs(n):
    if visited[n] == -1:
        visited[n] = 1
        print(n, end=' ')
        for i in graph[n]:
            dfs(i)

check = [-1] * (n+1)
def bfs(n):
    q = deque()
    if check[n] == -1:
        q.append(n)
        check[n] = 1
    while q:
        tmp = q.popleft()
        print(tmp, end=' ')
        for i in graph[tmp]:
            if check[i] == -1:
                q.append(i)
                check[i] = 1
    return
    
dfs(v)
print("")
bfs(v)
