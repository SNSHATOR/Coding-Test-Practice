# 4673 분류: 구현

notselfnum = []
start = 1
while start <= 10000:
    b = start
    while True:
        a = str(b)
        for i in range(len(a)):
            b += int(a[i])
        if b <= 10000:
            notselfnum.append(b)
        else:
            break
    start += 1

all = {i for i in range(1, 10001)}
result = all - set(notselfnum)
for i in sorted(result):
    print(i)