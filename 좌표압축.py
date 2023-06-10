# 18870

n = int(input())
coordinates = list(map(int, input().split()))

coordinates_sorted = sorted(coordinates)
coordinates_sorted = list(dict.fromkeys(coordinates_sorted))

result = {}
for i in range(len(coordinates_sorted)):
    result[coordinates_sorted[i]] = i

for i in coordinates:
    print(result[i], end = ' ')