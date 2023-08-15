n = int(input())
m = int(input())

arr = [[] for _ in range(n+1)]
v = [0] * (n+1)

for _ in range(m):
    a, b = map(int, input().split())
    if a not in arr[b]:
        arr[b].append(a)

    if b not in arr[a]:
        arr[a].append(b)


def visit(x):
    v[x] = 1
    for e in arr[x]:
        if v[e] == 0:
            visit(e)


visit(1)
print(sum(v)-1)            