# 1987
r, c = map(int, input().split())
graph = []
for i in range(r):
    graph.append(list(input()))

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

# DFS
used_letters = []
used_letters.append(graph[0][0])
global max1
max1 = 0
def dfs(x, y):
    global max1
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx > -1 and nx < r and ny > -1 and ny < c and graph[nx][ny] not in used_letters:
            used_letters.append(graph[nx][ny])
            if len(used_letters) > max1:
                max1 = len(used_letters)
            dfs(nx, ny)
    used_letters.pop()
while(used_letters):
    dfs(0, 0)
print(max1)