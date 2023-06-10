# 1041 주사위
n = int(input())
dice = list(map(int, input().split()))

three = min(dice[0], dice[5]) + min(dice[1], dice[4]) + min(dice[2], dice[3])
one = min(dice)
two = min(min(dice[0], dice[5]) + min(dice[1], dice[4]), min(dice[1], dice[4]) + min(dice[2], dice[3]), min(dice[0], dice[5]) + min(dice[2], dice[3]))

if n == 1:
    print(sum(dice) - max(dice))
else:
    print(three * 4 + two * (8 * n - 12) + one * (5 * (n ** 2) - 16 * n + 12))