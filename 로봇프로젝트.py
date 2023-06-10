import sys
input = sys.stdin.readline

while(True):
    try:
        hole_size = int(input())
        n = int(input())
        blocks = []
        for _ in range(n):
            blocks.append(int(input()))
    except:
        break

    blocks.sort()
    hole_size *= 10000000

    result = 0
    for block in blocks:
        if block > hole_size / 2:
            break
        start, end = 0, n - 1
        while start <= end:
            mid = (start + end) // 2
            if blocks[mid] == hole_size - block:
                result = block
                break
            elif blocks[mid] < hole_size - block:
                start = mid + 1
            else:
                end = mid - 1

    if result == hole_size / 2 and blocks.count(result) == 1:
        result = 0

    if result != 0:
        print(f"yes {result} {hole_size - result}")
    else:
        print("danger")
