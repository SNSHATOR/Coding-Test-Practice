testcase = int(input())
cases = []
for i in range(testcase):
    cases.append(list(map(int, input().split())))

for i in cases:
    sum = 0
    for j in range(i[0]):
        sum += i[j + 1]
    i.append(sum / i[0])

result = []

for i in cases:
    count = 0
    for j in range(i[0]):
        if i[j + 1] > i[i[0] + 1]:
            count += 1
    result.append(count)

for i in range(testcase):
    result[i] = result[i] / cases[i][0] * 100

for i in result:
    print(f'{i:.3f}%')