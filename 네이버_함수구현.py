def solution(arr):
    checked = []
    result = []
    for num in arr:
        if num not in checked:
            checked.append(num)
            count = 0
            for i in arr:
                if num == i:
                    count += 1
            if count > 1:
                result.append(count)
    if len(result) == 0:
        return [-1]
    else:
        return result

import sys
input = sys.stdin.readline

arr = list(map(int, input().split()))
print(solution(arr))