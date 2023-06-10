#1316 분류: 구현
n = int(input())
words = []
result = n
for i in range(n):
    words.append(input())
    checked = ['']
    for letter in words[i]:
        if letter == checked[len(checked) - 1]:
            pass
        else:
            if letter not in checked:
                checked.append(letter)
            else:
                result -= 1
                break

print(result)