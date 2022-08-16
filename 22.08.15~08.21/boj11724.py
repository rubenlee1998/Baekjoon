import sys
sys.setrecursionlimit(10000)

def dfs(v):
    visited[v] = True
    for i in graph[v]:
        if not visited[i]:
            dfs(i)


n, m = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(n+1)]
visited = [False]*(n+1)
count = 0

for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

for j in range(1, n+1):
    if not visited[j]:
        dfs(j)
        count += 1

print(count)
