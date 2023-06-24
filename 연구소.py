# 14502. 분류: 구현
import sys
input = sys.stdin.readline
import copy

n, m = map(int, input().split())
a = []
for i in range(n):
    a.append(list(map(int, input().split())))

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
answer = 0

def dfs(v):
    global dx, dy, n, m, copya
    x, y = v[0], v[1]
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx >= 0 and ny >= 0 and nx < n and ny < m and copya[nx][ny] == 0:
            copya[nx][ny] = 2
            dfs([nx, ny])


def virus_spread():
    count = 0
    global two, copya
    for v in two:
        dfs(v)
    for i in range(n):
        for j in range(m):
            if copya[i][j] == 0:
                count += 1
    return count

# 0인 부분, 2인 부분 각각 리스트에 담아두기
zero = []
two = []
for i in range(n):
    for j in range(m):
        if a[i][j] == 0:
            zero.append([i, j])
        elif a[i][j] == 2:
            two.append([i, j])
# 벽 세우기
from itertools import combinations
for i in combinations(zero, 3): # i -> ([1,2], [2,3], [3,4])
    copya = copy.deepcopy(a)
    for j in i:
        copya[j[0]][j[1]] = 1
    answer = max(virus_spread(), answer)

print(answer)
