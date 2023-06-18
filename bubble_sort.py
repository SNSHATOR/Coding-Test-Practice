def bubble_sort(array):
    length = len(array)
    while True:
        change = False
        for i in range(length - 1):
            if array[i] > array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]
                change = True
        length -= 1
        if not change:
            break

# 테스트
array = list(map(int, input().split()))
bubble_sort(array)
print(array)