n = int(input())
for i in range(n - 1):
    print(' ' * (n - 1 - i), end='')
    print('*' * (2 * i + 1))
print('*' * (2 * n - 1))
for i in range(n - 1):
    print(' ' * (i + 1), end='')
    print('*' * ( (2 * n - 3) - 2 * i))