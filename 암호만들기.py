# 백준 1759
from itertools import combinations

l, c = map(int, input().split())
alpha = list(input().split())
answer = []

v = ['a', 'e', 'i', 'o', 'u']
consonants = []
vowels = []
for a in alpha:
    if a in v:
        vowels.append(a)
    else:
        consonants.append(a)

# 모음 최대 개수 제한
if l - len(vowels) >= 2:
    vmax = len(vowels)
else:
    vmax = l - 2

for i in range(1, vmax + 1):
    j = l - i
    vv = list(combinations(vowels, i))
    cc = list(combinations(consonants, j))
    for m in vv:
        for n in cc:
            tmp = []
            tmp.extend(m)
            tmp.extend(n)
            tmp.sort()
            answer.append(''.join(tmp))

answer.sort()
for i in answer:
    print(i)