#1926 그림
import sys
sys.setrecursionlimit(10**6)

n, m = map(int, input().split())
graph = []
for i in range(n):
    graph.append(list(map(int, input().split())))

visited = [[0] * m for _ in range(n)]
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def dfs(x, y):
    global area
    area += 1
    visited[x][y] = 1
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 1 and visited[nx][ny] == 0:
            dfs(nx, ny)

count = 0
global area
area = 0
biggest_area = 0
for i in range(n):
    for j in range(m):
        if graph[i][j] == 1 and visited[i][j] == 0:
            dfs(i, j)
            if biggest_area < area:
                biggest_area = area
            count += 1
            area = 0

print(count)
print(biggest_area)