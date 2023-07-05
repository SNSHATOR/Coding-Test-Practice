#20529

from itertools import combinations
import sys
input = sys.stdin.readline

# 두 mbti끼리의 거리를 계산하는 함수
def distance(a, b):
    count = 0
    for i in range(4):
        if a[i] != b[i]:
            count += 1
    return count

# 세 mbti끼리의 거리의 합을 반환하는 함수
def three(abc):
    return distance(abc[0], abc[1]) + distance(abc[0], abc[2]) + distance(abc[1], abc[2])

t = int(input())
result = []
for _ in range(t):
    n = int(input())
    mbti = list(input().split())
    if n > 32: # 33개 이상이면 mbti 같은 세사람이 무조건 있으니까 0
        result.append(0)
    else:
        min = 1e9
        for combination in combinations(mbti, 3):
            v = three(combination)
            if v < min:
                min = v
        result.append(min)

for r in result:
    print(r)